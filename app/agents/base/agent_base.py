from __future__ import annotations

from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from app.agents.base.base_models import (BaseAction, BaseBelief, BaseDesire, BaseGoal,
                              BaseIntention, BasePlan)
from models.utils.type_definitions import *
from pydantic import BaseModel, ConfigDict, Field

from app.models.message import ACLMessage, Message, Performative


class AgentBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    """
    Base class for all agents in the system, incorporating BDI attributes and core functionalities.

    Attributes:
        agent_id (UUID): Unique identifier for the agent.
        name (str): Name of the agent.
        beliefs (List[BaseBelief]): Current beliefs of the agent.
        desires (List[BaseDesire]): Current desires of the agent.
        intentions (List[BaseIntention]): Current intentions of the agent.
        available_actions (List[BaseAction]): Actions available to the agent.
        goals (List[BaseGoal]): Current goals of the agent.
        plans (List[BasePlan]): Current plans of the agent.
        resources (Dict[str, float]): Resources available to the agent.
    """

    agent_id: UUID = Field(default_factory=uuid4, description="Unique identifier for the agent")
    name: str = Field(..., description="Name of the agent")
    beliefs: List[BaseBelief] = Field(default_factory=list, description="Current beliefs of the agent")
    desires: List[BaseDesire] = Field(default_factory=list, description="Current desires of the agent")
    intentions: List[BaseIntention] = Field(default_factory=list, description="Current intentions of the agent")
    available_actions: List[BaseAction] = Field(default_factory=list, description="Actions available to the agent")
    goals: List[BaseGoal] = Field(default_factory=list, description="Current goals of the agent")
    plans: List[BasePlan] = Field(default_factory=list, description="Current plans of the agent")
    resources: Dict[str, float] = Field(default_factory=dict, description="Resources available to the agent")

    def perceive(self, environment: Dict[str, Any]):
        """
        Update the agent's beliefs based on environmental perception.

        Args:
            environment (Dict[str, Any]): Current state of the environment.
        """
        for key, value in environment.items():
            self.update_belief(key, value)

    def deliberate(self):
        """
        Deliberate on current beliefs and desires to form intentions.
        """
        for desire in self.desires:
            if self.is_achievable(desire) and not self.has_intention(desire):
                self.add_intention(desire)

    def plan(self):
        """
        Generate plans for current intentions.
        """
        for intention in self.intentions:
            if not intention.has_plan() and (new_plan := self.generate_plan(intention.goal)):
                intention.set_plan(new_plan)
                self.plans.append(new_plan)

    def execute(self):
        """
        Execute actions based on current plans and intentions.
        """
        for intention in self.intentions:
            if intention.has_plan() and (action := intention.get_next_action()):
                self.execute_action(action)

    def communicate(self, message: Dict[str, Any], receiver_id: UUID):
        """
        Send a message to another agent using the Agent Communication Language (ACL).

        Args:
            message (Dict[str, Any]): Content of the message.
            receiver_id (UUID): ID of the receiving agent.
        """
        acl_message = ACLMessage(
            sender_id=self.agent_id,
            receiver_id=receiver_id,
            performative=Performative.INFORM,  # Default performative, can be changed as needed
            content=message,
            conversation_id=uuid4(),  # Generate a new conversation ID
            language="English",  # Default language, can be changed as needed
            ontology=None,  # Can be set if using a specific ontology
            protocol=None  # Can be set if following a specific protocol
        )
        
        # Convert ACLMessage to a standard Message object
        standard_message = acl_message.to_message()
        
        # Send the message (implementation depends on the communication infrastructure)
        self._send_message(standard_message)

    def _send_message(self, message: Message):
        """
        Private method to send a message. This method should be implemented
        according to the specific communication infrastructure being used.
        """
        # Implementation depends on the communication infrastructure
        pass

    def update_belief(self, key: str, value: Any, certainty: float = 1.0):
        """
        Update or add a belief.

        Args:
            key (str): Key of the belief.
            value (Any): Value of the belief.
            certainty (float): Certainty of the belief (0.0 to 1.0).
        """
        if existing_belief := next((b for b in self.beliefs if b.key == key), None):
            existing_belief.update(value, certainty)
        else:
            self.beliefs.append(BaseBelief(key=key, value=value, certainty=certainty))

    def add_desire(self, description: str, priority: float):
        """
        Add a new desire.

        Args:
            description (str): Description of the desire.
            priority (float): Priority of the desire.
        """
        self.desires.append(BaseDesire(description=description, priority=priority))

    def add_intention(self, desire: BaseDesire):
        """
        Add a new intention based on a desire.

        Args:
            desire (BaseDesire): The desire to form an intention from.
        """
        self.intentions.append(BaseIntention(goal=BaseGoal(description=desire.description, priority=desire.priority)))

    def is_achievable(self, desire: BaseDesire) -> bool:
        """
        Check if a desire is achievable given current beliefs and resources.

        Args:
            desire (BaseDesire): The desire to check.

        Returns:
            bool: True if achievable, False otherwise.
        """
        # Implementation depends on specific criteria for achievability
        return True

    def has_intention(self, desire: BaseDesire) -> bool:
        """
        Check if an intention already exists for a given desire.

        Args:
            desire (BaseDesire): The desire to check.

        Returns:
            bool: True if an intention exists, False otherwise.
        """
        return any(i.goal.description == desire.description for i in self.intentions)

    def generate_plan(self, goal: BaseGoal) -> Optional[BasePlan]:
        """
        Generate a plan to achieve a given goal.

        Args:
            goal (BaseGoal): The goal to plan for.

        Returns:
            Optional[BasePlan]: A plan if one can be generated, None otherwise.
        """
        from app.services.planning_service import PlanningService
        from app.models.agent.goal import Goal
        from app.models.agent.plan import Plan

        # Convert BaseGoal to Goal
        goal_obj = Goal(id=str(goal.id), description=goal.description, priority=goal.priority)

        # Get the current state of the agent
        current_state = {belief.key: belief.value for belief in self.beliefs}

        # Initialize PlanningService
        planning_service = PlanningService({})  # Empty dict as domain_knowledge, adjust as needed

        try:
            # Generate plan using PlanningService
            plan = planning_service.generate_plan(goal_obj, current_state)

            # Convert Plan to BasePlan and return
            return BasePlan(
                id=plan.id,
                goal_id=plan.goal_id,
                steps=[step.description for step in plan.steps],
            )
        except Exception as e:
            print(f"Error generating plan: {str(e)}")
            return None

    def execute_action(self, action: BaseAction):
        """
        Execute a given action.

        Args:
            action (BaseAction): The action to execute.
        """
        action.execute(self.get_belief, self.update_belief)

    def get_belief(self, key: str) -> Any:
        """
        Get the value of a belief.

        Args:
            key (str): The key of the belief.

        Returns:
            Any: The value of the belief, or None if not found.
        """
        belief = next((b for b in self.beliefs if b.key == key), None)
        return belief.value if belief else None

    def react(self, stimulus: str):
        """
        React to a given stimulus based on predefined rules.

        Args:
            stimulus (str): The stimulus to react to.
        """
        # Define reactive behavior rules
        reactive_rules = {
            "danger": self.handle_danger,
            "opportunity": self.handle_opportunity,
            "communication": self.handle_communication,
            # Add more rules as needed
        }

        # Check if the stimulus matches any predefined rule
        for trigger, action in reactive_rules.items():
            if trigger in stimulus.lower():
                action(stimulus)
                break
        else:
            print(f"No reactive rule defined for stimulus: {stimulus}")

    def handle_danger(self, stimulus: str):
        print(f"Danger detected: {stimulus}")
        # Implement danger response logic here
        self.update_belief("danger_level", "high")
        self.add_goal("Ensure safety", priority=10)
        if emergency_action := next((action for action in self.available_actions if action.name == "emergency_response"), None):
            self.execute_action(emergency_action)
        else:
            print("No emergency response action available")

    def handle_opportunity(self, stimulus: str):
        print(f"Opportunity detected: {stimulus}")
        # Implement opportunity response logic here
        self.update_belief("opportunity_available", True)
        self.add_goal("Exploit opportunity", priority=8)
        if opportunity_action := next((action for action in self.available_actions if action.name == "seize_opportunity"), None):
            self.execute_action(opportunity_action)
        else:
            print("No action available to seize opportunity")

    def handle_communication(self, stimulus: str):
        print(f"Communication received: {stimulus}")
        # Implement communication handling logic here
        message = ACLMessage.parse_raw(stimulus)
        if message.performative == Performative.REQUEST:
            self.add_goal(f"Respond to request: {message.content}", priority=5)
        elif message.performative == Performative.INFORM:
            self.update_belief(f"info_from_{message.sender}", message.content)
        self.add_intention(BaseIntention(goal_id="process_communication"))

    def add_goal(self, description: str, priority: float):
        """
        Add a new goal.

        Args:
            description (str): Description of the goal.
            priority (float): Priority of the goal.
        """
        self.goals.append(BaseGoal(description=description, priority=priority))

    def add_action(self, action: BaseAction):
        """
        Add a new available action.

        Args:
            action (BaseAction): The action to add.
        """
        self.available_actions.append(action)

    def update_resources(self, resource: str, amount: float):
        """
        Update the amount of a resource.

        Args:
            resource (str): The resource to update.
            amount (float): The new amount of the resource.
        """
        self.resources[resource] = amount

AgentBase.model_rebuild()