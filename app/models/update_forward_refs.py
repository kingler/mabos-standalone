from .agent_base import AgentBase
from .belief import Belief
from .desire import Desire
from .intention import Intention
from .goal import Goal
from .plan import Plan
from .action import Action
from .agent import Agent
from .agent_role import AgentRole

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