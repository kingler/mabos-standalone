from pydantic import BaseModel, Field
from typing import Dict, List
from .plan import Plan

class PlanLibrary(BaseModel):
    plans: Dict[str, List[Plan]] = Field(default_factory=dict)

    def add_plan(self, plan: Plan):
        if plan.goal_id not in self.plans:
            self.plans[plan.goal_id] = []
        self.plans[plan.goal_id].append(plan)

    def remove_plan(self, plan_id: str, goal_id: str):
        if goal_id in self.plans:
            self.plans[goal_id] = [plan for plan in self.plans[goal_id] if plan.id != plan_id]
            if not self.plans[goal_id]:
                del self.plans[goal_id]

    def get_plans_for_goal(self, goal_id: str) -> List[Plan]:
        return self.plans.get(goal_id, [])

    def select_plan(self, goal_id: str, current_state: List[str]) -> Plan:
        suitable_plans = [plan for plan in self.get_plans_for_goal(goal_id) if plan.check_preconditions(current_state)]
        if not suitable_plans:
            raise ValueError(f"No suitable plan found for the goal: {goal_id}")
        return max(suitable_plans, key=lambda p: p.priority)

    def update_plan(self, updated_plan: Plan):
        self.remove_plan(updated_plan.id, updated_plan.goal_id)
        self.add_plan(updated_plan)