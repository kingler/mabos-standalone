import os
from dotenv import load_dotenv
import uuid
from typing import List, Dict
from app.models.goal import Goal
from app.core.llm_decomposer import LLMDecomposer

# Load environment variables
load_dotenv()


class GoalService:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.llm_decomposer = LLMDecomposer(api_key)
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