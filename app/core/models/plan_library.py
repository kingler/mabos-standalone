from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from app.core.models.agent.plan import Plan


class PlanLibrary(BaseModel):
    """
    Represents a library of plans for achieving goals in a Multi-Agent System (MAS).

    Attributes:
        plans (Dict[str, List[Plan]]): A dictionary mapping goal IDs to lists of plans.
    """
    plans: Dict[str, List[Plan]] = Field(default_factory=dict)

    def add_plan(self, plan: Plan):
        """
        Adds a plan to the library.

        Args:
            plan (Plan): The plan to add.
        """
        if plan.goal_id not in self.plans:
            self.plans[plan.goal_id] = []
        self.plans[plan.goal_id].append(plan)

    def remove_plan(self, plan_id: str, goal_id: str):
        """
        Removes a plan from the library.

        Args:
            plan_id (str): The ID of the plan to remove.
            goal_id (str): The ID of the goal associated with the plan.
        """
        if goal_id in self.plans:
            self.plans[goal_id] = [plan for plan in self.plans[goal_id] if plan.id != plan_id]
            if not self.plans[goal_id]:
                del self.plans[goal_id]

    def get_plans_for_goal(self, goal_id: str) -> List[Plan]:
        """
        Retrieves the plans associated with a specific goal.

        Args:
            goal_id (str): The ID of the goal.

        Returns:
            List[Plan]: The list of plans associated with the goal.
        """
        return self.plans.get(goal_id, [])

    def select_plan(self, goal_id: str, current_state: List[str]) -> Optional[Plan]:
        """
        Selects the most suitable plan for a goal based on the current state.

        Args:
            goal_id (str): The ID of the goal.
            current_state (List[str]): The current state of the agent.

        Returns:
            Optional[Plan]: The selected plan, or None if no suitable plan is found.
        """
        suitable_plans = [plan for plan in self.get_plans_for_goal(goal_id) if plan.check_preconditions(current_state)]
        if suitable_plans:
            return max(suitable_plans, key=lambda p: p.priority)
        return None

    def update_plan(self, updated_plan: Plan):
        """
        Updates an existing plan in the library.

        Args:
            updated_plan (Plan): The updated plan.
        """
        self.remove_plan(updated_plan.id, updated_plan.goal_id)
        self.add_plan(updated_plan)