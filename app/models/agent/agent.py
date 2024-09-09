# Correct placement of __future__ import
from __future__ import annotations

# Now other imports
from typing import TYPE_CHECKING, Any, Dict, List
from uuid import UUID

from durable.lang import post
from pydantic import BaseModel, ConfigDict, Field, field_validator

from .action import Action
from .agent_role import AgentRole  # Consider moving this import
from .belief import Belief
from .desire import Desire
from .goal import Goal
from .intention import Intention
from .plan import Plan, PlanStep

if TYPE_CHECKING:
    from app.models.rules.rules_engine import RuleEngine

class Agent(BaseModel):
    def __init__(self, agent_id: str, name: str, api_key: str, llm_service: Any, agent_communication_service: Any):
        self.agent_id = agent_id
        self.name = name
        self.api_key = api_key
        self.llm_service = llm_service
        self.agent_communication_service = agent_communication_service
        
    def initialize_rule_engine(self):
        from app.models.rules.rules_engine import RuleEngine
        self.rule_engine = RuleEngine()
    
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    agent_id: str = Field(..., description="The unique identifier of the agent")
    name: str = Field(..., description="The name of the agent")
    beliefs: List['Belief'] = Field(default_factory=list, description="The agent's current beliefs about the world")
    desires: List['Desire'] = Field(default_factory=list, description="The agent's current desires")
    intentions: List['Intention'] = Field(default_factory=list, description="The agent's current intentions")
    available_actions: List['Action'] = Field(default_factory=list, description="Actions available to the agent")
    roles: List['AgentRole'] = Field(default_factory=list, description="Roles assigned to the agent")

    @field_validator('agent_type', check_fields=False)
    def validate_agent_type(cls, value):
        allowed_types = ['reactive', 'deliberative', 'hybrid']
        if value not in allowed_types:
            raise ValueError(f'Agent type must be one of {allowed_types}')
        return value

    def act(self):
        for intention in self.intentions:
            if intention.goal.description == 'process_orders':
                for order_id in self.beliefs.get('pending_orders', []):
                    self.post_fact({'subject': 'order', 'action': 'process', 'order_id': order_id})

    def add_belief(self, belief: 'Belief'):
        self.beliefs.append(belief)

    def remove_belief(self, belief: 'Belief'):
        self.beliefs.remove(belief)

    def add_desire(self, desire: 'Desire'):
        self.desires.append(desire)

    def remove_desire(self, desire: 'Desire'):
        self.desires.remove(desire)

    def add_intention(self, intention: 'Intention'):
        self.intentions.append(intention)

    def remove_intention(self, intention: 'Intention'):
        self.intentions.remove(intention)

    def add_action(self, action: 'Action'):
        self.available_actions.append(action)

    def remove_action(self, action: 'Action'):
        self.available_actions.remove(action)

    def deliberate(self):
        active_desires = [d for d in self.desires if d.status == "active"]
        active_desires.sort(key=lambda d: d.priority, reverse=True)

        if active_desires and (selected_desire := active_desires[0]):
            if all(i.goal != selected_desire for i in self.intentions):
                self.add_intention(Intention(goal=selected_desire))

    def plan(self):
        for intention in self.intentions:
            if intention.status == "active":
                if applicable_actions := [
                    action for action in self.available_actions 
                    if action.is_applicable(lambda key: next((b.certainty for b in self.beliefs if b.description == key), None))
                ]:
                    selected_action = applicable_actions[0]
                    if selected_action.is_completed(lambda key: next((b.certainty for b in self.beliefs if b.description == key), None)):
                        intention.complete_intention()
                    else:
                        intention.actions.append(selected_action)
                else:
                    intention.suspend_intention()

    def execute(self):
        for intention in self.intentions:
            for action in intention.actions:
                action.execute(
                    get_belief=lambda key: next((b.certainty for b in self.beliefs if b.description == key), None),
                    set_belief=lambda key, value: self.add_belief(Belief(description=key, certainty=value))
                )

    def perceive(self, observations):
        self.current_state = observations
        self.update_beliefs(self.current_state)

    def update_beliefs(self, current_state):
        for key, value in current_state.items():
            if belief := next((b for b in self.beliefs if b.name == key), None):
                belief.value = value
            else:
                self.beliefs.append(Belief(name=key, value=value))

    def decide(self):
        return self.choose_action(self.current_state)

# Example of model rebuild
Agent.model_rebuild()
