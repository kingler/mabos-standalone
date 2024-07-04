from pydantic import BaseModel, Field
from typing import List, Dict, Any
from .goal import Goal
from .task import Task
from .action import Action


class GoalPlanTree(BaseModel):
    root: Task
    subtasks: Dict[str, List[Task]] = Field(default_factory=dict)
    actions: Dict[str, List[Action]] = Field(default_factory=dict)

    def add_subtask(self, parent_task: Task, subtask: Task):
        if parent_task.id not in self.subtasks:
            self.subtasks[parent_task.id] = []
        self.subtasks[parent_task.id].append(subtask)

    def add_action(self, task: Task, action: Action):
        if task.id not in self.actions:
            self.actions[task.id] = []
        self.actions[task.id].append(action)

    def get_actions(self) -> List[Action]:
        return [action for action_list in self.actions.values() for action in action_list]

class HTNPlanner(BaseModel):
    domain_knowledge: Dict[str, Any] = Field(default_factory=dict)

    def plan(self, goal: Goal, current_state: Dict[str, Any]) -> GoalPlanTree:
        root_task = self._convert_goal_to_task(goal)
        goal_plan_tree = GoalPlanTree(root=root_task)
        self._decompose_task(root_task, current_state, goal_plan_tree)
        return goal_plan_tree

    def _convert_goal_to_task(self, goal: Goal) -> Task:
        return Task(description=goal.description, task_type="high_level", priority=goal.priority)

    def _decompose_task(self, task: Task, state: Dict[str, Any], tree: GoalPlanTree):
        if task.task_type == "primitive":
            action = Action(action_id=task.id, description=task.description)
            tree.add_action(task, action)
        else:
            methods = self._get_applicable_methods(task, state)
            for method in methods:
                subtasks = self._apply_method(method, task, state)
                for subtask in subtasks:
                    tree.add_subtask(task, subtask)
                    self._decompose_task(subtask, state, tree)

    def _get_applicable_methods(self, task: Task, state: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [method for method in self.domain_knowledge.get(task.description, [])
                if self._method_preconditions_met(method, state)]

    def _method_preconditions_met(self, method: Dict[str, Any], state: Dict[str, Any]) -> bool:
        return all(self._condition_met(precondition, state) for precondition in method.get('preconditions', []))

    def _condition_met(self, condition: Dict[str, Any], state: Dict[str, Any]) -> bool:
        condition_type = condition["type"]
        variable = state.get(condition["variable"])
        value = condition["value"]

        if condition_type == "equals":
            return variable == value
        elif condition_type == "not_equals":
            return variable != value
        elif condition_type == "greater_than":
            return variable > value
        elif condition_type == "less_than":
            return variable < value
        elif condition_type == "in":
            return value in (variable or [])
        elif condition_type == "not_in":
            return value not in (variable or [])
        else:
            raise ValueError(f"Unknown condition type: {condition_type}")

    def _apply_method(self, method: Dict[str, Any], task: Task, state: Dict[str, Any]) -> List[Task]:
        return [Task(description=subtask, task_type=method.get('type', 'compound'), priority=task.priority) 
                for subtask in method.get('subtasks', [])]

    def execute_plan(self, goal_plan_tree: GoalPlanTree) -> bool:
        return all(self._execute_action(action) for action in goal_plan_tree.get_actions())

    def _execute_action(self, action: Action) -> bool:
        # In a real system, this would interact with the environment or other systems
        # For now, we'll just return True to simulate successful execution
        print(f"Executing action: {action.description}")
        return True

    def plan_and_execute(self, goal: Goal, current_state: Dict[str, Any]) -> bool:
        goal_plan_tree = self.plan(goal, current_state)
        return self.execute_plan(goal_plan_tree)

    def retrieve_links(self, impacted_classes: List[str]) -> List[str]:
        # Implement probabilistic retrieval algorithm to return links between impacted classes and SIG elements
        return [link for link in self.domain_knowledge if link in impacted_classes]