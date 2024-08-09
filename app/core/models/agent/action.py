from typing import Dict, Any, Callable, List
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, JSON
from db.database import Base

class Action(BaseModel):
    """
    Represents an action that an agent can perform.

    Attributes:
        id (str): The unique identifier of the action.
        description (str): A description of the action.
        preconditions (Dict[str, Any]): Conditions that must be met before the action can be executed.
        effects (Dict[str, Any]): The expected outcomes of the action.
        required_capabilities (List[str]): The capabilities required to execute this action.
    """
    id: str = Field(..., description="The unique identifier of the action")
    description: str = Field(..., description="A description of the action")
    preconditions: Dict[str, Any] = Field(default_factory=dict, description="Conditions that must be met before the action can be executed")
    effects: Dict[str, Any] = Field(default_factory=dict, description="The expected outcomes of the action")
    required_capabilities: List[str] = Field(default_factory=list, description="The capabilities required to execute this action")
    
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

class ActionDB(Base):
    __tablename__ = "actions"

    id = Column(String, primary_key=True, index=True)
    description = Column(String)
    preconditions = Column(JSON)
    effects = Column(JSON)
    required_capabilities = Column(JSON)

    @classmethod
    def from_pydantic(cls, action: Action) -> "ActionDB":
        return cls(
            id=action.id,
            description=action.description,
            preconditions=action.preconditions,
            effects=action.effects,
            required_capabilities=action.required_capabilities
        )

    def to_pydantic(self) -> Action:
        return Action(
            id=self.id,
            description=self.description,
            preconditions=self.preconditions,
            effects=self.effects,
            required_capabilities=self.required_capabilities
        )

Action.model_rebuild()