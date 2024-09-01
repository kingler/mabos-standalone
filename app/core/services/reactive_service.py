from typing import Any, Dict
from uuid import UUID

from app.core.agents.core_agents.reactive_agent import ReactiveAgent
from app.core.services.agent_service import AgentService


class ReactiveService:
    def __init__(self, agent_service: AgentService):
        self.agent_service = agent_service

    def handle_event(self, agent_id: UUID, event: Dict[str, Any]) -> Dict[str, Any]:
        agent = self.agent_service.get_agent(agent_id)
        return agent.handle_event(event) if isinstance(agent, ReactiveAgent) else None
        # Note: Logic to execute the action or update agent's state should be added here if needed

    def add_reaction_rule(self, agent_id: UUID, event_type: str, action: str) -> ReactiveAgent | None:
        agent = self.agent_service.get_agent(agent_id)
        return agent.reaction_rules.update({event_type: action}) if isinstance(agent, ReactiveAgent) else None