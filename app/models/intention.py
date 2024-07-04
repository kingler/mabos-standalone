from typing import List, Any, Optional
from pydantic import BaseModel, Field
from .belief import Belief
from .plan import Plan
from .goal import Goal


class Intention(BaseModel):
    """
    Represents an intention in the BDI model.

    Attributes:
        status (str): The current status of the intention.
        goal (Goal): The goal associated with the intention.
        plan (Plan): The plan to achieve the goal.
    """
    status: str = "pending"
    goal: Goal
    plan: Plan
    
    class Config:
        from_attributes = True

    def activate_intention(self):
        """
        Activates the intention by setting its status to "active".
        """
        self.status = "active"

    def suspend_intention(self):
        """
        Suspends the intention by setting its status to "suspended".
        """
        self.status = "suspended"

    def complete_intention(self):
        """
        Completes the intention by setting its status to "completed".
        """
        self.status = "completed"

    def is_achievable(self, current_beliefs: List[Belief]) -> bool:
        """
        Checks if the intention is achievable based on the current beliefs.

        Args:
            current_beliefs (List[Belief]): The list of current beliefs.

        Returns:
            bool: True if the intention is achievable, False otherwise.
        """
        return any(belief.description == self.goal.description and belief.certainty >= 0.8 for belief in current_beliefs)

    def execute_intention(self, execute_action):
        """
        Executes the intention by calling the provided execute_action function.

        Args:
            execute_action: The function to execute the intention.
        """
        result = execute_action()
        self.status = "completed" if result else "failed"
        return result

    def update_status(self, new_status: str):
        """
        Updates the status of the intention.

        Args:
            new_status (str): The new status of the intention.
        """
        self.status = new_status

    def revise_intention(self, new_goal: Goal, new_plan: Optional[Plan] = None):
        """
        Revises the intention by updating the goal and optionally the plan, and setting the status to "revised".

        Args:
            new_goal (Goal): The new goal for the intention.
            new_plan (Optional[Plan]): The new plan for the intention, if provided.
        """
        self.goal = new_goal
        if new_plan:
            self.plan = new_plan
        self.status = "revised"

    def is_completed(self) -> bool:
        """
        Checks if the intention is completed.

        Returns:
            bool: True if the intention status is "completed", False otherwise.
        """
        return self.status == "completed"

    def is_failed(self) -> bool:
        """
        Checks if the intention has failed.

        Returns:
            bool: True if the intention status is "failed", False otherwise.
        """
        return self.status == "failed"

Intention.model_rebuild()
