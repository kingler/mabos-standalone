from typing import Dict, Any
from uuid import UUID
from app.services.agent_service import AgentService
from app.models.agent import EnvironmentalAgent

class EnvironmentService:
    def __init__(self, agent_service: AgentService):
        self.agent_service = agent_service

    def update_environment_state(self, agent_id: UUID, new_state: Dict[str, Any]) -> EnvironmentalAgent:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, EnvironmentalAgent):
            agent.update_environment_state(new_state)
            # Notify other agents about the environment change
            self._notify_agents_of_change(new_state)
            return agent
        return None

    def _notify_agents_of_change(self, new_state: Dict[str, Any]):
        all_agents = self.agent_service.get_all_agents()
        for agent in all_agents:
            if not isinstance(agent, EnvironmentalAgent):
                # Update beliefs of non-environmental agents
                self.agent_service.update_agent_beliefs(agent.id, new_state)