from __future__ import annotations
from typing import List, Dict, Any, ForwardRef
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict

from app.models.message import ACLMessage, Performative, Message

from .base_models import BaseBelief
from .base_models import BaseDesire
from .base_models import BaseIntention
from .base_models import BaseGoal
from .base_models import BasePlan
from .base_models import BaseAction
from .type_definitions import *

class AgentBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    """
    Base class for all agents in the system, incorporating BDI attributes and core functionalities.

    Attributes:
        agent_id (UUID): Unique identifier for the agent.
        name (str): Name of the agent.
        beliefs (List[Belief]): Current beliefs of the agent.
        desires (List[Desire]): Current desires of the agent.
        intentions (List[Intention]): Current intentions of the agent.
        available_actions (List[Action]): Actions available to the agent.
        goals (List[Goal]): Current goals of the agent.
        plans (List[Plan]): Current plans of the agent.
        resources (Dict[str, float]): Resources available to the agent.
    """

    agent_id: UUID = Field(default_factory=uuid4, description="Unique identifier for the agent")
    name: str = Field(..., description="Name of the agent")
    beliefs: List['Belief'] = Field(default_factory=list, description="Current beliefs of the agent")
    desires: List['Desire'] = Field(default_factory=list, description="Current desires of the agent")
    intentions: List['Intention'] = Field(default_factory=list, description="Current intentions of the agent")
    available_actions: List['Action'] = Field(default_factory=list, description="Actions available to the agent")
    goals: List['Goal'] = Field(default_factory=list, description="Current goals of the agent")
    plans: List['Plan'] = Field(default_factory=list, description="Current plans of the agent")
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
            self.beliefs.append(Belief(key=key, value=value, certainty=certainty))

    def add_desire(self, description: str, priority: float):
        """
        Add a new desire.

        Args:
            description (str): Description of the desire.
            priority (float): Priority of the desire.
        """
        self.desires.append(Desire(description=description, priority=priority))

    def add_intention(self, desire: Desire):
        """
        Add a new intention based on a desire.

        Args:
            desire (Desire): The desire to form an intention from.
        """
        self.intentions.append(Intention(goal=Goal(description=desire.description, priority=desire.priority)))

    def is_achievable(self, desire: Desire) -> bool:
        """
        Check if a desire is achievable given current beliefs and resources.

        Args:
            desire (Desire): The desire to check.

        Returns:
            bool: True if achievable, False otherwise.
        """
        # Implementation depends on specific criteria for achievability
        return True

    def has_intention(self, desire: Desire) -> bool:
        """
        Check if an intention already exists for a given desire.

        Args:
            desire (Desire): The desire to check.

        Returns:
            bool: True if an intention exists, False otherwise.
        """
        return any(i.goal.description == desire.description for i in self.intentions)

    def generate_plan(self, goal: Goal) -> Optional[Plan]:
        """
        Generate a plan to achieve a given goal.

        Args:
            goal (Goal): The goal to plan for.

        Returns:
            Optional[Plan]: A plan if one can be generated, None otherwise.
        """
        # Implementation depends on planning algorithm
        return None

    def execute_action(self, action: Action):
        """
        Execute a given action.

        Args:
            action (Action): The action to execute.
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
        # Implementation depends on reactive behavior rules

    def add_goal(self, description: str, priority: float):
        """
        Add a new goal.

        Args:
            description (str): Description of the goal.
            priority (float): Priority of the goal.
        """
        self.goals.append(Goal(description=description, priority=priority))

    def add_action(self, action: Action):
        """
        Add a new available action.

        Args:
            action (Action): The action to add.
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