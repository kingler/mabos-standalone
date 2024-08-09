from typing import Dict, Any, Callable, List, Optional
from pydantic import BaseModel, Field
from sqlalchemy import Column, String, JSON
from app.db.database import Base

class Action(BaseModel):
    id: str = Field(..., description="The unique identifier of the action")
    description: str = Field(..., description="A description of the action")
    preconditions: Dict[str, Any] = Field(default_factory=dict, description="Conditions that must be met before the action can be executed")
    effects: Dict[str, Any] = Field(default_factory=dict, description="The expected outcomes of the action")
    required_capabilities: List[str] = Field(default_factory=list, description="The capabilities required to execute this action")
    
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

class ActionDB(Base):
    __tablename__ = "actions"

    id = Column(String, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
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