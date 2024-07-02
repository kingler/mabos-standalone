from typing import Dict, Any
from uuid import UUID
from app.services.agent_service import AgentService
from app.models.agent import ProactiveAgent

class StrategyService:
    def __init__(self, agent_service: AgentService):
        self.agent_service = agent_service

    def propose_strategy(self, agent_id: UUID, strategy: Dict[str, Any]) -> Dict[str, Any]:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, ProactiveAgent):
            proposed_strategy = agent.propose_strategy(strategy)
            # Here you might want to add logic to evaluate the strategy
            # or share it with other agents for collaboration
            return proposed_strategy
        return None

    def add_long_term_goal(self, agent_id: UUID, goal: str) -> ProactiveAgent:
        agent = self.agent_service.get_agent(agent_id)
        if isinstance(agent, ProactiveAgent):
            agent.long_term_goals.append(goal)
            return agent
        return None