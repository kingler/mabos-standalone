from typing import List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field, field_validator
from durable.lang import post 
#from app.core.world_model import WorldModel# Import post from durable_rules

from .belief import Belief
from .desire import Desire
from .intention import Intention
from .action import Action
from .goal import Goal
from .plan import Plan, PlanStep
from .agent_role import AgentRole

class Agent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    """
    Base class for all agents.

    Attributes:
        agent_id (str): The unique identifier of the agent.
        name (str): The name of the agent.
        beliefs (List[Belief]): The agent's current beliefs about the world.
        desires (List[Desire]): The agent's current desires.
        intentions (List[Intention]): The agent's current intentions.
        available_actions (List[Action]): Actions available to the agent.
        roles (List[Role]): Roles assigned to the agent.
    """
    agent_id: str = Field(..., description="The unique identifier of the agent")
    name: str = Field(..., description="The name of the agent")
    beliefs: List[Belief] = Field(default_factory=list, description="The agent's current beliefs about the world")
    desires: List[Desire] = Field(default_factory=list, description="The agent's current desires")
    intentions: List[Intention] = Field(default_factory=list, description="The agent's current intentions")
    available_actions: List[Action] = Field(default_factory=list, description="Actions available to the agent")
    roles: List[AgentRole] = Field(default_factory=list, description="Roles assigned to the agent")

    @field_validator('agent_type', check_fields=False)
    def validate_agent_type(cls, value):
        allowed_types = ['reactive', 'deliberative', 'hybrid']
        if value not in allowed_types:
            raise ValueError(f'Agent type must be one of {allowed_types}')
        return value

    def add_role(self, role: AgentRole):
        """
        Add a new role to the agent.

        Args:
            role (AgentRole): The role to add.
        """
        self.roles.append(role)

    def remove_role(self, role: AgentRole):
        """
        Remove a role from the agent.

        Args:
            role (AgentRole): The role to remove.
        """
        self.roles.remove(role)

    def post_fact(self, fact: Dict[str, Any]):
        """
        Post a fact to the rules engine.

        Args:
            fact (Dict[str, Any]): The fact to post.
        """
        post('business', fact)

    def act(self):
        """
        Execute actions based on the agent's intentions.
        """
        for intention in self.intentions:
            if intention.goal.description == 'process_orders':
                for order_id in self.beliefs.get('pending_orders', []):
                    self.post_fact({'subject': 'order', 'action': 'process', 'order_id': order_id})

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


    def perceive(self, observations):
        """
        Perceive the environment and update the agent's beliefs.

        Args:
            observations: The observations from the environment.
        """
        self.current_state = observations
        self.update_beliefs(self.current_state)

    def update_beliefs(self, current_state):
        """
        Update the agent's beliefs based on the current state.

        Args:
            current_state: The current state of the agent.
        """
        for key, value in current_state.items():
            belief = next((b for b in self.beliefs if b.name == key), None)
            if belief:
                belief.value = value
            else:
                self.beliefs.append(Belief(name=key, value=value))

    def decide(self):
        """
        Make a decision based on the current state.

        Returns:
            The action to be taken by the agent.
        """
        action = self.choose_action(self.current_state)
        return action

    def choose_action(self, current_state):
        """
        Choose an action based on the current state.

        Args:
            current_state: The current state of the agent.

        Returns:
            The chosen action.
        """
        # Filter available actions based on the current state
        applicable_actions = [
            action for action in self.available_actions
            if action.is_applicable(current_state)
        ]

        # Evaluate each applicable action based on beliefs, desires, and intentions
        action_scores = []
        for action in applicable_actions:
            score = 0
            for belief in self.beliefs:
                if action.supports_belief(belief):
                    score += belief.certainty
            for desire in self.desires:
                if action.satisfies_desire(desire):
                    score += desire.priority
            for intention in self.intentions:
                if action.fulfills_intention(intention):
                    score += intention.priority
            action_scores.append((action, score))

        # Choose the action with the highest score
        if action_scores:
            chosen_action = max(action_scores, key=lambda x: x[1])[0]
        else:
            # If no applicable action found, choose a default action or do nothing
            chosen_action = None

        return chosen_action
 
        
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
        Perceive the environment and update beliefs based on roles.
        """
        for key, value in self.environment_state.items():
            for role in self.roles:
                if key in role.responsibilities:
                    self.revise_beliefs(Belief(description=f"{key}: {value}", certainty=1.0))

    def act(self):
        """
        Perform actions based on the current environment state and roles.
        """
        for role in self.roles:
            for intention in self.intentions:
                if intention.status == "active" and intention.goal in role.responsibilities:
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
        Deliberate on goals and update intentions based on roles.
        """
        for goal in self.goals:
            if goal.is_achievable(self.beliefs) and self.has_resources_for_goal(goal):
                for role in self.roles:
                    if role.allocate_task(goal):
                        self.commit_to_intention(Intention(goal=goal))
                        break

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
        Generate plans for current intentions based on roles.
        """
        for intention in self.intentions:
            if intention.status == "active" and not intention.plan:
                for role in self.roles:
                    if role.allocate_task(intention.goal):
                        if new_plan := self.generate_plan(intention.goal):
                            intention.plan = new_plan
                            self.plans.append(new_plan)
                        break

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
        # Implement step creation logic based on goal requirements, available actions, and roles
        steps = []
        current_state = {b.description: b.certainty for b in self.beliefs}
        for requirement, value in goal.requirements.items():
            if current_state.get(requirement, 0) < value:
                for role in self.roles:
                    for action in role.available_actions:
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
        # Implement symbolic planning logic based on goal requirements, available actions, and roles
        symbolic_plan = {}
        current_state = {b.description: b.certainty for b in self.beliefs}
        for requirement, value in goal.requirements.items():
            if current_state.get(requirement, 0) < value:
                for role in self.roles:
                    for action in role.available_actions:
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
        # Implement LLM-based planning logic based on goal description, requirements, and roles
        llm_plan = {
            "goal_description": goal.description,
            "goal_requirements": goal.requirements,
            "plan_steps": [],
        }
        for role in self.roles:
            if role.allocate_task(goal):
                llm_plan["plan_steps"].extend([
                    {"description": f"Step 1 of LLM-based plan for role {role.name}"},
                    {"description": f"Step 2 of LLM-based plan for role {role.name}"},
                    {"description": f"Step 3 of LLM-based plan for role {role.name}"}
                ])
        return llm_plan

    def execute(self):
        """
        Execute plans to achieve goals based on roles.
        """
        for intention in self.intentions:
            if intention.status == "active" and intention.plan and not intention.plan.is_completed:
                for role in self.roles:
                    if role.allocate_task(intention.goal):
                        self.execute_plan(intention.plan)
                        break

        for plan in self.plans:
            if not plan.is_completed:
                for role in self.roles:
                    if role.allocate_task(next((g for g in self.goals if g.id == plan.goal_id), None)):
                        self.execute_plan(plan)
                        break

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
        # Implement step execution logic based on roles
        for role in self.roles:
            if step.description in [action.description for action in role.available_actions]:
                print(f"Executing step: {step.description} for role {role.name}")
                return True  # Placeholder
        return False

    def replan(self, plan: Plan):
        """
        Replan when a step fails.

        Args:
            plan (Plan): The plan that failed.
        """
        # Implement replanning logic based on roles
        print(f"Replanning for goal: {plan.goal_id}")
        for role in self.roles:
            if role.allocate_task(next((g for g in self.goals if g.id == plan.goal_id), None)):
                if new_plan := self.generate_plan(next((g for g in self.goals if g.id == plan.goal_id), None)):
                    plan.steps = new_plan.steps
                    plan.symbolic_plan = new_plan.symbolic_plan
                    plan.llm_plan = new_plan.llm_plan
                    plan.is_completed = False
                    print(f"Successfully replanned for goal: {plan.goal_id} using role {role.name}")
                    break
        else:
            print(f"Failed to replan for goal: {plan.goal_id}")

ProactiveAgent.model_rebuild()

class ReactiveAgent(Agent):
    """
    An agent that reacts to changes in the environment.

    Attributes:
        stimulus_response_rules (List[Dict[str, Any]]): List of stimulus-response rules.
    """
    stimulus_response_rules: List[Dict[str, Any]] = Field(default_factory=list, description="List of stimulus-response rules")

    def add_rule(self, stimulus: str, response: str, role: AgentRole):
        """
        Add a new stimulus-response rule.

        Args:
            stimulus (str): The stimulus that triggers the rule.
            response (str): The response to execute when the stimulus is triggered.
            role (AgentRole): The role associated with the rule.
        """
        self.stimulus_response_rules.append({"stimulus": stimulus, "response": response, "role": role})

    def perceive(self):
        """
        Perceive the environment and react based on stimulus-response rules.
        """
        for belief in self.beliefs:
            for rule in self.stimulus_response_rules:
                if rule["stimulus"] in belief.description and self.can_execute_action(rule["response"], rule["role"]):
                    self.execute_action(rule["response"], rule["role"])
                    break  # Stop after executing the highest priority matching rule

    def can_execute_action(self, action: str, role: AgentRole) -> bool:
        """
        Check if the agent has the necessary resources and role to execute the action.

        Args:
            action (str): The action to check resources for.
            role (AgentRole): The role associated with the action.

        Returns:
            bool: True if the agent has the necessary resources and role, False otherwise.
        """
        # Check if the agent has the role
        if role not in self.roles:
            return False
        
        # Check if the agent has the necessary resources to execute the action
        required_resources = self.get_required_resources(action)
        for resource, amount in required_resources.items():
            if self.resources.get(resource, 0) < amount:
                return False
        return True

    def execute_action(self, action: str, role: AgentRole):
        """
        Execute a reactive action based on the associated role.
        
        Args:
            action (str): The action to execute.
            role (AgentRole): The role associated with the action.
        """
        if role.name == "Leader":
            if "coordinate" in action.lower():
                # Coordinate team actions and update environment accordingly
                print(f"Leader coordinating team actions: {action}")
                self.coordinate_team_actions(action)
            elif "strategic" in action.lower():
                # Make strategic decisions and update environment based on the decision
                print(f"Leader making strategic decision: {action}")
                self.make_strategic_decision(action)
        elif role.name == "Worker":
            if "execute" in action.lower():
                # Execute the assigned task and update the environment
                print(f"Worker executing task: {action}")
                self.execute_task(action)
        else:
            print(f"Executing reactive action: {action} for role {role.name}")
            self.update_environment(action, role)

    def update_environment(self, action: str, role: AgentRole):
        """
        Update the environment based on the executed action and role.
        
        Args:
            action (str): The executed action.
            role (AgentRole): The role associated with the action.
        """
        if role.name == "Leader":
            if "coordinate" in action.lower():
                # Coordinate team actions and update environment accordingly
                print(f"Leader coordinating team actions: {action}")
                # Identify the tasks to be coordinated
                tasks = self.identify_tasks()
                
                # Assign tasks to team members based on their roles and capabilities
                task_assignments = self.assign_tasks(tasks)
                
                # Communicate the task assignments to the team members
                self.communicate_task_assignments(task_assignments)
                
                # Monitor the progress of the assigned tasks
                task_progress = self.monitor_task_progress(task_assignments)
                
                # Update the environment based on the task progress
                self.update_environment_with_progress(task_progress)
            elif "strategic" in action.lower():
                # Make strategic decisions and update environment based on the decision
                print(f"Leader making strategic decision: {action}")
                # Gather relevant information for strategic decision-making
                environment_data = self.gather_environment_data()
                team_capabilities = self.assess_team_capabilities()
                
                # Analyze the information to identify strategic opportunities or challenges
                strategic_insights = self.analyze_strategic_situation(environment_data, team_capabilities)
                
                # Generate potential strategic decisions based on the insights
                potential_decisions = self.generate_strategic_decisions(strategic_insights)
                
                # Evaluate the potential decisions and select the best one
                selected_decision = self.evaluate_and_select_decision(potential_decisions)
                
                # Implement the selected strategic decision
                self.implement_strategic_decision(selected_decision)
                
                # Update the environment based on the implemented decision
                self.update_environment_with_strategic_decision(selected_decision)
        elif role.name == "Worker":
            if "execute" in action.lower():
                # Execute the assigned task and update the environment
                print(f"Worker executing task: {action}")
                # Get the assigned task from the worker's task list
                assigned_task = self.get_assigned_task()
                
                if assigned_task:
                    # Execute the assigned task
                    task_result = self.execute_task(assigned_task)
                    
                    # Update the environment based on the task result
                    self.update_environment_with_task_result(task_result)
                    
                    # Remove the completed task from the worker's task list
                    self.remove_completed_task(assigned_task)
                else:
                    print("No assigned task found for the worker.")
            elif "report" in action.lower():
                # Report progress and update the environment with the progress information
                print(f"Worker reporting progress: {action}")
                # Get the worker's progress on the assigned tasks
                task_progress = self.get_task_progress()
                
                # Prepare a progress report
                progress_report = self.prepare_progress_report(task_progress)
                
                # Communicate the progress report to the team leader or manager
                self.communicate_progress_report(progress_report)
                
                # Update the environment with the progress information
                self.update_environment_with_progress(task_progress)
        else:
            print(f"Unknown role: {role.name}. No environment updates performed.")

ReactiveAgent.model_rebuild()
