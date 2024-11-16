import json
import logging
from typing import Any, List, Optional

from pydantic import BaseModel, Field, ConfigDict

from app.models.agent.agent import Agent
from app.models.message import ACLMessage
from app.tools.llm_manager import LLMManager


class LLMService(BaseModel):
    llm_manager: LLMManager = Field(default_factory=LLMManager)
    system_prompt: Optional[str] = Field(default=None)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(self, **data):
        # If llm_manager is provided in data, use it; otherwise create a new one
        if 'llm_manager' not in data:
            data['llm_manager'] = LLMManager()
            
        super().__init__(**data)
        self.system_prompt = self._generate_system_prompt()

    def _generate_system_prompt(self) -> str:
        return """
        You are an AI assistant specialized in creating ontologies for various business domains. Your task is to help instantiate a business domain ontology based on the provided business description. Follow these guidelines:

        1. Identify key concepts: Recognize and define the main entities in the business domain.
        2. Establish relationships: Determine how these concepts are interconnected.
        3. Define attributes: For each concept, list relevant attributes.
        4. Consider domain-specific elements: Address concepts unique to the described business domain.
        5. Think about business operations: Include concepts related to core business processes and management.
        6. Consider technical aspects: Include concepts related to any relevant technologies or systems.
        7. Regulatory compliance: Include concepts related to relevant laws and regulations.
        8. Use clear and consistent terminology: Ensure that all terms and concepts are well-defined and consistently used throughout the ontology.

        Your goal is to create a comprehensive and well-structured ontology that accurately represents the given business domain. This ontology will serve as a foundation for understanding the business model, improving operations, and developing software systems to support the business.
        """

    async def _chain_prompts(self, prompts: List[str]) -> str:
        try:
            result = ""
            for prompt in prompts:
                response = await self.llm_manager.generate_text(f"{self.system_prompt}\n\n{result}\n\n{prompt}")
                result += f"\n{response}"
            return result.strip()
        except Exception as e:
            logging.error(f"Error in _chain_prompts: {str(e)}")
            raise

    async def generate_human_message(self, content: Any) -> str:
        try:
            prompts = [
                f"Convert the following content into a human-friendly message: {content}",
                "Ensure the message is clear, concise, and easy to understand.",
                "If the content contains technical terms, provide brief explanations."
            ]
            return await self._chain_prompts(prompts)
        except Exception as e:
            logging.error(f"Error generating human message: {str(e)}")
            raise

    async def interpret_human_message(self, content: str) -> Any:
        try:
            prompts = [
                f"Interpret the following human message: {content}",
                "Convert the message into structured data suitable for an agent.",
                "Identify key entities, intents, and any specific actions requested.",
                "Return the result as a JSON object."
            ]
            result = await self._chain_prompts(prompts)
            return json.loads(result)
        except Exception as e:
            logging.error(f"Error interpreting human message: {str(e)}")
            raise

    async def determine_agent_state_update(self, agent: 'Agent', message: 'ACLMessage') -> dict[str, Any]:
        try:
            prompts = [
                f"Given the agent's current state: {json.dumps(agent.state)}",
                f"And the received message: {message.content}",
                "Determine how to update the agent's state based on this information.",
                "Consider the agent's current beliefs, desires, and intentions.",
                "Identify any new information that should be added to the agent's knowledge base.",
                "Suggest any changes to the agent's goals or plans.",
                "Return a JSON object with the proposed updates to the agent's state."
            ]
            result = await self._chain_prompts(prompts)
            return json.loads(result)
        except Exception as e:
            logging.error(f"Error determining agent state update: {str(e)}")
            raise

    async def generate_agent_response(self, agent: 'Agent', human_message: str) -> str:
        try:
            prompts = [
                f"Given the agent's current state: {json.dumps(agent.state)}",
                f"And the human message: {human_message}",
                "Generate an appropriate response for the agent.",
                "Ensure the response aligns with the agent's goals and knowledge.",
                "The response should be clear, helpful, and relevant to the human's query or request."
            ]
            return await self._chain_prompts(prompts)
        except Exception as e:
            logging.error(f"Error generating agent response: {str(e)}")
            raise
