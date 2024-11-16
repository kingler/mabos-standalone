import asyncio
import logging
import os
import tiktoken
from typing import Any, Dict, Optional, List
import json
import uuid
import time

import httpx
import openai
import yaml
from anthropic import Anthropic
from pydantic import BaseModel, Field, validator
from tenacity import retry, stop_after_attempt, wait_exponential
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import Choice

from app.config.config import LLM_CONFIG, API_KEYS

logger = logging.getLogger(__name__)

class LLMManager(BaseModel):
    llms_config: Dict[str, Any] = Field(default_factory=lambda: LLM_CONFIG)
    api_keys: Dict[str, str] = Field(default_factory=lambda: API_KEYS)
    default_model: str = Field(default=None)
    model_performance: Dict[str, float] = Field(default_factory=dict)
    model_costs: Dict[str, Dict[str, float]] = Field(default_factory=dict)
    tokenizers: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        if not self.llms_config:
            raise ValueError("LLM configuration is empty. Check your LLM_CONFIG in app/config/config.py")
        if 'llms' not in self.llms_config:
            raise ValueError(f"Expected 'llms' key in config, got keys: {self.llms_config.keys()}")
        self.default_model = self.llms_config['llms']['text_generation']['default']
        if not self.default_model:
            raise ValueError("Default model not found in configuration")
        self.api_keys = self.llms_config.get('api_keys', {})
        self.model_performance = self._load_model_performance()
        self.model_costs = self._load_model_costs()
        self._validate_api_keys()

    async def generate_text(self, prompt: str, model: Optional[str] = None) -> str:
        model = model or self.default_model
        model_config = self.get_model_config(model)
        
        if 'claude' in model:
            return await self._anthropic_completion(prompt, model, model_config)
        elif 'gpt' in model:
            return await self._openai_completion(prompt, model, model_config)
        elif 'gemini' in model:
            return await self._gemini_completion(prompt, model, model_config)
        elif 'llama' in model:
            return await self._groq_completion(prompt, model, model_config)
        else:
            raise ValueError(f"Unsupported model: {model}")

    def get_model_config(self, model_name: str) -> Dict[str, Any]:
        for model in self.llms_config['text_generation']['available']:
            if model_name in model:
                return model[model_name]
        raise ValueError(f"Model {model_name} not found in configuration")

    def _validate_api_keys(self):
        if missing_keys := [key for key, value in self.api_keys.items() if not value]:
            raise ValueError(f"Missing API keys: {', '.join(missing_keys)}")

    def _load_model_performance(self) -> Dict[str, float]:
        if 'llms' not in self.llms_config or 'text_generation' not in self.llms_config['llms']:
            logging.warning("Expected structure not found in llms_config")
            return {}
        
        available_models = self.llms_config['llms']['text_generation'].get('available', [])
        return {model: config.get('performance', 0.5) 
                for model_dict in available_models 
                for model, config in model_dict.items()}

    def _load_model_costs(self) -> Dict[str, Dict[str, float]]:
        if 'llms' not in self.llms_config or 'text_generation' not in self.llms_config['llms']:
            logging.warning("Expected structure not found in llms_config")
            return {}
        
        available_models = self.llms_config['llms']['text_generation'].get('available', [])
        return {model: {'input': config.get('cost_input', 0), 'output': config.get('cost_output', 0)} 
                for model_dict in available_models 
                for model, config in model_dict.items()}

    def _load_tokenizers(self):
        for model_dict in self.llms_config['text_generation']['available']:
            for model, config in model_dict.items():
                if 'gpt' in model:
                    self.tokenizers[model] = tiktoken.encoding_for_model(model)
                elif 'claude' in model:
                    # Claude uses GPT-4's tokenizer
                    self.tokenizers[model] = tiktoken.encoding_for_model("gpt-4")

    def estimate_tokens(self, text: str, model: str) -> int:
        if tokenizer := self.tokenizers.get(model):
            return len(tokenizer.encode(text))
        else:
            # Fallback to a simple estimation if no specific tokenizer is available
            return len(text.split())

    def estimate_cost(self, text: str, model: str) -> float:
        tokens = self.estimate_tokens(text, model)
        cost_info = self.model_costs.get(model, {})
        input_cost = cost_info.get('input', 0) * (tokens / 1000)
        output_cost = cost_info.get('output', 0) * (tokens / 1000)  # Assuming same token count for output
        return input_cost + output_cost

    def select_best_model(self, task: str, max_tokens: int) -> str:
        task_complexity = self._estimate_task_complexity(task)
        
        best_model = None
        best_score = float('-inf')

        for model_dict in self.llms_config['text_generation']['available']:
            for model, config in model_dict.items():
                performance_score = self.model_performance.get(model, 0)
                cost = (self.model_costs[model]['input'] + self.model_costs[model]['output']) * (max_tokens / 1000)
                
                score = (performance_score * task_complexity) / (cost + 0.001)
                
                if score > best_score:
                    best_score = score
                    best_model = model

        logger.info(f"Selected model {best_model} for task: {task}")
        return best_model

    def _estimate_task_complexity(self, task: str) -> float:
        complexity = min(len(task) / 100, 1)
        complex_keywords = ['analyze', 'evaluate', 'synthesize', 'create', 'design']
        if any(keyword in task.lower() for keyword in complex_keywords):
            complexity += 0.2
        return min(complexity, 1)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _anthropic_completion(self, prompt: str, model: str, model_config: Dict[str, Any]) -> str:
        anthropic_client = Anthropic(api_key=self.api_keys['anthropic'])
        response = await anthropic_client.messages.create(
            model=model,
            max_tokens=model_config.get('max_tokens', 4096),
            temperature=model_config.get('temperature', 0.7),
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text

    async def _openai_completion(self, prompt: str, model: str, model_config: Dict[str, Any]) -> str:
        openai.api_key = self.api_keys['openai']
        response = await openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=model_config.get('max_tokens', 4096),
            temperature=model_config.get('temperature', 0.7)
        )
        return response.choices[0].message.content

    async def _gemini_completion(self, prompt: str, model: str, model_config: Dict[str, Any]) -> str:
        import google.generativeai as genai
        genai.configure(api_key=self.api_keys['gemini'])
        
        # Load the appropriate Gemini model
        gemini_model = genai.GenerativeModel(model)
        
        # Generate the completion
        response = gemini_model.generate_content(
            [prompt],
            generation_config=model_config.get('generation_config', {}),
            safety_settings=model_config.get('safety_settings', {}),
            stream=False
        )
        
        # Extract and return the generated text
        return response[0].text

    async def _groq_completion(self, prompt: str, model: str, model_config: Dict[str, Any]) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                model_config['url'],
                headers={
                    "Authorization": f"Bearer {self.api_keys['groq']}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": model_config.get('max_tokens', 4096),
                    "temperature": model_config.get('temperature', 0.7)
                }
            )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise Exception(f"Error generating text with Groq: {response.text}")

    async def generate_image(self, prompt: str, model: Optional[str] = None) -> bytes:
        model = model or self.llms_config['image_generation']['default']
        model_config = next(m for m in self.llms_config['image_generation']['available'] if model in m)[model]
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                model_config['url'],
                headers={"Authorization": f"Bearer {self.api_keys['stability_ai']}"},
                json={"text_prompts": [{"text": prompt}]}
            )
        
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error generating image: {response.text}")

    async def generate_speech(self, text: str, voice: str = "alloy") -> bytes:
        from deepgram import DeepgramClient, SpeakOptions

        deepgram = DeepgramClient(api_key=self.api_keys['deepgram'])
        options = SpeakOptions(model=voice)

        response = await deepgram.speak.asyncrest.v("1").save("output.mp3", {"text": text}, options)
        
        if response.status_code != 200:
            raise Exception(f"Error generating speech: {response.text}")
        
        with open("output.mp3", "rb") as audio_file:
            return audio_file.read()

    async def speech_to_text(self, audio_file_path: str, model: str = "whisper-1") -> str:
        from deepgram import DeepgramClient, TranscriptionOptions

        deepgram = DeepgramClient(api_key=self.api_keys['deepgram'])
        options = TranscriptionOptions(model=model)

        with open(audio_file_path, "rb") as audio_file:
            response = await deepgram.transcription.prerecorded(audio_file, options)
        
        if response.status_code == 200:
            return response.json()['results']['channels'][0]['alternatives'][0]['transcript']
        else:
            raise Exception(f"Error transcribing speech: {response.text}")

    async def generate_with_tools(
        self,
        prompt: str,
        tools: List[Dict],
        tool_choice: Dict[str, Any],
        model: Optional[str] = None,
        **kwargs
    ) -> ChatCompletion:
        model = model or self.default_model
        model_config = self.get_model_config(model)

        if 'claude' in model:
            return await self._anthropic_tool_completion(prompt, tools, tool_choice, model, model_config)
        elif 'gpt' in model:
            return await self._openai_tool_completion(prompt, tools, tool_choice, model, model_config)
        else:
            raise ValueError(f"Tool calling not supported for model: {model}")

    async def _openai_tool_completion(
        self,
        prompt: str,
        tools: List[Dict],
        tool_choice: Dict[str, Any],
        model: str,
        model_config: Dict[str, Any]
    ) -> ChatCompletion:
        client = OpenAI(api_key=self.api_keys['openai'])
        
        try:
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                tools=tools,
                tool_choice=tool_choice,
                **model_config
            )
            return response
        except Exception as e:
            raise ValueError(f"OpenAI API error: {str(e)}")

    async def _anthropic_tool_completion(
        self,
        prompt: str,
        tools: List[Dict],
        tool_choice: Dict[str, Any],
        model: str,
        model_config: Dict[str, Any]
    ) -> ChatCompletion:
        # Format the tool schema as part of the prompt
        schema_prompt = f"\nPlease provide output in the following JSON schema:\n{json.dumps(tools[0]['function']['parameters'], indent=2)}"
        
        try:
            response = await self._anthropic_completion(prompt + schema_prompt, model, model_config)
            
            # Create a ChatCompletion-like response
            return ChatCompletion(
                id="anthropic_" + str(uuid.uuid4()),
                choices=[Choice(
                    index=0,
                    message={
                        "role": "assistant",
                        "tool_calls": [{
                            "id": "call_" + str(uuid.uuid4()),
                            "type": "function",
                            "function": {
                                "name": tools[0]["function"]["name"],
                                "arguments": response
                            }
                        }]
                    }
                )],
                created=int(time.time())
            )
        except Exception as e:
            raise ValueError(f"Anthropic API error: {str(e)}")

# Usage example
async def main():
    manager = LLMManager()
    result = await manager.generate_text("Explain the concept of quantum computing.")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())