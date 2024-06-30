from typing import Callable, List
from .belief import Belief

class Desire:
    def __init__(self, desire_id: str, description: str, priority: int, activation_condition: Callable[[List[Belief]], bool], completion_condition: Callable[[List[Belief]], bool], deadline: float):
        self.desire_id = desire_id
        self.description = description
        self.priority = priority
        self.activation_condition = activation_condition
        self.completion_condition = completion_condition
        self.deadline = deadline

    def is_active(self, current_beliefs: List[Belief]) -> bool:
        return self.activation_condition(current_beliefs)

    def is_completed(self, current_beliefs: List[Belief]) -> bool:
        return self.completion_condition(current_beliefs)

    def update_priority(self, new_priority: int):
        self.priority = new_priority

    def is_achievable(self, current_beliefs: List[Belief]) -> bool:
        # Implement logic to determine if the desire is achievable given current beliefs
        return True  # Placeholder