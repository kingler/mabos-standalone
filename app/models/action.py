from typing import Dict, Any, Callable
from pydantic import BaseModel, Field

class Action(BaseModel):
    """
    Represents an action that an agent can perform.

    Attributes:
        action_id (str): The unique identifier of the action.
        description (str): A description of the action.
        preconditions (Dict[str, Any]): Conditions that must be met before the action can be executed.
        effects (Dict[str, Any]): The expected outcomes of the action.
    """
    action_id: str = Field(..., description="The unique identifier of the action")
    description: str = Field(..., description="A description of the action")
    preconditions: Dict[str, Any] = Field(default_factory=dict, description="Conditions that must be met before the action can be executed")
    effects: Dict[str, Any] = Field(default_factory=dict, description="The expected outcomes of the action")
    
    def execute(self, get_belief: Callable[[str], Any], set_belief: Callable[[str, Any], None]) -> bool:
        """
        Executes the action by updating the agent's beliefs based on the action's effects.

        Args:
            get_belief (Callable[[str], Any]): A function to retrieve the current value of a belief.
            set_belief (Callable[[str, Any], None]): A function to update the value of a belief.

        Returns:
            bool: True if the action was executed successfully, False otherwise.
        """
        if not self.is_applicable(get_belief):
            return False    
        for effect_key, effect_value in self.effects.items():
            set_belief(effect_key, effect_value)
        return True

    def is_applicable(self, get_belief: Callable[[str], Any]) -> bool:
        """
        Checks if the action is applicable based on the current beliefs of the agent.

        Args:
            get_belief (Callable[[str], Any]): A function to retrieve the current value of a belief.

        Returns:
            bool: True if all preconditions are satisfied, False otherwise.
        """
        return all(
            get_belief(precondition_key) == precondition_value
            for precondition_key, precondition_value in self.preconditions.items()
        )

    def is_completed(self, get_belief: Callable[[str], Any]) -> bool:
        """
        Checks if the action has been completed based on the current beliefs of the agent.

        Args:
            get_belief (Callable[[str], Any]): A function to retrieve the current value of a belief.

        Returns:
            bool: True if all effects have been achieved, False otherwise.
        """
        return all(get_belief(effect_key) == effect_value
                   for effect_key, effect_value in self.effects.items())

Action.model_rebuild()