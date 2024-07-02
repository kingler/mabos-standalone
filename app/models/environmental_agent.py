from typing import Dict, Any
from pydantic import Field
from .agent import Agent

class EnvironmentalAgent(Agent):
    environment_state: Dict[str, Any] = Field(default_factory=dict, description="The current state of the environment")

    def update_environment_state(self, new_state: Dict[str, Any]):
        """Update the agent's perception of the environment state."""
        self.environment_state.update(new_state)

    def perceive(self):
        """Perceive the environment and update beliefs."""
        for key, value in self.environment_state.items():
            self.add_belief(f"{key}: {value}")

    def act(self):
        """Perform actions based on the current environment state."""
        # This method can be overridden with specific environmental actions
        pass