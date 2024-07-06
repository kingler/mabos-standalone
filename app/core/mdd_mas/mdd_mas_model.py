from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from uuid import UUID, uuid4
from enum import Enum

class ModelType(str, Enum):
    UML = "UML"
    BPMN = "BPMN"
    GOAL = "GOAL"
    BDI = "BDI"

class Model(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: ModelType
    content: Dict[str, Any]
    version: int = 1

class Agent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    beliefs: Dict[str, Any] = Field(default_factory=dict)
    desires: List[str] = Field(default_factory=list)
    intentions: List[str] = Field(default_factory=list)

class Goal(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    subgoals: List[UUID] = Field(default_factory=list)

class BusinessProcess(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    bpmn_xml: str

class Communication(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    sender: UUID
    receiver: UUID
    content: str

class PerformanceMetrics(BaseModel):
    agent_count: int
    average_response_time: float
    goals_achieved: int

class ModelRepository(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    models: List[Model] = Field(default_factory=list)

class DomainSpecificLanguage(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    grammar: str
    version: str

class BusinessSystemIntegration(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    system_name: str
    integration_type: str
    connection_details: Dict[str, Any]

class ReusableComponent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: str
    content: Dict[str, Any]
    version: int = 1