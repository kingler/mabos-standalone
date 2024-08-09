from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.core.agents.base.agent_base import AgentBase
    from app.core.models.agent.agent import Agent
    from app.core.models.agent.belief import Belief
    from app.core.models.agent.desire import Desire
    from app.core.models.agent.intention import Intention
    from app.core.models.agent.goal import Goal
    from app.core.models.agent.plan import Plan
    from app.core.models.agent.action import Action
    from app.core.models.agent.agent_role import AgentRole

def update_forward_refs():
    from app.core.agents.base.agent_base import AgentBase
    from app.core.models.agent.agent import Agent
    from app.core.models.agent.belief import Belief
    from app.core.models.agent.desire import Desire
    from app.core.models.agent.intention import Intention
    from app.core.models.agent.goal import Goal
    from app.core.models.agent.plan import Plan
    from app.core.models.agent.action import Action
    from app.core.models.agent.agent_role import AgentRole

    AgentBase.update_forward_refs(Belief=Belief, Desire=Desire, Intention=Intention, Goal=Goal, Plan=Plan, Action=Action)
    Agent.update_forward_refs(AgentRole=AgentRole)
    Belief.update_forward_refs(Agent=Agent)
    Desire.update_forward_refs(Agent=Agent)
    Intention.update_forward_refs(Agent=Agent, Goal=Goal)
    Goal.update_forward_refs(Agent=Agent, Belief=Belief)
    Plan.update_forward_refs(Agent=Agent, Goal=Goal)
    Action.update_forward_refs(Agent=Agent)
    AgentRole.update_forward_refs(Agent=Agent)