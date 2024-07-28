from typing import Any, Dict, List
from pydantic import Field
from requests import post
from ..agent import Agent

class BusinessAgent(Agent):
    business_id: str = Field(..., description="The business ID associated with the agent")
    any_field: Any = Field(..., description="A field that can be of any type")
    beliefs: Dict[str, Any] = Field(default_factory=dict, description="The agent's current beliefs")
    desires: List[str] = Field(default_factory=list, description="The agent's current desires")
    intentions: List[str] = Field(default_factory=list, description="The agent's current intentions")

    def update_belief(self, key, value):
        self.beliefs[key] = value

    def add_desire(self, desire):
        self.desires.append(desire)

    def set_intention(self, intention):
        self.intentions.append(intention)

    def act(self):
        for intention in self.intentions:
            if intention == 'process_orders':
                for order_id in self.beliefs.get('pending_orders', []):
                    post(f'http://{self.business_id}/actions', {'subject': 'order', 'action': 'process', 'order_id': order_id})