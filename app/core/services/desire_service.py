from typing import Optional

from app.core.models.agent.agent import Agent
from app.core.models.agent.desire import Desire
from app.core.services.agent_service import AgentService


class DesireService:
    def __init__(self, agent_service: AgentService):
        self.agent_service = agent_service

    def create_desire(self, agent_id: str, desire_data: dict) -> Optional[Desire]:
        if agent := self.agent_service.get_agent(agent_id):
            desire = Desire(**desire_data)
            agent.add_desire(desire)
            return desire
        return None

    def get_desire(self, agent_id: str, desire_id: str) -> Optional[Desire]:
        if agent := self.agent_service.get_agent(agent_id):
            return agent.get_desire(desire_id)
        return None

    def update_desire(self, agent_id: str, desire_id: str, new_data: dict) -> Optional[Desire]:
        if agent := self.agent_service.get_agent(agent_id):
            if desire := agent.get_desire(desire_id):
                desire.update_desire(**new_data)
                return desire
        return None

    def delete_desire(self, agent_id: str, desire_id: str) -> bool:
        if agent := self.agent_service.get_agent(agent_id):
            return agent.remove_desire(desire_id)
        return False

    def generate_desires(self, agent_id: str) -> Optional[Agent]:
        if agent := self.agent_service.get_agent(agent_id):
            self.agent_service._update_desires(agent)
            return agent
        return None
