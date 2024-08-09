from typing import Dict, List, Any
from uuid import UUID
from app.core.models.message import ACLMessage, Performative
from app.core.models.agent import Agent
from app.core.models.message import Message
from app.core.services.agent_service import AgentService
from app.core.services.llm_service import LLMService

class HumanCommunicationService:
    def __init__(self, agent_service: AgentService, llm_service: LLMService):
        self.agent_service = agent_service
        self.llm_service = llm_service
        self.human_messages: Dict[UUID, List[ACLMessage]] = {}

    async def send_message_to_human(self, agent_id: UUID, human_id: UUID, content: Any):
        agent = self.agent_service.get_agent(agent_id)
        if not agent:
            raise ValueError("Agent not found")

        # Use LLM to generate a human-friendly message
        human_friendly_content = await self.llm_service.generate_human_message(content)

        message = ACLMessage(
            sender_id=agent_id,
            receiver_id=human_id,
            performative=Performative.INFORM,
            content=human_friendly_content
        )

        if human_id not in self.human_messages:
            self.human_messages[human_id] = []
        self.human_messages[human_id].append(message)

    async def get_messages_for_human(self, human_id: UUID) -> List[ACLMessage]:
        return self.human_messages.get(human_id, [])

    async def send_message_to_agent(self, human_id: UUID, agent_id: UUID, content: str):
        agent = self.agent_service.get_agent(agent_id)
        if not agent:
            raise ValueError("Agent not found")

        # Use LLM to interpret the human message and generate appropriate ACL content
        interpreted_content = await self.llm_service.interpret_human_message(content)

        message = ACLMessage(
            sender_id=human_id,
            receiver_id=agent_id,
            performative=Performative.INFORM,  # Default to INFORM, but could be determined by LLM
            content=interpreted_content
        )

        await self._process_human_message(agent, message)

    async def _process_human_message(self, agent: 'Agent', message: ACLMessage):
        # Use LLM to determine how to update the agent's state based on the human message
        state_update = await self.llm_service.determine_agent_state_update(agent, message)
        
        # Apply the state update to the agent
        await self.agent_service.update_agent_state(agent.id, state_update)