from typing import Dict, Any, List
from uuid import UUID
from app.core.models.agent.agent import Agent
from app.core.models.message import ACLMessage, Performative
from app.core.services.agent_service import AgentService
from app.core.services.knowledge_base_service import KnowledgeBaseService

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
        if receiver := self.agent_service.get_agent(message.receiver_id):
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
        # Extract the request from the message content
        request = message.content

        # Check if the receiver agent can handle the request
        if receiver.can_handle_request(request):
            # Execute the requested action or task
            response = await receiver.execute_request(request)

            # Send the response back to the sender
            await self.send_message(
                receiver.id,
                message.sender_id,
                Performative.INFORM,
                response
            )
        else:
            # If the receiver cannot handle the request, send a failure response
            await self.send_message(
                receiver.id,
                message.sender_id,
                Performative.FAILURE,
                f"Agent {receiver.id} cannot handle the request: {request}"
            )

    async def _handle_inform(self, receiver: 'Agent', message: ACLMessage):
        # Extract the information from the message content
        information = message.content

        # Process the received information
        await receiver.process_information(information)

        # Optionally, send an acknowledgement back to the sender
        await self.send_message(
            receiver.id,
            message.sender_id,
            Performative.CONFIRM,
            f"Information received and processed by {receiver.id}"
        )

    async def _handle_query(self, receiver: 'Agent', message: ACLMessage):
        # Extract the query from the message content
        query = message.content

        # Check if the receiver agent can handle the query
        if receiver.can_handle_query(query):
            # Execute the query and get the result
            result = await receiver.execute_query(query)

            # Send the query result back to the sender
            await self.send_message(
                receiver.id,
                message.sender_id,
                Performative.INFORM,
                result
            )
        else:
            # If the receiver cannot handle the query, send a failure response
            await self.send_message(
                receiver.id,
                message.sender_id,
                Performative.FAILURE,
                f"Agent {receiver.id} cannot handle the query: {query}"
            )

    async def _handle_proposal(self, receiver: 'Agent', message: ACLMessage):
        # Extract the proposal from the message content
        proposal = message.content

        # Check if the receiver agent can handle the proposal
        if receiver.can_handle_proposal(proposal):
            # Evaluate the proposal and make a decision
            decision = await receiver.evaluate_proposal(proposal)

            if decision.accepted:
                # If the proposal is accepted, send an accept-proposal message back to the sender
                await self.send_message(
                    receiver.id,
                    message.sender_id,
                    Performative.ACCEPT_PROPOSAL,
                    decision.content
                )
            else:
                # If the proposal is rejected, send a reject-proposal message back to the sender
                await self.send_message(
                    receiver.id,
                    message.sender_id,
                    Performative.REJECT_PROPOSAL,
                    decision.content
                )
        else:
            # If the receiver cannot handle the proposal, send a failure response
            await self.send_message(
                receiver.id,
                message.sender_id,
                Performative.FAILURE,
                f"Agent {receiver.id} cannot handle the proposal: {proposal}"
            )
