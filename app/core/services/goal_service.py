import os
from dotenv import load_dotenv
import uuid
from typing import List
from app.core.models.agent.goal import Goal, SoftGoal
from app.core.models.llm_decomposer import LLMDecomposer

# Load environment variables
load_dotenv()


class GoalService:
    def __init__(self):
        self.llm_decomposer = LLMDecomposer()
        self.goals = {}

    def create_goal(self, description: str, priority: int) -> Goal:
        goal_id = str(uuid.uuid4())
        new_goal = Goal(
            id=goal_id,
            description=description,
            priority=priority
        )
        self.goals[goal_id] = new_goal
        return new_goal

    def get_goal(self, goal_id: str) -> Goal:
        return self.goals.get(goal_id)

    def list_goals(self) -> List[Goal]:
        return list(self.goals.values())

    def decompose_goal(self, goal_id: str) -> Goal:
        goal = self.goals.get(goal_id)
        if goal:
            goal.decompose(self.llm_decomposer)
        return goal

    def update_goal_status(self, goal_id: str, is_achieved: bool) -> Goal:
        goal = self.goals.get(goal_id)
        if goal:
            goal.is_achieved = is_achieved
        return goal

    def add_soft_goal_to_goal(self, goal_id: str, soft_goal: SoftGoal):
        goal = self.get_goal(goal_id)
        if goal:
            goal.add_soft_goal(soft_goal)

    def update_goal_contribution(self, goal_id: str, parent_goal_id: str, contribution: float):
        goal = self.get_goal(goal_id)
        if goal:
            goal.update_contribution(parent_goal_id, contribution)

    def propagate_goal_changes(self, goal_id: str):
        goal = self.get_goal(goal_id)
        if goal:
            goal.propagate_changes()