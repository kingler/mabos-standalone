from typing import Any, Dict, List
from pydantic import Field, SkipValidation
from app.core.models.agent import Agent
from app.core.models.message import ACLMessage, Performative
from app.core.models.agent.goal import Goal
from app.core.services.llm_service import LLMService
from app.core.services.agent_communication_service import AgentCommunicationService
from app.core.models.llm_decomposer import LLMDecomposer
import openai

class LLMAgent(Agent):
    agent_id: str
    name: str
    api_key: str
    llm_service: LLMService = Field(default_factory=SkipValidation)
    agent_communication_service: AgentCommunicationService = Field(default_factory=SkipValidation)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, agent_id: str, name: str, api_key: str, llm_service: LLMService, agent_communication_service: AgentCommunicationService):
        super().__init__(agent_id=agent_id, name=name, api_key=api_key, llm_service=llm_service, agent_communication_service=agent_communication_service)
        self.llm_decomposer = LLMDecomposer(api_key)
        openai.api_key = self.api_key

    async def process_message(self, message: ACLMessage):
        """Process incoming messages using LLM capabilities."""
        if message.performative == Performative.REQUEST:
            response = await self.handle_request(message.content)
        elif message.performative == Performative.INFORM:
            response = await self.process_information(message.content)
        elif message.performative == Performative.QUERY:
            response = await self.handle_query(message.content)
        else:
            response = "Unsupported message performative"

        await self.agent_communication_service.send_message(
            self.agent_id,
            message.sender_id,
            Performative.INFORM,
            response
        )

    async def handle_request(self, request: str) -> str:
        """Handle requests using LLM capabilities."""
        prompt = f"Given the following request: '{request}', how should I respond or act?"
        return await self.llm_service.generate_agent_response(self, prompt)

    async def process_information(self, information: str) -> str:
        """Process information using LLM capabilities."""
        prompt = f"Given the following information: '{information}', what are the key points or actions to take?"
        return await self.llm_service.generate_agent_response(self, prompt)

    async def handle_query(self, query: str) -> str:
        """Handle queries using LLM capabilities."""
        prompt = f"Given the following query: '{query}', what is the appropriate response?"
        return await self.llm_service.generate_agent_response(self, prompt)

    async def decompose_goal(self, goal: Goal) -> List[Goal]:
        """Decompose a high-level goal into subgoals using LLM capabilities."""
        return self.llm_decomposer.decompose_with_validation(goal)

    async def generate_human_message(self, content: Any) -> str:
        """Generate a human-friendly message from structured content."""
        return await self.llm_service.generate_human_message(content)

    async def interpret_human_message(self, content: str) -> Any:
        """Interpret a human message into structured data."""
        return await self.llm_service.interpret_human_message(content)

    async def function_call(self, function_name: str, parameters: Dict[str, Any]) -> Any:
        """Make a function call using LLM capabilities."""
        prompt = f"Execute the following function: {function_name} with parameters: {parameters}"
        return await self.llm_service.generate_agent_response(self, prompt)

    async def ask_question(self, question: str) -> str:
        """Ask a question and get a response using LLM capabilities."""
        prompt = f"Please answer the following question: {question}"
        return await self.llm_service.generate_agent_response(self, prompt)

    async def update_state(self, message: ACLMessage):
        """Update agent state based on received message."""
        state_update = await self.llm_service.determine_agent_state_update(self, message)
        for key, value in state_update.items():
            setattr(self, key, value)

    async def generate_response(self, human_message: str) -> str:
        """Generate a response to a human message."""
        return await self.llm_service.generate_agent_response(self, human_message)