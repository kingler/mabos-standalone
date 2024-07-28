from typing import List, Dict, Optional
from pydantic import Field
from ..agent import Agent
from ..goal import Goal
from ..plan import Plan, PlanStep
import uuid
from ..symbolic_planner import SymbolicPlanner

class ProactiveAgent(Agent):
    """
    A proactive agent that can deliberate on goals, generate plans, and execute them.

    Attributes:
        goals (List[Goal]): List of the agent's goals.
        plans (List[Plan]): List of the agent's plans.
        resources (Dict[str, float]): The agent's resources.
    """
    goals: List[Goal] = Field(default_factory=list, description="List of agent's goals")
    plans: List[Plan] = Field(default_factory=list, description="List of agent's plans")
    resources: Dict[str, float] = Field(default_factory=dict, description="Agent's resources")

    def add_goal(self, goal: Goal):
        """
        Add a new goal to the agent.

        Args:
            goal (Goal): The goal to add.
        """
        self.goals.append(goal)
        self.goals.sort(key=lambda g: g.priority, reverse=True)

    def remove_goal(self, goal: Goal):
        """
        Remove a goal from the agent.

        Args:
            goal (Goal): The goal to remove.
        """
        self.goals.remove(goal)

    def deliberate(self):
        """
        Deliberate on goals and update intentions.
        """
        for goal in self.goals:
            if goal.is_achievable(self.beliefs) and self.has_resources_for_goal(goal):
                self.add_intention(goal)

    def has_resources_for_goal(self, goal: Goal) -> bool:
        """
        Check if the agent has the necessary resources for the goal.

        Args:
            goal (Goal): The goal to check resources for.

        Returns:
            bool: True if the agent has the necessary resources, False otherwise.
        """
        for resource, required_amount in goal.resource_requirements.items():
            if resource not in self.resources or self.resources[resource] < required_amount:
                return False
        return True

    def plan(self):
        """
        Generate plans for current intentions.
        """
        for intention in self.intentions:
            new_plan = self.generate_plan(intention)
            if new_plan:
                self.plans.append(new_plan)

    def generate_plan(self, goal: Goal) -> Optional[Plan]:
        """
        Generate a plan to achieve a goal.

        Args:
            goal (Goal): The goal to generate a plan for.

        Returns:
            Optional[Plan]: The generated plan, or None if a plan cannot be generated.
        """
        # Use a planning library or custom logic to generate a plan
        from app.models.plan_library import PlanningLibrary, CustomPlanner

        # Check if a suitable plan exists in the plan library
        plan_library = PlanningLibrary()
        existing_plan = plan_library.select_plan(goal.id, self.beliefs)
        if existing_plan:
            return existing_plan

        # If no suitable plan found, generate a new plan using custom logic
        custom_planner = CustomPlanner()
        new_plan = custom_planner.generate_plan(goal, self.beliefs, self.capabilities)
        if new_plan:
            plan_library.add_plan(new_plan)
            return new_plan
        plan_id = str(uuid.uuid4())
        steps = self.create_plan_steps(goal)
        if steps:
            return Plan(
                id=plan_id,
                goal_id=goal.id,
                steps=steps,
                symbolic_plan=self.create_symbolic_plan(goal),
                llm_plan=self.create_llm_plan(goal),
                is_completed=False
            )
        return None

    def create_plan_steps(self, goal: Goal) -> List[PlanStep]:
        """
        Create a list of plan steps to achieve the goal.

        Args:
            goal (Goal): The goal to create plan steps for.

        Returns:
            List[PlanStep]: The list of plan steps.
        """
        steps = []
        for requirement in goal.requirements:
            if requirement in self.capabilities:
                step_id = str(uuid.uuid4())
                step_description = f"Fulfill requirement: {requirement}"
                step = PlanStep(id=step_id, description=step_description, goal_id=goal.id)
                steps.append(step)
            else:
                print(f"Agent does not have the capability to fulfill requirement: {requirement}")
        
        if len(steps) == len(goal.requirements):
            return steps
        else:
            print(f"Agent cannot create a complete plan for goal: {goal.description}")
            return []
        return [
            PlanStep(id=str(uuid.uuid4()), description=f"Step 1 to achieve {goal.description}"),
            PlanStep(id=str(uuid.uuid4()), description=f"Step 2 to achieve {goal.description}"),
            PlanStep(id=str(uuid.uuid4()), description=f"Step 3 to achieve {goal.description}")
        ]

    def create_symbolic_plan(self, goal: Goal) -> Dict:
        """
        Create a symbolic plan for the goal.

        Args:
            goal (Goal): The goal to create a symbolic plan for.

        Returns:
            Dict: The symbolic plan.
        """
        symbolic_plan = {}
        
        # Define initial state and goal state
        initial_state = self.get_current_state()
        goal_state = goal.get_desired_state()
        
        # Define planning domain and problem
        domain = self.create_planning_domain()
        problem = self.create_planning_problem(initial_state, goal_state)
        
        # Call symbolic planner to generate plan
        planner = SymbolicPlanner()
        plan = planner.solve(domain, problem)
        
        # Convert plan to symbolic representation
        for action in plan:
            symbolic_plan[action.name] = action.parameters
        
        return symbolic_plan

    def create_llm_plan(self, goal: Goal) -> Dict:
        """
        Create an LLM-based plan for the goal.

        Args:
            goal (Goal): The goal to create an LLM-based plan for.

        Returns:
            Dict: The LLM-based plan.
        """
        # TODO: Implement LLM-based planning logic
        return {}  # Placeholder

    def execute(self):
        """
        Execute plans to achieve goals.
        """
        for plan in self.plans:
            if not plan.is_completed:
                self.execute_plan(plan)

    def execute_plan(self, plan: Plan):
        """
        Execute a single plan.

        Args:
            plan (Plan): The plan to execute.
        """
        while not plan.is_completed:
            next_step = plan.get_next_step()
            if next_step:
                if self.execute_step(next_step):
                    plan.update_step_status(next_step.id, True)
                else:
                    self.replan(plan)
                    break
            else:
                break
        plan.check_completion()

        goal = next((g for g in self.goals if g.id == plan.goal_id), None)
        if plan.is_completed and goal:
            goal.update_status(True)

    def execute_step(self, step: PlanStep) -> bool:
        """
        Execute a single step of the plan.

        Args:
            step (PlanStep): The step to execute.

        Returns:
            bool: True if the step is executed successfully, False otherwise.
        """
        # Check if the agent has the capability to execute the step
        if self.has_capability(step.description):
            # Execute the step based on its description
            if step.description.startswith("Move to"):
                target_location = step.description.split("Move to ")[1]
                self.move_to(target_location)
            elif step.description.startswith("Pick up"):
                object_name = step.description.split("Pick up ")[1]
                self.pick_up(object_name)
            elif step.description.startswith("Put down"):
                object_name = step.description.split("Put down ")[1]
                self.put_down(object_name)
            elif step.description.startswith("Use"):
                tool_name = step.description.split("Use ")[1]
                self.use_tool(tool_name)
            elif step.description.startswith("Interact with"):
                    entity_name = step.description.split("Interact with ")[1]
                    self.interact_with(entity_name)
            elif step.description.startswith("Communicate"):
                    message = step.description.split("Communicate ")[1]
                    self.communicate(message)
            else:
                    print(f"Unknown step description: {step.description}")
                    return False
            pass
            
            print(f"Executed step: {step.description}")
            return True
        else:
            print(f"Agent does not have the capability to execute step: {step.description}")
            return False

    def replan(self, plan: Plan):
        """
        Replan when a step fails.

        Args:
            plan (Plan): The plan that needs replanning.
        """
        print(f"Replanning for goal: {plan.goal_id}")
        
        # Get the goal associated with the plan
        goal = next((g for g in self.goals if g.id == plan.goal_id), None)
        
        if goal:
            # Generate a new plan using the symbolic planner
            symbolic_planner = SymbolicPlanner()
            new_plan = symbolic_planner.plan(goal)
            
            if new_plan:
                # Update the plan with the new steps
                plan.steps = new_plan.steps
                plan.symbolic_plan = new_plan.symbolic_plan
                plan.llm_plan = new_plan.llm_plan
                plan.is_completed = False
                print(f"Successfully replanned for goal: {plan.goal_id}")
            else:
                print(f"Failed to generate a new plan for goal: {plan.goal_id}")
        else:
            print(f"No goal found associated with plan: {plan.id}")