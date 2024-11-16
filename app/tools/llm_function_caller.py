from typing import Any, Dict, List, Type, Optional
from pydantic import BaseModel
from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion import Choice
import json

class LLMFunctionCaller:
    def __init__(self, llm_manager: 'LLMManager'):
        self.llm_manager = llm_manager

    async def call_with_schema(
        self, 
        prompt: str, 
        output_schema: Type[BaseModel], 
        model: Optional[str] = None,
        **kwargs
    ) -> BaseModel:
        # Create tool schema for the LLM
        tool_schema = {
            "type": "function",
            "function": {
                "name": output_schema.__name__.lower(),
                "description": output_schema.__doc__ or "Generate structured output",
                "parameters": output_schema.schema()
            }
        }

        try:
            # Generate completion with tool calling
            response = await self.llm_manager.generate_with_tools(
                prompt,
                tools=[tool_schema],
                tool_choice={"type": "function", "function": {"name": tool_schema["function"]["name"]}},
                model=model,
                **kwargs
            )

            # Handle the response
            if not isinstance(response, ChatCompletion):
                raise ValueError("Unexpected response type")

            tool_calls = response.choices[0].message.tool_calls
            if not tool_calls:
                raise ValueError("No tool calls in response")

            # Parse and validate response
            result = json.loads(tool_calls[0].function.arguments)
            return output_schema.parse_obj(result)

        except Exception as e:
            raise ValueError(f"Failed to generate structured output: {str(e)}") 