from typing import Any, Dict, List

from app.models.agent.action import Action
from app.models.agent.goal import Goal
from app.models.agent.plan import Plan
from app.models.agent.task import Task
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.knowledge.reasoning.htn_planner import (GoalPlanTree,
                                                             HTNPlanner)
from app.tools.reasoner import Reasoner
from app.models.plan_library import PlanLibrary


class PlanningService:
    def __init__(self, domain_knowledge: Dict[str, Any]):
        self.knowledge_base = KnowledgeBase
        self.reasoner = Reasoner(KnowledgeBase)
        self.htn_planner = HTNPlanner(domain_knowledge=domain_knowledge)
        self.plan_library = PlanLibrary()

    def generate_plan(self, goal: Goal, current_state: Dict[str, Any]) -> Plan:
        # First, try to find a suitable plan in the library
        try:
            return self.plan_library.select_plan(goal.id, list(current_state.keys()))
        except ValueError:
            # If no suitable plan is found, generate a new one using HTN planning
            goal_plan_tree = self.htn_planner.plan(goal, current_state)
            new_plan = self._convert_tree_to_plan(goal_plan_tree, goal)
            self._link_plan_to_goal(new_plan, goal)
            self.plan_library.add_plan(new_plan)
            return new_plan

    def _link_plan_to_goal(self, plan: Plan, goal: Goal):
        for step in plan.steps:
            step.goal_id = goal.id

    def _convert_tree_to_plan(self, tree: GoalPlanTree, goal: Goal) -> Plan:
        actions = tree.get_actions()
        return Plan(
            goal_id=goal.id,
            actions=[action.id for action in actions],
            priority=goal.priority,
            preconditions=self._extract_preconditions(tree),
            postconditions=self._extract_postconditions(tree)
        )

    def _extract_preconditions(self, tree: GoalPlanTree) -> List[str]:
        # This is a simplification. In a real system, you'd need to analyze the tree structure
        return [f"precondition_{i}" for i in range(len(tree.subtasks))]

    def _extract_postconditions(self, tree: GoalPlanTree) -> List[str]:
        # This is a simplification. In a real system, you'd need to analyze the tree structure
        return [f"postcondition_{i}" for i in range(len(tree.actions))]

    def execute_plan(self, plan: Plan, current_state: Dict[str, Any]) -> bool:
        return self.htn_planner.execute_plan(self._convert_plan_to_tree(plan, current_state))

    def _convert_plan_to_tree(self, plan: Plan, current_state: Dict[str, Any]) -> GoalPlanTree:
        # This is a simplification. In a real system, you'd need to recreate the tree structure
        root_task = Task(description=f"Achieve goal {plan.goal_id}", task_type="high_level", priority=plan.priority)
        tree = GoalPlanTree(root=root_task)
        for action_id in plan.actions:
            action = Action(action_id=action_id, description=f"Execute action {action_id}")
            tree.add_action(root_task, action)
        return tree

    def add_plan_to_library(self, plan: Plan):
        self.plan_library.add_plan(plan)

    def remove_plan_from_library(self, plan_id: str, goal_id: str):
        self.plan_library.remove_plan(plan_id, goal_id)

    def get_plans_for_goal(self, goal_id: str) -> List[Plan]:
        return self.plan_library.get_plans_for_goal(goal_id)

    def update_plan_in_library(self, updated_plan: Plan):
        self.plan_library.update_plan(updated_plan)

    def retrieve_links(self, impacted_classes: List[str]) -> List[str]:
        return self.htn_planner.retrieve_links(impacted_classes)

    def user_evaluation(self, links: List[str]) -> List[str]:
        # Implement user evaluation logic to accept/reject links
        accepted_links = []
        for link in links:
            user_input = input(f"Do you accept the link: {link}? (yes/no): ")
            if user_input.lower() == "yes":
                accepted_links.append(link)
        return accepted_links

    def re_analyze_contributions(self, goal_id: str):
        goal = self.goal_service.get_goal(goal_id)
        if goal:
            for parent_goal_id, contribution in goal.contributions.items():
                # Modify contributions as necessary
                new_contribution = float(input(f"Enter new contribution value for parent goal {parent_goal_id}: "))
                goal.update_contribution(parent_goal_id, new_contribution)
            self.goal_service.propagate_goal_changes(goal_id)

    def re_evaluate_goals(self, impacted_elements: List[str]):
        for element in impacted_elements:
            goal = self.goal_service.get_goal(element)
            if goal:
                self.re_analyze_contributions(goal.id)
                # Propagate changes throughout the SIG
                self.goal_service.propagate_goal_changes(goal.id)
        
        