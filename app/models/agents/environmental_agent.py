from typing import Dict, Any
from pydantic import Field
from ..agent import Agent
from ..belief import Belief

class EnvironmentalAgent(Agent):
    """
    An agent that interacts with and perceives the environment.

    Attributes:
        environment_state (Dict[str, Any]): The current state of the environment.
    """
    environment_state: Dict[str, Any] = Field(default_factory=dict, description="The current state of the environment")

    def update_environment_state(self, new_state: Dict[str, Any]):
        """
        Update the agent's perception of the environment state.

        Args:
            new_state (Dict[str, Any]): The new state of the environment.
        """
        self.environment_state.update(new_state)

    def perceive(self):
        """
        Perceive the environment and update beliefs.
        """
        for key, value in self.environment_state.items():
            belief_description = f"{key}"
            existing_belief = next((b for b in self.beliefs if b.description == belief_description), None)
            if existing_belief:
                existing_belief.update_value(value)
                existing_belief.update_certainty(1.0)
            else:
                self.add_belief(Belief(description=belief_description, certainty=1.0, value=value))

    def act(self):
        """
        Perform actions based on the current environment state.
        """
        # Deliberate on desires and create intentions
        self.deliberate()

        # Plan actions for active intentions
        self.plan()

        # Execute planned actions
        for intention in self.intentions:
            if intention.status == "active":
                for step in intention.plan.steps:
                    if step.status == "pending":
                        step.action.execute(self)
                        step.status = "completed"
                        break
                else:
                    intention.status = "completed"
