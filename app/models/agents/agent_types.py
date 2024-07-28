"""
This module provides different types of agents.

Agents:
    - Agent: Base class for all agents.
    - EnvironmentalAgent: An agent that interacts with the environment.
    - ProactiveAgent: An agent that proactively pursues its goals.
    - ReactiveAgent: An agent that reacts to changes in the environment.
"""

from ..agent import Agent, EnvironmentalAgent, ProactiveAgent, ReactiveAgent
from ..agent_role import AgentRole

# The base Agent class and its subclasses are already defined in agent.py,
# so we don't need to redefine them here. We can extend them if needed:

class CustomEnvironmentalAgent(EnvironmentalAgent):
    """
    A custom environmental agent with additional functionality.
    """
    def custom_environmental_method(self):
        print("Custom environmental method")

class CustomProactiveAgent(ProactiveAgent):
    """
    A custom proactive agent with additional functionality.
    """
    def custom_proactive_method(self):
        print("Custom proactive method")

class CustomReactiveAgent(ReactiveAgent):
    """
    A custom reactive agent with additional functionality.
    """
    def custom_reactive_method(self):
        print("Custom reactive method")

# If you need to add more agent types or extend existing ones, do it here.