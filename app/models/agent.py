from pydantic import BaseModel, ConfigDict
from typing import List, Dict

class Belief(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: str
    content: str

class Desire(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    description: str
    priority: int

class Intention(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    desire_id: str
    plan_id: str

class Agent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str
    name: str
    beliefs: List[Belief] = []
    desires: List[Desire] = []
    intentions: List[Intention] = []
    goals: List[str] = []
    resources: Dict[str, float] = {}

    def add_belief(self, belief: Belief):
        self.beliefs.append(belief)

    def remove_belief(self, belief_id: str):
        self.beliefs = [b for b in self.beliefs if b.id != belief_id]

    def add_desire(self, desire: Desire):
        self.desires.append(desire)

    def remove_desire(self, desire_id: str):
        self.desires = [d for d in self.desires if d.id != desire_id]

    def add_intention(self, intention: Intention):
        self.intentions.append(intention)

    def remove_intention(self, intention_id: str):
        self.intentions = [i for i in self.intentions if i.id != intention_id]

    def add_goal(self, goal_id: str):
        self.goals.append(goal_id)

    def remove_goal(self, goal_id: str):
        self.goals.remove(goal_id)

    def update_resource(self, resource_name: str, value: float):
        self.resources[resource_name] = value