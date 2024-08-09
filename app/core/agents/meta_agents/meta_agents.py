from uuid import UUID
from typing import List
from app.core.models.agent.agent import Agent
from app.core.models.agent.belief import Belief
from app.core.models.agent.desire import Desire
from app.core.models.agent.intention import Intention
from app.core.models.agent.goal import Goal
from app.core.models.agent.plan import Plan
from app.core.models.agent.task import Task

class MetaAgent(Agent):
    beliefs: List[Belief] = []
    desires: List[Desire] = []
    intentions: List[Intention] = []
    goals: List[Goal] = []
    plans: List[Plan] = []
    tasks: List[Task] = []

    def add_belief(self, description: str, certainty: float = 1.0):
        self.beliefs.append(Belief(description=description, certainty=certainty))

    def add_desire(self, description: str, priority: int):
        self.desires.append(Desire(description=description, priority=priority))

    def add_goal(self, description: str, priority: int):
        self.goals.append(Goal(description=description, priority=priority))

    def create_plan(self, goal_id: UUID, steps: List[str]):
        plan = Plan(goal_id=goal_id, steps=[])
        for step in steps:
            plan.steps.append(Task(description=step))
        self.plans.append(plan)

    def assign_task(self, plan_id: UUID, task_description: str):
        for plan in self.plans:
            if plan.id == plan_id:
                task = Task(description=task_description)
                plan.steps.append(task)
                self.tasks.append(task)
                break

    def update_task_status(self, task_id: UUID, status: str):
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                break

    def reason(self):
        # Reason about beliefs and desires to generate goals
        for belief in self.beliefs:
            if belief.certainty >= 0.8:
                for desire in self.desires:
                    if desire.description.startswith(belief.description):
                        goal = Goal(description=desire.description, priority=desire.priority)
                        if goal not in self.goals:
                            self.goals.append(goal)

        # Reason about goals and plans to generate intentions        
        for goal in self.goals:
            if not any(intention.goal_id == goal.id for intention in self.intentions):
                applicable_plans = [plan for plan in self.plans if plan.goal_id == goal.id]
                if applicable_plans:
                    best_plan = max(applicable_plans, key=lambda plan: sum(task.status == "completed" for task in plan.steps))
                    intention = Intention(goal_id=goal.id, plan_id=best_plan.id)
                    self.intentions.append(intention)

        # Perform BDI reasoning using the reasoning engine
        bdi_results = self.reasoning_engine.reason(
            context={
                "beliefs": [{"content": belief.description} for belief in self.beliefs],
                "desires": [{"description": desire.description, "priority": desire.priority} for desire in self.desires],
                "intentions": [{"goal_id": intention.goal_id, "plan_id": intention.plan_id} for intention in self.intentions]
            }
        )
        self.beliefs = [Belief(description=belief["content"], certainty=1.0) for belief in bdi_results.get("beliefs", [])]
        self.desires = [Desire(description=desire["description"], priority=desire["priority"]) for desire in bdi_results.get("desires", [])]
        self.intentions = [Intention(goal_id=intention["goal_id"], plan_id=intention["plan_id"]) for intention in bdi_results.get("intentions", [])]

    def plan(self):
        for goal in self.goals:
            if not any(plan.goal_id == goal.id for plan in self.plans):
                plan = self.planning_service.generate_plan(goal, self.current_state())
                if plan:
                    self.plans.append(plan)
                    intention = Intention(goal_id=goal.id, plan_id=plan.id)
                    self.intentions.append(intention)
        
        for intention in self.intentions:
            plan = next((plan for plan in self.plans if plan.id == intention.plan_id), None)
            if plan:
                if self.planning_service.execute_plan(plan, self.current_state()):
                    self.update_task_status(plan.id, "completed")
                else:
                    self.planning_service.remove_plan_from_library(plan.id, plan.goal_id)
                    self.plans.remove(plan)
                    self.intentions.remove(intention)

    def execute(self):
        for intention in self.intentions:
            plan = next((plan for plan in self.plans if plan.id == intention.plan_id), None)
            if plan:
                for task in plan.steps:
                    if task.status != "completed":
                        print(f"Executing task: {task.description}")
                        # Execute the task using the appropriate service or module
                        if self.execute_task(task):
                            self.update_task_status(task.id, "completed")
                        else:
                            print(f"Failed to execute task: {task.description}")
                            break
                if all(task.status == "completed" for task in plan.steps):
                    self.update_goal_status(intention.goal_id, "achieved")
                    self.intentions.remove(intention)