from pydantic import BaseModel
from typing import List, Dict, Any

class BusinessGoal(BaseModel):
    id: str
    description: str
    priority: int

class BusinessAction(BaseModel):
    id: str
    description: str
    impact: Dict[str, Any]

class BusinessPlan(BaseModel):
    id: str
    name: str
    goals: List[BusinessGoal]
    actions: List[BusinessAction]
    current_state: Dict[str, Any]
    resources: Dict[str, float]