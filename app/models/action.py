from typing import Dict, Any, Callable
from pydantic import BaseModel, Field

class Action(BaseModel):
    action_id: str = Field(..., description="The unique identifier of the action")
    description: str = Field(..., description="A description of the action")
    preconditions: Dict[str, Any] = Field(default_factory=dict, description="Conditions that must be met before the action can be executed")
    effects: Dict[str, Any] = Field(default_factory=dict, description="The expected outcomes of the action")
    
    def execute(self, get_belief: Callable[[str], Any], set_belief: Callable[[str, Any], None]) -> bool:
        if not self.is_applicable(get_belief):
            return False    
        for effect_key, effect_value in self.effects.items():
            set_belief(effect_key, effect_value)
        return True

    def is_applicable(self, get_belief: Callable[[str], Any]) -> bool:
        return all(
            get_belief(precondition_key) == precondition_value
            for precondition_key, precondition_value in self.preconditions.items()
        )

    def is_completed(self, get_belief: Callable[[str], Any]) -> bool:
        return all(get_belief(effect_key) == effect_value
                   for effect_key, effect_value in self.effects.items())

Action.model_rebuild()