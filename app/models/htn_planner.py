from pydantic import BaseModel, Field
from typing import List, Dict, Any
from .goal import Goal
from .task import Task
from .action import Action


class GoalPlanTree(BaseModel):
    """
    Represents a goal plan tree in the HTN planner.

    Attributes:
        root (Task): The root task of the goal plan tree.
        subtasks (Dict[str, List[Task]]): A dictionary mapping task IDs to their subtasks.
        actions (Dict[str, List[Action]]): A dictionary mapping task IDs to their actions.
    """
    root: Task
    subtasks: Dict[str, List[Task]] = Field(default_factory=dict)
    actions: Dict[str, List[Action]] = Field(default_factory=dict)

    def add_subtask(self, parent_task: Task, subtask: Task):
        """
        Add a subtask to the parent task in the goal plan tree.

        Args:
            parent_task (Task): The parent task to add the subtask to.
            subtask (Task): The subtask to add.
        """
        if parent_task.id not in self.subtasks:
            self.subtasks[parent_task.id] = []
        self.subtasks[parent_task.id].append(subtask)

    def add_action(self, task: Task, action: Action):
        """
        Add an action to the task in the goal plan tree.

        Args:
            task (Task): The task to add the action to.
            action (Action): The action to add.
        """
        if task.id not in self.actions:
            self.actions[task.id] = []
        self.actions[task.id].append(action)

    def get_actions(self) -> List[Action]:
        """
        Get all actions in the goal plan tree.

        Returns:
            List[Action]: A list of all actions in the goal plan tree.
        """
        return [action for action_list in self.actions.values() for action in action_list]

class HTNPlanner(BaseModel):
    """
    Represents an HTN (Hierarchical Task Network) planner.

    Attributes:
        domain_knowledge (Dict[str, Any]): The domain knowledge used by the planner.
    """
    domain_knowledge: Dict[str, Any] = Field(default_factory=dict)

    def plan(self, goal: Goal, current_state: Dict[str, Any]) -> GoalPlanTree:
        """
        Generate a plan for the given goal based on the current state.

        Args:
            goal (Goal): The goal to plan for.
            current_state (Dict[str, Any]): The current state of the environment.

        Returns:
            GoalPlanTree: The generated goal plan tree.
        """
        root_task = self._convert_goal_to_task(goal)
        goal_plan_tree = GoalPlanTree(root=root_task)
        self._decompose_task(root_task, current_state, goal_plan_tree)
        return goal_plan_tree

    def _convert_goal_to_task(self, goal: Goal) -> Task:
        """
        Convert a goal to a task.

        Args:
            goal (Goal): The goal to convert.

        Returns:
            Task: The converted task.
        """
        return Task(description=goal.description, task_type="high_level", priority=goal.priority)

    def _decompose_task(self, task: Task, state: Dict[str, Any], tree: GoalPlanTree):
        """
        Decompose a task into subtasks or actions.

        Args:
            task (Task): The task to decompose.
            state (Dict[str, Any]): The current state of the environment.
            tree (GoalPlanTree): The goal plan tree to update with subtasks and actions.
        """
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
        """
        Get applicable methods for the given task based on the current state.

        Args:
            task (Task): The task to find applicable methods for.
            state (Dict[str, Any]): The current state of the environment.

        Returns:
            List[Dict[str, Any]]: A list of applicable methods.
        """
        return [method for method in self.domain_knowledge.get(task.description, [])
                if self._method_preconditions_met(method, state)]

    def _method_preconditions_met(self, method: Dict[str, Any], state: Dict[str, Any]) -> bool:
        """
        Check if the preconditions of a method are met based on the current state.

        Args:
            method (Dict[str, Any]): The method to check preconditions for.
            state (Dict[str, Any]): The current state of the environment.

        Returns:
            bool: True if all preconditions are met, False otherwise.
        """
        return all(self._condition_met(precondition, state) for precondition in method.get('preconditions', []))

    def _condition_met(self, condition: Dict[str, Any], state: Dict[str, Any]) -> bool:
        """
        Check if a condition is met based on the current state.

        Args:
            condition (Dict[str, Any]): The condition to check.
            state (Dict[str, Any]): The current state of the environment.

        Returns:
            bool: True if the condition is met, False otherwise.

        Raises:
            ValueError: If the condition type is unknown.
        """
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
        """
        Apply a method to a task to generate subtasks.

        Args:
            method (Dict[str, Any]): The method to apply.
            task (Task): The task to apply the method to.
            state (Dict[str, Any]): The current state of the environment.

        Returns:
            List[Task]: The generated subtasks.
        """
        return [Task(description=subtask, task_type=method.get('type', 'compound'), priority=task.priority) 
                for subtask in method.get('subtasks', [])]

    def execute_plan(self, goal_plan_tree: GoalPlanTree) -> bool:
        """
        Execute the actions in the goal plan tree.

        Args:
            goal_plan_tree (GoalPlanTree): The goal plan tree containing the actions to execute.

        Returns:
            bool: True if all actions are executed successfully, False otherwise.
        """
        return all(self._execute_action(action) for action in goal_plan_tree.get_actions())

    def _execute_action(self, action: Action) -> bool:
        """
        Execute a single action.

        Args:
            action (Action): The action to execute.

        Returns:
            bool: True if the action is executed successfully, False otherwise.
        """
        # In a real system, this would interact with the environment or other systems
        # For now, we'll just return True to simulate successful execution
        print(f"Executing action: {action.description}")
        return True

    def plan_and_execute(self, goal: Goal, current_state: Dict[str, Any]) -> bool:
        """
        Generate a plan for the given goal and execute it.

        Args:
            goal (Goal): The goal to plan and execute.
            current_state (Dict[str, Any]): The current state of the environment.

        Returns:
            bool: True if the plan is generated and executed successfully, False otherwise.
        """
        goal_plan_tree = self.plan(goal, current_state)
        return self.execute_plan(goal_plan_tree)

    def retrieve_links(self, impacted_classes: List[str]) -> List[str]:
        """
        Retrieve links between impacted classes and SIG elements using a probabilistic retrieval algorithm.

        Args:
            impacted_classes (List[str]): The list of impacted classes.

        Returns:
            List[str]: The list of retrieved links.
        """
        # Implement probabilistic retrieval algorithm to return links between impacted classes and SIG elements
        return [link for link in self.domain_knowledge if link in impacted_classes]