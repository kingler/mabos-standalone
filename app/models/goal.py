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

    def decompose(self, llm_decomposer):
        self.subgoals = llm_decomposer.decompose(self)
        self.validate_subgoals()

    def validate_subgoals(self):
        # Placeholder for subgoal validation logic
        pass

    def update_status(self, is_achieved: bool):
        self.is_achieved = is_achieved

    def add_metadata(self, key: str, value: any):
        self.metadata[key] = value