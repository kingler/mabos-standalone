from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from uuid import UUID, uuid4
from enum import Enum

class ActorType(str, Enum):
    AGENT = "Agent"
    ROLE = "Role"
    POSITION = "Position"

class DependencyType(str, Enum):
    GOAL = "Goal"
    SOFTGOAL = "Softgoal"
    TASK = "Task"
    RESOURCE = "Resource"

class Actor(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: ActorType
    goals: List[str] = Field(default_factory=list)
    softgoals: List[str] = Field(default_factory=list)
    tasks: List[str] = Field(default_factory=list)
    resources: List[str] = Field(default_factory=list)

class Dependency(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: DependencyType
    depender: UUID  # Actor ID
    dependee: UUID  # Actor ID

class Contribution(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    from_element: UUID  # Goal, Softgoal, Task, or Resource ID
    to_element: UUID  # Usually a Softgoal ID
    type: str  # e.g., "+", "++", "-", "--", etc.

class Plan(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    actor: UUID  # Actor ID
    subgoals: List[UUID] = Field(default_factory=list)
    subtasks: List[UUID] = Field(default_factory=list)

class TroposModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    actors: List[Actor] = Field(default_factory=list)
    dependencies: List[Dependency] = Field(default_factory=list)
    contributions: List[Contribution] = Field(default_factory=list)
    plans: List[Plan] = Field(default_factory=list)