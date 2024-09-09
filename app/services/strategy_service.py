from typing import Any, Dict
from uuid import UUID

from app.agents.core_agents.proactive_agent import ProactiveAgent
from app.services.agent_service import AgentService


class StrategyService:
    def __init__(self, agent_service: AgentService):
        self.agent_service = agent_service

    def propose_strategy(self, agent_id: UUID, strategy: Dict[str, Any]) -> Dict[str, Any]:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, ProactiveAgent):
            return agent.propose_strategy(strategy)
        return None

    def add_long_term_goal(self, agent_id: UUID, goal: str) -> ProactiveAgent:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, ProactiveAgent):
            agent.long_term_goals.append(goal)
            return agent
        return None