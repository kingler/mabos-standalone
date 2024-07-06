from app.models.multiagent_system import MultiAgentSystem
from app.models.agent import Agent
from typing import List, Optional
from uuid import UUID

class MASService:
    def __init__(self, num_agents: int, num_states: int, state_size: int, action_size: int, ontology_path: str):
        self.mas = MultiAgentSystem(num_agents, num_states, state_size, action_size, ontology_path)

    def add_agent(self, agent: Agent) -> Agent:
        return self.mas.add_agent(agent)

    def get_agent(self, agent_id: UUID) -> Optional[Agent]:
        return self.mas.get_agent(agent_id)

    def remove_agent(self, agent_id: UUID) -> bool:
        return self.mas.remove_agent(agent_id)

    def list_agents(self) -> List[Agent]:
        return self.mas.list_agents()

    def send_message(self, sender_id: UUID, receiver_id: UUID, content: str):
        self.mas.send_message(sender_id, receiver_id, content)

    def step(self):
        self.mas.step()

    def run(self, steps: int):
        self.mas.run(steps)