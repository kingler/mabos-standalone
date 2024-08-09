from app.core.agents.base.agent_base import AgentBase
from app.core.models.agent.belief import Belief
from app.core.models.agent.desire import Desire
from app.core.models.agent.intention import Intention
from app.core.models.agent.goal import Goal
from app.core.models.agent.plan import Plan
from app.core.models.agent.action import Action
from app.core.models.agent.agent import Agent
from app.core.models.agent.agent_role import AgentRole

def update_forward_refs():
    AgentBase.update_forward_refs(Agent=Agent, Belief=Belief, Desire=Desire, Intention=Intention, Goal=Goal, Plan=Plan, Action=Action)
    Belief.update_forward_refs(AgentBase=AgentBase)
    Desire.update_forward_refs(AgentBase=AgentBase)
    Intention.update_forward_refs(AgentBase=AgentBase, Goal=Goal)
    Goal.update_forward_refs(AgentBase=AgentBase)
    Plan.update_forward_refs(AgentBase=AgentBase, Goal=Goal)
    Action.update_forward_refs(AgentBase=AgentBase)
    Agent.update_forward_refs(AgentRole=AgentRole)
    AgentRole.update_forward_refs(Agent=Agent)