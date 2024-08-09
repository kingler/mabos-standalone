import httpx
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
import os
import logging
from anthropic import Anthropic
import yaml
import openai
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class LLMManager(BaseModel):
    llms_config: Dict[str, Any] = Field(...)
    api_key: str = Field(...)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, llms_config: Dict[str, Any], api_key: str):
        super().__init__(llms_config=llms_config, api_key=api_key)
        self.default_model = llms_config['llms']['text_generation']['default']

    async def generate_text(self, prompt: str) -> str:
        model_config = self.get_model_config(self.default_model)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                model_config['url'],
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": self.api_key,
                },
                json={
                    "model": self.default_model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": model_config['max_tokens'],
                    "temperature": model_config['temperature'],
                },
                timeout=llms_config['default_params']['timeout']
            )
        
        if response.status_code == 200:
            return response.json()['content'][0]['text']
        else:
            raise Exception(f"Error generating text: {response.text}")

    def get_model_config(self, model_name: str) -> Dict[str, Any]:
        for model in llms_config['llms']['text_generation']['available']:
            if model_name in model:
                return model[model_name]
        raise ValueError(f"Model {model_name} not found in configuration")

    def get_default_llm(self):
        default_llm = llms_config['llms']['text_generation']['default']
        available_llms = llms_config['llms']['text_generation']['available']
        llm_config = next(
            (llm for llm in available_llms if default_llm in llm),
            None
        )
        return llm_config[default_llm] if llm_config else None

    def _validate_api_keys(self):
        missing_keys = [key for key, value in self.api_keys.items() if value is None]
        if missing_keys:
            raise ValueError(f"Missing API keys: {', '.join(missing_keys)}")
        for provider, key in self.api_keys.items():
            if not key:
                logger.warning(f"API key for {provider} is not set. Some functionality may be limited.")

    def _load_model_performance(self) -> Dict[str, float]:
        # Load model performance scores (0-1 scale)
        return {
            'gpt-4': 0.95,
            'gpt-3.5-turbo': 0.85,
            'palm2': 0.80,
            'gemini': 0.90,
            'claude': 0.88,
            'mistral-7b': 0.75,
            'mixtral-8x7b': 0.82,
        }

    def _load_model_costs(self) -> Dict[str, float]:
        # Load model costs per 1000 tokens (approximate values)
        return {
            'gpt-4': 0.06,
            'gpt-3.5-turbo': 0.002,
            'palm2': 0.001,
            'gemini': 0.0035,
            'claude': 0.015,
            'mistral-7b': 0.0005,
            'mixtral-8x7b': 0.0008,
        }

    def select_best_model(self, task: str, max_tokens: int) -> str:
        available_models = llms_config['llms']['text_generation']['available']
        task_complexity = self._estimate_task_complexity(task)
        
        best_model = None
        best_score = float('-inf')

        for model in available_models:
            performance_score = self.model_performance.get(model, 0)
            cost = self.model_costs.get(model, float('inf')) * (max_tokens / 1000)
            
            # Calculate a score based on performance, cost, and task complexity
            score = (performance_score * task_complexity) / (cost + 0.001)  # Adding 0.001 to avoid division by zero
            
            if score > best_score:
                best_score = score
                best_model = model

        logger.info(f"Selected model {best_model} for task: {task}")
        return best_model

    def _estimate_task_complexity(self, task: str) -> float:
        # Simple estimation based on task length and keyword presence
        complexity = min(len(task) / 100, 1)  # 0-1 scale based on length
        complex_keywords = ['analyze', 'evaluate', 'synthesize', 'create', 'design']
        if any(keyword in task.lower() for keyword in complex_keywords):
            complexity += 0.2
        return min(complexity, 1)  # Ensure it doesn't exceed 1

    async def get_text_completion_async(self, prompt: str, model: str = None, max_tokens: int = None, temperature: float = None) -> str:
        if model is None:
            model = llms_config['llms']['text_generation']['default']
        
        model_config = next(m for m in llms_config['llms']['text_generation']['available'] if model in m)[model]
        
        max_tokens = max_tokens or model_config.get('max_tokens', 4096)
        temperature = temperature or model_config.get('temperature', 0.7)

        if 'claude' in model:
            return self._anthropic_completion_with_retry(prompt, model, max_tokens, temperature)
        elif 'gpt' in model:
            return self._openai_completion(prompt, model, max_tokens, temperature)
        # Add other model providers as needed
        else:
            raise ValueError(f"Unsupported model: {model}")

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def _anthropic_completion_with_retry(self, prompt: str, model: str, max_tokens: int, temperature: float) -> str:
        import anthropic
        from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
        anthropic_client = Anthropic(api_key=self.api_key)
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text

    def _openai_completion(self, prompt: str, model: str, max_tokens: int, temperature: float) -> str:
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content

    def track_usage(self, model: str, input_tokens: int, output_tokens: int):
        # Track token usage and costs
        pass

    async def stream_completion(self, prompt: str, model: str = None):
        # Implement streaming for supported models
        pass

    def get_image(self, prompt: str, model: str = "stable-diffusion") -> str:
        # Implement image generation using Replicate API
        import replicate
        
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt}
        )
        
        return output[0]  # Returns URL of generated image

    def generate_audio(self, prompt: str, task: str) -> str:
        model = llms_config['llms']['audio']['text_to_speech']['models'][0]
        voice = llms_config['llms']['audio']['text_to_speech']['parameters']['voice']['options'][0]
        return self.text_to_speech(prompt, model, voice)

    def speech_to_text(self, audio_file_path: str, model: str = "whisper-1", **kwargs) -> str:
        audio_config = llms_config['llms']['audio']['speech_to_text']
        
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model=model,
                file=audio_file,
                **kwargs
            )
        
        return response['text']

    def text_to_speech(self, text: str, model: str = "tts-1", voice: str = "alloy", **kwargs) -> bytes:
        tts_config = llms_config['llms']['audio']['text_to_speech']
        
        response = openai.Audio.speech(
            model=model,
            input=text,
            voice=voice,
            **kwargs
        )
        
        return response.content

# Usage example:
async def main():
    manager = LLMManager()
    tasks = [
        manager.get_text_completion_async("Task 1 prompt", model="claude-3-opus-20240229"),
        manager.get_text_completion_async("Task 2 prompt", model="gemini-1.5-pro"),
        manager.get_text_completion_async("Task 3 prompt", model="gpt-4")
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

    async for chunk in manager.stream_completion("Stream this response", model="claude-3-opus-20240229"):
        print(chunk, end='', flush=True)

if __name__ == "__main__":
    asyncio.run(main())