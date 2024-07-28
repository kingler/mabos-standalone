from .agent import Agent
from .belief import Belief
from .desire import Desire
from .intention import Intention
from .goal import Goal
from .plan import Plan
from .action import Action

def initialize_models():
    Agent.update_forward_refs()
    Belief.update_forward_refs()
    Desire.update_forward_refs()
    Intention.update_forward_refs()
    Goal.update_forward_refs()
    Plan.update_forward_refs()
    Action.update_forward_refs()