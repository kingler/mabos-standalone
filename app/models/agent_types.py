"""
This module provides different types of agents.

Agents:
    - Agent: Base class for all agents.
    - EnvironmentalAgent: An agent that interacts with the environment.
    - ProactiveAgent: An agent that proactively pursues its goals.
    - ReactiveAgent: An agent that reacts to changes in the environment.
"""

from .agent import Agent
from .environmental_agent import EnvironmentalAgent
from .proactive_agent import ProactiveAgent
from .reactive_agent import ReactiveAgent

__all__ = ['Agent', 'EnvironmentalAgent', 'ProactiveAgent', 'ReactiveAgent']