from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.agents.base.agent_base import AgentBase
    from app.models.agent.action import Action
    from app.models.agent.agent import Agent
    from app.models.agent.agent_role import AgentRole
    from app.models.agent.belief import Belief
    from app.models.agent.desire import Desire
    from app.models.agent.goal import Goal
    from app.models.agent.intention import Intention
    from app.models.agent.plan import Plan

def update_forward_refs():
    from app.agents.base.agent_base import AgentBase
    from app.models.agent.action import Action
    from app.models.agent.agent import Agent
    from app.models.agent.agent_role import AgentRole
    from app.models.agent.belief import Belief
    from app.models.agent.desire import Desire
    from app.models.agent.goal import Goal
    from app.models.agent.intention import Intention
    from app.models.agent.plan import Plan

    AgentBase.update_forward_refs(Belief=Belief, Desire=Desire, Intention=Intention, Goal=Goal, Plan=Plan, Action=Action)
    Agent.update_forward_refs(AgentRole=AgentRole)
    Belief.update_forward_refs(Agent=Agent)
    Desire.update_forward_refs(Agent=Agent)
    Intention.update_forward_refs(Agent=Agent, Goal=Goal)
    Goal.update_forward_refs(Agent=Agent, Belief=Belief)
    Plan.update_forward_refs(Agent=Agent, Goal=Goal)
    Action.update_forward_refs(Agent=Agent)
    AgentRole.update_forward_refs(Agent=Agent)