import json
from typing import Any, Dict, List

from app.models.agent import Agent
from app.models.message import ACLMessage

class LLMService:
    def __init__(self, llm_model):
        self.llm_model = llm_model
        self.system_prompt = self._generate_system_prompt() # This could be an instance of an LLM API client

    def _generate_system_prompt(self) -> str:
        return """
        You are an AI assistant integrated into a Multi-Agent System for business operations.
        Your role is to assist in interpreting human messages, generating responses, and updating agent states.
        Please provide concise, accurate, and relevant information based on the given context.
        """

    async def _chain_prompts(self, prompts: List[str]) -> str:
        result = ""
        for prompt in prompts:
            response = await self.llm_model.generate(f"{self.system_prompt}\n\n{result}\n\n{prompt}")
            result += f"\n{response.text}"
        return result.strip()

    async def generate_human_message(self, content: Any) -> str:
        prompts = [
            f"Convert the following content into a human-friendly message: {content}",
            "Ensure the message is clear, concise, and easy to understand.",
            "If the content contains technical terms, provide brief explanations."
        ]
        return await self._chain_prompts(prompts)

    async def interpret_human_message(self, content: str) -> Any:
        prompts = [
            f"Interpret the following human message: {content}",
            "Convert the message into structured data suitable for an agent.",
            "Identify key entities, intents, and any specific actions requested.",
            "Return the result as a JSON object."
        ]
        result = await self._chain_prompts(prompts)
        return json.loads(result)

    async def determine_agent_state_update(self, agent: 'Agent', message: ACLMessage) -> Dict[str, Any]:
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

    async def generate_agent_response(self, agent: 'Agent', human_message: str) -> str:
        prompts = [
            f"Given the agent's current state: {json.dumps(agent.state)}",
            f"And the human message: {human_message}",
            "Generate an appropriate response for the agent.",
            "Ensure the response aligns with the agent's goals and knowledge.",
            "The response should be clear, helpful, and relevant to the human's query or request."
        ]
        return await self._chain_prompts(prompts)