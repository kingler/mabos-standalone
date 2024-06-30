from typing import Any, Dict
from app.models.message import ACLMessage

class LLMService:
    def __init__(self, llm_model):
        self.llm_model = llm_model  # This could be an instance of an LLM API client

    async def generate_human_message(self, content: Any) -> str:
        # Use the LLM to generate a human-friendly message from the agent's content
        prompt = f"Convert the following content into a human-friendly message: {content}"
        response = await self.llm_model.generate(prompt)
        return response.text

    async def interpret_human_message(self, content: str) -> Any:
        # Use the LLM to interpret the human message and convert it into a format suitable for agents
        prompt = f"Interpret the following human message and convert it into structured data for an agent: {content}"
        response = await self.llm_model.generate(prompt)
        # Assume the LLM returns a JSON string that we can parse
        return json.loads(response.text)

    async def determine_agent_state_update(self, agent: 'Agent', message: ACLMessage) -> Dict[str, Any]:
        # Use the LLM to determine how to update the agent's state based on the human message
        prompt = f"Given the agent's current state: {agent.state}\n"
        prompt += f"And the received message: {message.content}\n"
        prompt += "Determine how to update the agent's state. Return a JSON object with the updates."
        response = await self.llm_model.generate(prompt)
        # Assume the LLM returns a JSON string that we can parse
        return json.loads(response.text)