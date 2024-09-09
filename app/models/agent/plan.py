from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict


class PlanStep(BaseModel):
    """
    Represents a step in a plan.

    Attributes:
        id (str): The unique identifier of the plan step.
        description (str): The description of the plan step.
        is_completed (bool): Indicates whether the plan step is completed. Defaults to False.
        goal_id (Optional[str]): The identifier of the associated goal, if any. Defaults to None.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    description: str
    is_completed: bool = False
    goal_id: Optional[str] = None

class Plan(BaseModel):
    """
    Represents a plan for achieving a goal.

    Attributes:
        id (str): The unique identifier of the plan.
        goal_id (str): The identifier of the associated goal.
        steps (List[PlanStep]): The list of steps in the plan.
        symbolic_plan (Dict): The symbolic representation of the plan.
        llm_plan (Dict): The LLM (Language Model) representation of the plan.
        is_completed (bool): Indicates whether the plan is completed. Defaults to False.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: str
    goal_id: str
    steps: List[PlanStep]
    symbolic_plan: Dict
    llm_plan: Dict
    is_completed: bool = False

    def add_step(self, step: PlanStep):
        """
        Adds a step to the plan and links it to the associated goal if specified.

        Args:
            step (PlanStep): The plan step to add.
        """
        self.steps.append(step)
        if step.goal_id:
            self._link_step_to_goal(step)
            
    def _link_step_to_goal(self, step: PlanStep):
        """
        Links a plan step to its associated goal.

        Args:
            step (PlanStep): The plan step to link.

        Raises:
            ValueError: If the specified goal is not found.
        """
        from .goal import Goal
        
        if step.goal_id:
            if goal := Goal.get(id=step.goal_id):
                goal.plan_steps.append(step)
            else:
                raise ValueError(f"Goal with ID {step.goal_id} not found")
            
    def update_step_status(self, step_id: str, is_completed: bool):
        """
        Updates the completion status of a plan step.

        Args:
            step_id (str): The identifier of the plan step to update.
            is_completed (bool): The new completion status of the plan step.
        """
        for step in self.steps:
            if step.id == step_id:
                step.is_completed = is_completed
                break
        self.check_completion()

    def check_completion(self):
        """
        Checks if all steps in the plan are completed and updates the plan's completion status.
        """
        self.is_completed = all(step.is_completed for step in self.steps)

    def get_next_step(self) -> Optional[PlanStep]:
        """
        Retrieves the next incomplete step in the plan.

        Returns:
            Optional[PlanStep]: The next incomplete step, or None if all steps are completed.
        """
        return next((step for step in self.steps if not step.is_completed), None)
    def check_preconditions(self, current_state: List[str]) -> bool:
        """
        Checks if the preconditions for the plan are met in the current state.

        Args:
            current_state (List[str]): A list of strings representing the current state.

        Returns:
            bool: True if all preconditions are met, False otherwise.
        """
        # Assuming self.preconditions is a list of required conditions for the plan
        if not hasattr(self, 'preconditions') or not self.preconditions:
            return True  # If no preconditions are defined, consider them met

        # Check if all preconditions are in the current state
        return all(precondition in current_state for precondition in self.preconditions)

    @property
    def priority(self) -> int:
        """
        Calculate and return the priority of the plan.

        The priority is determined by:
        1. The urgency of the associated goal
        2. The number of steps in the plan (shorter plans are prioritized)
        3. The current completion status

        Returns:
            int: The calculated priority of the plan (higher value means higher priority)
        """
        base_priority = 100  # Start with a base priority

        # Factor in goal urgency (assuming Goal has an 'urgency' attribute)
        if hasattr(self, 'goal') and hasattr(self.goal, 'urgency'):
            base_priority += self.goal.urgency * 10

        # Prioritize shorter plans
        step_count_factor = max(10 - len(self.steps), 0)  # Max 10 points for this factor
        base_priority += step_count_factor

        # Consider completion status
        if not self.is_completed:
            completion_percentage = sum(step.is_completed for step in self.steps) / len(self.steps)
            base_priority += int((1 - completion_percentage) * 20)  # Max 20 points for incomplete plans

        return base_priority
