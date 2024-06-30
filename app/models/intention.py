from typing import List, Dict, Any
from .belief import Belief
from .desire import Desire
from ..task_management.action import Action
from .knowledge_base import KnowledgeBase
from app.core.knowledge_graph import KnowledgeGraph

class Intention:
    def __init__(self, intention_id: str, description: str, actions: List[Action], goal: Any, preconditions: List[str], postconditions: List[str], status: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph):
        self.intention_id = intention_id
        self.description = description
        self.actions = actions
        self.goal = goal
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.status = status
        self.knowledge_base = knowledge_base
        self.knowledge_graph = knowledge_graph

    def activate_intention(self):
        self.status = "active"

    def suspend_intention(self):
        self.status = "suspended"

    def complete_intention(self):
        self.status = "completed"

    def is_achievable(self, current_beliefs: List[Belief]) -> bool:
        return any(belief.description == self.goal.description and belief.certainty >= 0.8 for belief in current_beliefs)

    def execute_intention(self):
        for action in self.actions:
            action.execute()
        self.status = "completed" if all(action.is_completed() for action in self.actions) else "failed"

    def update_status(self, new_status: str):
        self.status = new_status

    def revise_intention(self, new_goal: Any, new_actions: List[Action]):
        self.goal = new_goal
        self.actions = new_actions
        self.status = "revised"