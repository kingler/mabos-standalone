from typing import List, Optional
import uuid
from app.models.business.business_goal import BusinessGoal

class BusinessGoalService:
    def __init__(self):
        self.goals = {}

    def create_goal(self, name: str, description: str, priority: str, parent_goal_id: Optional[str] = None) -> BusinessGoal:
        goal_id = str(uuid.uuid4())
        new_goal = BusinessGoal(
            id=goal_id,
            name=name,
            description=description,
            priority=priority,
            parent_goal_id=parent_goal_id
        )
        self.goals[goal_id] = new_goal
        if parent_goal_id:
            parent_goal = self.goals.get(parent_goal_id)
            if parent_goal:
                parent_goal.child_goal_ids.append(goal_id)
        return new_goal

    def get_goal(self, goal_id: str) -> Optional[BusinessGoal]:
        return self.goals.get(goal_id)

    def list_goals(self) -> List[BusinessGoal]:
        return list(self.goals.values())

    def update_goal(self, goal_id: str, **kwargs) -> Optional[BusinessGoal]:
        goal = self.goals.get(goal_id)
        if goal:
            for key, value in kwargs.items():
                setattr(goal, key, value)
            return goal
        return None

    def delete_goal(self, goal_id: str) -> bool:
        if goal_id in self.goals:
            del self.goals[goal_id]
            return True
        return False