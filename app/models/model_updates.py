from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.agent_base import AgentBase
    from .agent import Agent
    from .belief import Belief
    from .desire import Desire
    from .intention import Intention
    from .goal import Goal
    from .plan import Plan
    from .action import Action
    from app.models.agent_role import AgentRole

def update_forward_refs():
    from app.models.agent_base import AgentBase
    from .agent import Agent
    from .belief import Belief
    from .desire import Desire
    from .intention import Intention
    from .goal import Goal
    from .plan import Plan
    from .action import Action
    from app.models.agent_role import AgentRole

    AgentBase.update_forward_refs(Belief=Belief, Desire=Desire, Intention=Intention, Goal=Goal, Plan=Plan, Action=Action)
    Agent.update_forward_refs(AgentRole=AgentRole)
    Belief.update_forward_refs(Agent=Agent)
    Desire.update_forward_refs(Agent=Agent)
    Intention.update_forward_refs(Agent=Agent, Goal=Goal)
    Goal.update_forward_refs(Agent=Agent, Belief=Belief)
    Plan.update_forward_refs(Agent=Agent, Goal=Goal)
    Action.update_forward_refs(Agent=Agent)
    AgentRole.update_forward_refs(Agent=Agent)