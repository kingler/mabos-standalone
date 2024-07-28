from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from uuid import UUID, uuid4
from .type_definitions import *

class AgentBase(BaseModel):
    agent_id: UUID = Field(default_factory=uuid4, description="Unique identifier for the agent")
    name: str = Field(..., description="Name of the agent")
    resources: Dict[str, float] = Field(default_factory=dict, description="Resources available to the agent")
    beliefs: List[BeliefType] = Field(default_factory=list, description="Current beliefs of the agent")
    desires: List[DesireType] = Field(default_factory=list, description="Current desires of the agent")
    intentions: List[IntentionType] = Field(default_factory=list, description="Current intentions of the agent")
    available_actions: List[ActionType] = Field(default_factory=list, description="Actions available to the agent")
    goals: List[GoalType] = Field(default_factory=list, description="Current goals of the agent")
    plans: List[PlanType] = Field(default_factory=list, description="Current plans of the agent")

class BaseBelief(BaseModel):
    key: str = Field(..., description="The key or description of the belief")
    value: Any = Field(..., description="The value associated with the belief")
    certainty: float = Field(..., ge=0, le=1, description="Certainty level of the belief (0-1)")
    agent: AgentBaseType = Field(..., description="The agent holding this belief")

class BaseDesire(BaseModel):
    description: str = Field(..., description="Description of the desire")
    priority: float = Field(..., description="Priority of the desire")

class BaseIntention(BaseModel):
    goal_id: str = Field(..., description="ID of the associated goal")

class BaseGoal(BaseModel):
    id: str = Field(..., description="Unique identifier for the goal")
    description: str = Field(..., description="Description of the goal")
    priority: float = Field(..., description="Priority of the goal")

class BasePlan(BaseModel):
    id: str = Field(..., description="Unique identifier for the plan")
    goal_id: str = Field(..., description="ID of the associated goal")
    steps: List[str] = Field(default_factory=list, description="Steps of the plan")

class BaseAction(BaseModel):
    name: str = Field(..., description="Name of the action")
    description: str = Field(..., description="Description of the action")