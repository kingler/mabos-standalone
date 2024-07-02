from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Dict

class Goal(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    description: str
    priority: int
    status: str
    subgoals: List[str] = []
    llm_generated_context: Optional[str] = None
    is_achieved: bool = False
    metadata: Dict[str, any] = {}
    parent_goal: Optional['Goal'] = None
    child_goals: List['Goal'] = []

    def decompose(self, llm_decomposer, sub_goals: List['Goal']):
        self.subgoals = llm_decomposer.decompose(self)
        self.child_goals.extend(sub_goals)
        self.validate_subgoals()
        for sub_goal in sub_goals:
            sub_goal.parent_goal = self

    def validate_subgoals(self):
        if not isinstance(self.subgoals, list):
            raise TypeError("Subgoals must be a list")
        
        for subgoal in self.subgoals:
            if not isinstance(subgoal, str):
                raise TypeError("Each subgoal must be a string")
            
            if len(subgoal.strip()) == 0:
                raise ValueError("Subgoals cannot be empty or whitespace")
        
        if len(self.subgoals) == 0:
            raise ValueError("Goal must have at least one subgoal")

    def update_status(self, is_achieved: bool):
        self.is_achieved = is_achieved

    def add_metadata(self, key: str, value: any):
        self.metadata[key] = value