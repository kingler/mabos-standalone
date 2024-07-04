from typing import List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field, field_validator

from .belief import Belief
from .desire import Desire
from .intention import Intention
from .action import Action
from .goal import Goal
from .plan import Plan, PlanStep


class Agent(BaseModel):
    """
    Base class for all agents.

    Attributes:
        agent_id (str): The unique identifier of the agent.
        name (str): The name of the agent.
        beliefs (List[Belief]): The agent's current beliefs about the world.
        desires (List[Desire]): The agent's current desires.
        intentions (List[Intention]): The agent's current intentions.
        available_actions (List[Action]): Actions available to the agent.
    """
    agent_id: str = Field(..., description="The unique identifier of the agent")
    name: str = Field(..., description="The name of the agent")
    beliefs: List[Belief] = Field(default_factory=list, description="The agent's current beliefs about the world")
    desires: List[Desire] = Field(default_factory=list, description="The agent's current desires")
    intentions: List[Intention] = Field(default_factory=list, description="The agent's current intentions")
    available_actions: List[Action] = Field(default_factory=list, description="Actions available to the agent")

    @field_validator('agent_type', check_fields=False)
    def validate_agent_type(cls, value):
        allowed_types = ['reactive', 'deliberative', 'hybrid']
        if value not in allowed_types:
            raise ValueError(f'Agent type must be one of {allowed_types}')
        return value

    def add_belief(self, belief: Belief):
        """
        Add a new belief to the agent's beliefs.

        Args:
            belief (Belief): The belief to add.
        """
        self.beliefs.append(belief)

    def remove_belief(self, belief: Belief):
        """
        Remove a belief from the agent's beliefs.

        Args:
            belief (Belief): The belief to remove.
        """
        self.beliefs.remove(belief)

    def add_desire(self, desire: Desire):
        """
        Add a new desire to the agent's desires.

        Args:
            desire (Desire): The desire to add.
        """
        self.desires.append(desire)

    def remove_desire(self, desire: Desire):
        """
        Remove a desire from the agent's desires.

        Args:
            desire (Desire): The desire to remove.
        """
        self.desires.remove(desire)

    def add_intention(self, intention: Intention):
        """
        Add a new intention to the agent's intentions.

        Args:
            intention (Intention): The intention to add.
        """
        self.intentions.append(intention)

    def remove_intention(self, intention: Intention):
        """
        Remove an intention from the agent's intentions.

        Args:
            intention (Intention): The intention to remove.
        """
        self.intentions.remove(intention)

    def add_action(self, action: Action):
        """
        Add a new action to the agent's available actions.

        Args:
            action (Action): The action to add.
        """
        self.available_actions.append(action)

    def remove_action(self, action: Action):
        """
        Remove an action from the agent's available actions.

        Args:
            action (Action): The action to remove.
        """
        self.available_actions.remove(action)

    def deliberate(self):
        """
        Deliberate on the agent's desires and create new intentions.
        """
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
        """
        Plan actions for active intentions.
        """
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
        """
        Execute actions for active intentions.
        """
        for intention in self.intentions:
            for action in intention.actions:
                action.execute(
                    get_belief=lambda key: next((b.certainty for b in self.beliefs if b.description == key), None),
                    set_belief=lambda key, value: self.add_belief(Belief(description=key, certainty=value))
                )

    def revise_beliefs(self, new_belief: Belief):
        """
        Revise beliefs based on new information.

        Args:
            new_belief (Belief): The new belief to revise with.
        """
        if existing_belief := next((b for b in self.beliefs if b.description == new_belief.description), None):
            existing_belief.update(new_belief)
        else:
            self.add_belief(new_belief)

    def select_desires(self):
        """
        Select desires based on current beliefs and intentions.

        Returns:
            List[Desire]: The selected desires.
        """
        return [d for d in self.desires if self.is_desire_relevant(d)]

    def is_desire_relevant(self, desire: Desire) -> bool:
        """
        Check if a desire is relevant given current beliefs and intentions.

        Args:
            desire (Desire): The desire to check for relevance.

        Returns:
            bool: True if the desire is relevant, False otherwise.
        """
        # Implement relevance checking logic based on beliefs and intentions
        for belief in self.beliefs:
            if belief.description in desire.preconditions and belief.certainty < desire.preconditions[belief.description]:
                return False
        for intention in self.intentions:
            if intention.goal == desire:
                return False
        return True

    def commit_to_intention(self, intention: Intention):
        """
        Commit to an intention, possibly dropping conflicting intentions.

        Args:
            intention (Intention): The intention to commit to.
        """
        conflicting_intentions = [i for i in self.intentions if self.are_intentions_conflicting(i, intention)]
        for conflicting in conflicting_intentions:
            self.drop_intention(conflicting)
        self.add_intention(intention)

    def are_intentions_conflicting(self, intention1: Intention, intention2: Intention) -> bool:
        """
        Check if two intentions are conflicting.

        Args:
            intention1 (Intention): The first intention to check.
            intention2 (Intention): The second intention to check.

        Returns:
            bool: True if the intentions are conflicting, False otherwise.
        """
        # Implement conflict checking logic based on intention goals and resources
        if intention1.goal == intention2.goal:
            return True
        for resource in intention1.required_resources:
            if resource in intention2.required_resources:
                return True
        return False

    def drop_intention(self, intention: Intention):
        """
        Drop an intention and clean up related plans.

        Args:
            intention (Intention): The intention to drop.
        """
        self.intentions.remove(intention)
        self.plans = [p for p in self.plans if p.goal_id != intention.goal.id]

    def update_intention_status(self, intention: Intention, new_status: str):
        """
        Update an intention's status.

        Args:
            intention (Intention): The intention to update.
            new_status (str): The new status to set.
        """
        intention.update_status(new_status)
        
Agent.model_rebuild()

class EnvironmentalAgent(Agent):
    """
    An agent that interacts with the environment.

    Attributes:
        environment_state (Dict[str, Any]): The current state of the environment.
    """
    environment_state: Dict[str, Any] = Field(default_factory=dict, description="The current state of the environment")

    def update_environment_state(self, new_state: Dict[str, Any]):
        """
        Update the agent's perception of the environment state.

        Args:
            new_state (Dict[str, Any]): The new environment state.
        """
        self.environment_state.update(new_state)

    def perceive(self):
        """
        Perceive the environment and update beliefs.
        """
        for key, value in self.environment_state.items():
            self.revise_beliefs(Belief(description=f"{key}: {value}", certainty=1.0))

    def act(self):
        """
        Perform actions based on the current environment state.
        """
        # Implement environment-specific actions based on beliefs and intentions
        for intention in self.intentions:
            if intention.status == "active":
                for action in intention.actions:
                    if action.is_applicable(lambda key: next((b.certainty for b in self.beliefs if b.description == key), None)):
                        action.execute(
                            get_belief=lambda key: next((b.certainty for b in self.beliefs if b.description == key), None),
                            set_belief=lambda key, value: self.revise_beliefs(Belief(description=key, certainty=value))
                        )
                        break

EnvironmentalAgent.model_rebuild()        
        
class ProactiveAgent(Agent):
    """
    An agent that proactively pursues its goals.

    Attributes:
        goals (List[Goal]): List of agent's goals.
        plans (List[Plan]): List of agent's plans.
        resources (Dict[str, float]): Agent's resources.
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
                self.commit_to_intention(Intention(goal=goal))

    def has_resources_for_goal(self, goal: Goal) -> bool:
        """
        Check if the agent has the necessary resources for the goal.

        Args:
            goal (Goal): The goal to check resources for.

        Returns:
            bool: True if the agent has the necessary resources, False otherwise.
        """
        for resource, amount in goal.required_resources.items():
            if self.resources.get(resource, 0) < amount:
                return False
        return True

    def plan(self):
        """
        Generate plans for current intentions.
        """
        for intention in self.intentions:
            if intention.status == "active" and not intention.plan:
                if new_plan := self.generate_plan(intention.goal):
                    intention.plan = new_plan
                    self.plans.append(new_plan)

    def generate_plan(self, goal: Goal) -> Plan:
        """
        Generate a plan to achieve a goal.

        Args:
            goal (Goal): The goal to generate a plan for.

        Returns:
            Plan: The generated plan.
        """
        # Implement a more sophisticated planning algorithm
        # This could involve using a planning library or custom logic
        # For now, we'll return an improved dummy plan
        plan_id = str(UUID.uuid4())
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
        """
        Create a list of plan steps to achieve the goal.

        Args:
            goal (Goal): The goal to create plan steps for.

        Returns:
            List[PlanStep]: The list of plan steps.
        """
        # Implement step creation logic based on goal requirements and available actions
        steps = []
        current_state = {b.description: b.certainty for b in self.beliefs}
        for requirement, value in goal.requirements.items():
            if current_state.get(requirement, 0) < value:
                for action in self.available_actions:
                    if action.is_applicable(lambda key: current_state.get(key, 0)) and action.effects.get(requirement, 0) > 0:
                        steps.append(PlanStep(id=str(UUID.uuid4()), description=action.description))
                        for effect_key, effect_value in action.effects.items():
                            current_state[effect_key] = effect_value
                        break
        return steps

    def create_symbolic_plan(self, goal: Goal) -> Dict:
        """
        Create a symbolic plan for the goal.

        Args:
            goal (Goal): The goal to create a symbolic plan for.

        Returns:
            Dict: The symbolic plan.
        """
        # Implement symbolic planning logic based on goal requirements and available actions
        symbolic_plan = {}
        current_state = {b.description: b.certainty for b in self.beliefs}
        for requirement, value in goal.requirements.items():
            if current_state.get(requirement, 0) < value:
                for action in self.available_actions:
                    if action.is_applicable(lambda key: current_state.get(key, 0)) and action.effects.get(requirement, 0) > 0:
                        symbolic_plan[action.action_id] = {
                            "preconditions": action.preconditions,
                            "effects": action.effects
                        }
                        for effect_key, effect_value in action.effects.items():
                            current_state[effect_key] = effect_value
                        break
        return symbolic_plan

    def create_llm_plan(self, goal: Goal) -> Dict:
        """
        Create an LLM-based plan for the goal.

        Args:
            goal (Goal): The goal to create an LLM-based plan for.

        Returns:
            Dict: The LLM-based plan.
        """
        # Implement LLM-based planning logic based on goal description and requirements
        llm_plan = {
            "goal_description": goal.description,
            "goal_requirements": goal.requirements,
            "plan_steps": [
                {"description": "Step 1 of LLM-based plan"},
                {"description": "Step 2 of LLM-based plan"},
                {"description": "Step 3 of LLM-based plan"}
            ]
        }
        return llm_plan

    def execute(self):
        """
        Execute plans to achieve goals.
        """
        for intention in self.intentions:
            if intention.status == "active" and intention.plan and not intention.plan.is_completed:
                self.execute_plan(intention.plan)

        for plan in self.plans:
            if not plan.is_completed:
                self.execute_plan(plan)

    def execute_plan(self, plan: Plan):
        """
        Execute a single plan.

        Args:
            plan (Plan): The plan to execute.
        """
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
        """
        Execute a single step of the plan.

        Args:
            step (PlanStep): The step to execute.

        Returns:
            bool: True if the step was executed successfully, False otherwise.
        """
        # Implement step execution logic
        print(f"Executing step: {step.description}")
        return True  # Placeholder

    def replan(self, plan: Plan):
        """
        Replan when a step fails.

        Args:
            plan (Plan): The plan that failed.
        """
        # Implement replanning logic
        print(f"Replanning for goal: {plan.goal_id}")        

ProactiveAgent.model_rebuild()

class ReactiveAgent(Agent):
    """
    An agent that reacts to changes in the environment.

    Attributes:
        stimulus_response_rules (List[Dict[str, Any]]): List of stimulus-response rules.
    """
    stimulus_response_rules: List[Dict[str, Any]] = Field(default_factory=list, description="List of stimulus-response rules")

    def add_rule(self, stimulus: str, response: str):
        """
        Add a new stimulus-response rule.

        Args:
            stimulus (str): The stimulus that triggers the rule.
            response (str): The response to execute when the stimulus is triggered.
        """
        self.stimulus_response_rules.append({"stimulus": stimulus, "response": response})

    def perceive(self):
        """
        Perceive the environment and react based on stimulus-response rules.
        """
        for belief in self.beliefs:
            for rule in self.stimulus_response_rules:
                if rule["stimulus"] in belief.description and self.can_execute_action(rule["response"]):
                    self.execute_action(rule["response"])
                    break  # Stop after executing the highest priority matching rule


    def can_execute_action(self, action: str) -> bool:
        """
        Check if the agent has the necessary resources to execute the action.

        Args:
            action (str): The action to check resources for.

        Returns:
            bool: True if the agent has the necessary resources, False otherwise.
        """
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
