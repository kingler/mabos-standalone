from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


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

class OnboardingProcess(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    business_name: str
    business_description: str
    industry: str
    target_market: str
    key_stakeholders: List[str]
    business_goals: List[str]
    existing_systems: List[str]
    desired_features: List[str]
    integration_requirements: List[str]
    performance_expectations: Dict[str, Any]
    compliance_requirements: List[str]
    budget_constraints: Optional[float]
    timeline: str
    risk_tolerance: str
    scalability_requirements: str
    data_sources: List[str]
    expected_user_roles: List[str]
    success_criteria: List[str]
    
    def to_business_model(self) -> 'BusinessModel':
        # Convert onboarding data to a business model
        pass
    
    def generate_initial_mas_config(self) -> Dict[str, Any]:
        # Generate initial MAS configuration based on onboarding data
        pass
    
    def identify_required_agent_types(self) -> List[str]:
        # Identify the types of agents needed based on business requirements
        pass
    
    def suggest_knowledge_base_structure(self) -> Dict[str, Any]:
        # Suggest an initial knowledge base structure
        pass