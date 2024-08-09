from typing import Dict, Any
from uuid import UUID
from app.core.services.agent_service import AgentService
from app.core.models.agent import ReactiveAgent

class ReactiveService:
    def __init__(self, agent_service: AgentService):
        self.agent_service = agent_service

    def handle_event(self, agent_id: UUID, event: Dict[str, Any]) -> Dict[str, Any]:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, ReactiveAgent):
            response = agent.handle_event(event)
            # Here you might want to add logic to execute the action
            # or update the agent's state based on the response
            return response
        return None

    def add_reaction_rule(self, agent_id: UUID, event_type: str, action: str) -> ReactiveAgent:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, ReactiveAgent):
            agent.reaction_rules[event_type] = action
            return agent
        return None