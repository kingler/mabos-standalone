from core.models.agent.action import Action
from core.models.agent.agent import Agent
from core.models.agent.belief import Belief
from core.models.agent.desire import Desire
from core.models.agent.goal import Goal
from core.models.agent.intention import Intention
from core.models.agent.plan import Plan


def initialize_models():
    Agent.update_forward_refs()
    Belief.update_forward_refs()
    Desire.update_forward_refs()
    Intention.update_forward_refs()
    Goal.update_forward_refs()
    Plan.update_forward_refs()
    Action.update_forward_refs()