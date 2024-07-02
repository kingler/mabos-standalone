from typing import List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field

from .belief import Belief
from .desire import Desire
from .intention import Intention
from .action import Action
from .goal import Goal
from .plan import Plan, PlanStep


class Agent(BaseModel):
    agent_id: str = Field(..., description="The unique identifier of the agent")
    name: str = Field(..., description="The name of the agent")
    beliefs: List[Belief] = Field(default_factory=list, description="The agent's current beliefs about the world")
    desires: List[Desire] = Field(default_factory=list, description="The agent's current desires")
    intentions: List[Intention] = Field(default_factory=list, description="The agent's current intentions")
    available_actions: List[Action] = Field(default_factory=list, description="Actions available to the agent")

    def add_belief(self, belief: Belief):
        self.beliefs.append(belief)

    def remove_belief(self, belief: Belief):
        self.beliefs.remove(belief)

    def add_desire(self, desire: Desire):
        self.desires.append(desire)

    def remove_desire(self, desire: Desire):
        self.desires.remove(desire)

    def add_intention(self, intention: Intention):
        self.intentions.append(intention)

    def remove_intention(self, intention: Intention):
        self.intentions.remove(intention)

    def add_action(self, action: Action):
        self.available_actions.append(action)

    def remove_action(self, action: Action):
        self.available_actions.remove(action)

    def deliberate(self):
        # Filter desires by priority and status
        active_desires = [d for d in self.desires if d.status == "active"]
        active_desires.sort(key=lambda d: d.priority, reverse=True)

        # Select the highest priority active desire
        if active_desires and (selected_desire := active_desires[0]):
            # Check if the selected desire is not being pursued
            if all(i.goal != selected_desire for i in self.intentions):
                # Create a new intention for the selected desire
                self.add_intention(Intention(goal=selected_desire))

    def plan(self):
        for intention in self.intentions:
            if intention.status == "active":
                if applicable_actions := [
                    action for action in self.available_actions 
                    if action.is_applicable(lambda key: next((b.certainty for b in self.beliefs if b.description == key), None))
                ]:
                    # Select the first applicable action for now
                    selected_action = applicable_actions[0]
                    
                    # Check if the selected action achieves the intention's goal
                    if selected_action.is_completed(lambda key: next((b.certainty for b in self.beliefs if b.description == key), None)):
                        intention.complete_intention()
                    else:
                        # Add the selected action to the intention's action list
                        intention.actions.append(selected_action)
                else:
                    # No applicable actions found, suspend the intention
                    intention.suspend_intention()

    def execute(self):
        for intention in self.intentions:
            for action in intention.actions:
                action.execute(
                    get_belief=lambda key: next((b.certainty for b in self.beliefs if b.description == key), None),
                    set_belief=lambda key, value: self.add_belief(Belief(description=key, certainty=value))
                )



    def revise_beliefs(self, new_belief: Belief):
        """Revise beliefs based on new information."""
        if existing_belief := next((b for b in self.beliefs if b.description == new_belief.description), None):
            existing_belief.update(new_belief)
        else:
            self.add_belief(new_belief)

    def select_desires(self):
        """Select desires based on current beliefs and intentions."""
        return [d for d in self.desires if self.is_desire_relevant(d)]

    def is_desire_relevant(self, desire: Desire) -> bool:
        """Check if a desire is relevant given current beliefs and intentions."""
        # Implement relevance checking logic
        return True  # Placeholder

    def commit_to_intention(self, intention: Intention):
        """Commit to an intention, possibly dropping conflicting intentions."""
        conflicting_intentions = [i for i in self.intentions if self.are_intentions_conflicting(i, intention)]
        for conflicting in conflicting_intentions:
            self.drop_intention(conflicting)
        self.add_intention(intention)

    def are_intentions_conflicting(self, intention1: Intention, intention2: Intention) -> bool:
        """Check if two intentions are conflicting."""
        # Implement conflict checking logic
        return False  # Placeholder

    def drop_intention(self, intention: Intention):
        """Drop an intention and clean up related plans."""
        self.intentions.remove(intention)
        self.plans = [p for p in self.plans if p.goal_id != intention.goal.id]

    def update_intention_status(self, intention: Intention, new_status: str):
        """Update an intention's status."""
        intention.update_status(new_status)
        
Agent.model_rebuild()

class EnvironmentalAgent(Agent):
    environment_state: Dict[str, Any] = Field(default_factory=dict, description="The current state of the environment")

    def update_environment_state(self, new_state: Dict[str, Any]):
        """Update the agent's perception of the environment state."""
        self.environment_state.update(new_state)

    def perceive(self):
        """Perceive the environment and update beliefs."""
        for key, value in self.environment_state.items():
            self.add_belief(f"{key}: {value}")

    def act(self):
        """Perform actions based on the current environment state."""
        # This method can be overridden with specific environmental actions
        pass        

EnvironmentalAgent.model_rebuild()        
        
class ProactiveAgent(Agent):
    goals: List[Goal] = Field(default_factory=list, description="List of agent's goals")
    plans: List[Plan] = Field(default_factory=list, description="List of agent's plans")
    resources: Dict[str, float] = Field(default_factory=dict, description="Agent's resources")

    def add_goal(self, goal: Goal):
        """Add a new goal to the agent."""
        self.goals.append(goal)
        self.goals.sort(key=lambda g: g.priority, reverse=True)

    def remove_goal(self, goal: Goal):
        """Remove a goal from the agent."""
        self.goals.remove(goal)

    def deliberate(self):
        """Deliberate on goals and update intentions."""
        for goal in self.goals:
            if goal.is_achievable(self.beliefs) and self.has_resources_for_goal(goal):
                self.add_intention(goal)

    def has_resources_for_goal(self, goal: Goal) -> bool:
        """Check if the agent has the necessary resources for the goal."""
        # Implement resource checking logic
        return True  # Placeholder

    def plan(self):
        """Generate plans for current intentions."""
        for intention in self.intentions:
            if new_plan := self.generate_plan(intention):
                self.plans.append(new_plan)

    def generate_plan(self, goal: Goal) -> Plan:
        """Generate a plan to achieve a goal."""
        # Implement a more sophisticated planning algorithm
        # This could involve using a planning library or custom logic
        # For now, we'll return an improved dummy plan
        plan_id = str(UUID.uuid())
        steps = self.create_plan_steps(goal)
        return Plan(
            id=plan_id,
            goal_id=goal.id,
            steps=steps,
            symbolic_plan=self.create_symbolic_plan(goal),
            llm_plan=self.create_llm_plan(goal),
            is_completed=False
        )

    def create_plan_steps(self, goal: Goal) -> List[PlanStep]:
        """Create a list of plan steps to achieve the goal."""
        # Implement step creation logic
        return [
            PlanStep(id=str(UUID.uuid()), description=f"Step 1 to achieve {goal.description}"),
            PlanStep(id=str(UUID.uuid()), description=f"Step 2 to achieve {goal.description}"),
            PlanStep(id=str(UUID.uuid()), description=f"Step 3 to achieve {goal.description}")
        ]

    def create_symbolic_plan(self, goal: Goal) -> Dict:
        """Create a symbolic plan for the goal."""
        # Implement symbolic planning logic
        return {}  # Placeholder

    def create_llm_plan(self, goal: Goal) -> Dict:
        """Create an LLM-based plan for the goal."""
        # Implement LLM-based planning logic
        return {}  # Placeholder

    def execute(self):
        """Execute plans to achieve goals."""
        for plan in self.plans:
            if not plan.is_completed:
                self.execute_plan(plan)

    def execute_plan(self, plan: Plan):
        """Execute a single plan."""
        while not plan.is_completed and (next_step := plan.get_next_step()):
            if self.execute_step(next_step):
                plan.update_step_status(next_step.id, True)
            else:
                self.replan(plan)
                break
        plan.check_completion()

        if plan.is_completed and (goal := next((g for g in self.goals if g.id == plan.goal_id), None)):
            goal.update_status(True)

    def execute_step(self, step: PlanStep) -> bool:
        """Execute a single step of the plan."""
        # Implement step execution logic
        print(f"Executing step: {step.description}")
        return True  # Placeholder

    def replan(self, plan: Plan):
        """Replan when a step fails."""
        # Implement replanning logic
        print(f"Replanning for goal: {plan.goal_id}")        

ProactiveAgent.model_rebuild()

class ReactiveAgent(Agent):
    stimulus_response_rules: List[Dict[str, Any]] = Field(default_factory=list, description="List of stimulus-response rules")

    def add_rule(self, stimulus: str, response: str):
        """Add a new stimulus-response rule."""
        self.stimulus_response_rules.append({"stimulus": stimulus, "response": response})

    def perceive(self):
        """Perceive the environment and react based on stimulus-response rules."""
        for belief in self.beliefs:
            for rule in self.stimulus_response_rules:
                if rule["stimulus"] in belief.description and self.can_execute_action(rule["response"]):
                    self.execute_action(rule["response"])
                    break  # Stop after executing the highest priority matching rule


    def can_execute_action(self, action: str) -> bool:
        """Check if the agent has the necessary resources to execute the action."""
        # Implement resource checking logic
        return True  # Placeholder
    
    
    def execute_action(self, action: str):
        """Execute a reactive action."""
        # Implement action execution logic
        print(f"Executing reactive action: {action}")
        self.update_environment(action)

    def update_environment(self, action: str):
        """Update the environment based on the executed action."""
        # Implement environment update logic
        pass 

ReactiveAgent.model_rebuild()
