from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Optional

class PlanStep(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    description: str
    is_completed: bool = False
    goal_id: Optional[str] = None

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
        if step.goal_id:
            self._link_step_to_goal(step)
            
    def _link_step_to_goal(self, step: PlanStep):
        from app.models.goal import Goal
        
        if step.goal_id:
            goal = Goal.get(id=step.goal_id)
            if goal:
                goal.plan_steps.append(step)
                goal.save()
            else:
                raise ValueError(f"Goal with ID {step.goal_id} not found")
            
    def update_step_status(self, step_id: str, is_completed: bool):
        for step in self.steps:
            if step.id == step_id:
                step.is_completed = is_completed
                break

    def check_completion(self):
        self.is_completed = all(step.is_completed for step in self.steps)

    def get_next_step(self):
        return next((step for step in self.steps if not step.is_completed), None)
