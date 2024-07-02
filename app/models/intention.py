from typing import List, Any, Optional
from pydantic import BaseModel, Field
from .belief import Belief
from .plan import Plan
from .goal import Goal


class Intention(BaseModel):
    status: str = "pending"
    goal: Goal
    plan: Plan
    

    class Config:
        from_attributes = True

    def activate_intention(self):
        self.status = "active"

    def suspend_intention(self):
        self.status = "suspended"

    def complete_intention(self):
        self.status = "completed"

    def is_achievable(self, current_beliefs: List[Belief]) -> bool:
        return any(belief.description == self.goal.description and belief.certainty >= 0.8 for belief in current_beliefs)

    def execute_intention(self, execute_action):
        self.status = "completed" if execute_action() else "failed"

    def update_status(self, new_status: str):
        self.status = new_status

    def revise_intention(self, new_goal: Any):
        self.goal = new_goal
        self.status = "revised"

Intention.model_rebuild()
