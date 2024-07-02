from typing import Dict, List, Optional
from uuid import UUID, uuid4
from app.models.agent import Agent
from app.services.agent_service import AgentService
from app.models.message import Message

class MultiAgentSystem:
    def __init__(self):
        self.agents: Dict[UUID, Agent] = {}
        self.agent_service = AgentService()
        self.message_queue: List[Message] = []

    def add_agent(self, agent: Agent) -> Agent:
        agent_id = uuid4()
        agent.agent_id = str(agent_id)
        self.agents[agent_id] = agent
        return agent

    def get_agent(self, agent_id: UUID) -> Optional[Agent]:
        return self.agents.get(agent_id)

    def remove_agent(self, agent_id: UUID) -> bool:
        if agent_id in self.agents:
            del self.agents[agent_id]
            return True
        return False

    def list_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def send_message(self, sender_id: UUID, receiver_id: UUID, content: str):
        message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
        self.message_queue.append(message)

    def process_messages(self):
        for message in self.message_queue:
            receiver = self.agents.get(message.receiver_id)
            if receiver:
                receiver.receive_message(message)
        self.message_queue.clear()

    def step(self):
        for agent in self.agents.values():
            agent.perceive()
            agent.deliberate()
            agent.plan()
            agent.execute()
        self.process_messages()

    def run(self, steps: int):
        for _ in range(steps):
            self.step()