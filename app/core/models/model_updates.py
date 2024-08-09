from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.agents.base.agent_base import AgentBase
    from core.models.agent.agent import Agent
    from core.models.agent.belief import Belief
    from core.models.agent.desire import Desire
    from core.models.agent.intention import Intention
    from core.models.agent.goal import Goal
    from core.models.agent.plan import Plan
    from core.models.agent.action import Action
    from core.models.agent.agent_role import AgentRole

def update_forward_refs():
    from core.agents.base.agent_base import AgentBase
    from .agent import Agent
    from core.models.agent.belief import Belief
    from core.models.agent.desire import Desire
    from core.models.agent.intention import Intention
    from core.models.agent.goal import Goal
    from core.models.agent.plan import Plan
    from core.models.agent.action import Action
    from core.models.agent.agent_role import AgentRole

    AgentBase.update_forward_refs(Belief=Belief, Desire=Desire, Intention=Intention, Goal=Goal, Plan=Plan, Action=Action)
    Agent.update_forward_refs(AgentRole=AgentRole)
    Belief.update_forward_refs(Agent=Agent)
    Desire.update_forward_refs(Agent=Agent)
    Intention.update_forward_refs(Agent=Agent, Goal=Goal)
    Goal.update_forward_refs(Agent=Agent, Belief=Belief)
    Plan.update_forward_refs(Agent=Agent, Goal=Goal)
    Action.update_forward_refs(Agent=Agent)
    AgentRole.update_forward_refs(Agent=Agent)