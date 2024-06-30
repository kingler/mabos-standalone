from typing import Dict, Any, List
from uuid import UUID
from app.models.agent import Agent
from app.models.message import ACLMessage, Performative
from app.services.agent_service import AgentService
from app.services.knowledge_base_service import KnowledgeBaseService

class AgentCommunicationService:
    def __init__(self, agent_service: AgentService, knowledge_base_service: KnowledgeBaseService):
        self.agent_service = agent_service
        self.knowledge_base_service = knowledge_base_service
        self.subscribed_topics: Dict[str, List[UUID]] = {}

    async def send_message(self, sender_id: UUID, receiver_id: UUID, performative: Performative, content: Any):
        sender = self.agent_service.get_agent(sender_id)
        receiver = self.agent_service.get_agent(receiver_id)
        if not sender or not receiver:
            raise ValueError("Sender or receiver not found")
        
        message = ACLMessage(
            sender_id=sender_id,
            receiver_id=receiver_id,
            performative=performative,
            content=content
        )
        await self._deliver_message(message)

    async def _deliver_message(self, message: ACLMessage):
        receiver = self.agent_service.get_agent(message.receiver_id)
        if receiver:
            await self._process_message(receiver, message)

    async def _process_message(self, receiver: 'Agent', message: ACLMessage):
        # Update the agent's beliefs based on the message
        await self.knowledge_base_service.update_beliefs(receiver.id, message.content)

        # Handle the message based on its performative
        if message.performative == Performative.REQUEST:
            await self._handle_request(receiver, message)
        elif message.performative == Performative.INFORM:
            await self._handle_inform(receiver, message)
        elif message.performative == Performative.QUERY:
            await self._handle_query(receiver, message)
        elif message.performative == Performative.PROPOSE:
            await self._handle_proposal(receiver, message)
        # Add more handlers for other performatives

    async def broadcast_message(self, sender_id: UUID, performative: Performative, content: Any):
        sender = self.agent_service.get_agent(sender_id)
        if not sender:
            raise ValueError("Sender not found")

        all_agents = self.agent_service.get_all_agents()
        for receiver in all_agents:
            if receiver.id != sender_id:
                await self.send_message(sender_id, receiver.id, performative, content)

    async def publish_message(self, sender_id: UUID, topic: str, performative: Performative, content: Any):
        if topic in self.subscribed_topics:
            for receiver_id in self.subscribed_topics[topic]:
                await self.send_message(sender_id, receiver_id, performative, content)

    def subscribe_to_topic(self, agent_id: UUID, topic: str):
        if topic not in self.subscribed_topics:
            self.subscribed_topics[topic] = []
        if agent_id not in self.subscribed_topics[topic]:
            self.subscribed_topics[topic].append(agent_id)

    def unsubscribe_from_topic(self, agent_id: UUID, topic: str):
        if topic in self.subscribed_topics and agent_id in self.subscribed_topics[topic]:
            self.subscribed_topics[topic].remove(agent_id)

    # Implement handlers for different performatives
    async def _handle_request(self, receiver: 'Agent', message: ACLMessage):
        # Handle request messages
        pass

    async def _handle_inform(self, receiver: 'Agent', message: ACLMessage):
        # Handle inform messages
        pass

    async def _handle_query(self, receiver: 'Agent', message: ACLMessage):
        # Handle query messages
        pass

    async def _handle_proposal(self, receiver: 'Agent', message: ACLMessage):
        # Handle proposal messages
        pass