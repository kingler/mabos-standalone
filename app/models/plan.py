from pydantic import BaseModel, ConfigDict
from typing import List, Dict

class PlanStep(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    description: str
    is_completed: bool = False

class Plan(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: str
    goal_id: str
    steps: List[PlanStep]
    symbolic_plan: Dict
    llm_plan: Dict
    is_completed: bool = False

    def add_step(self, step: PlanStep):
        self.steps.append(step)

    def update_step_status(self, step_id: str, is_completed: bool):
        for step in self.steps:
            if step.id == step_id:
                step.is_completed = is_completed
                break

    def check_completion(self):
        self.is_completed = all(step.is_completed for step in self.steps)

    def get_next_step(self):
        return next((step for step in self.steps if not step.is_completed), None)
