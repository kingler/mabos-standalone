"""
Core model definitions for the MABOS system.
Consolidates and unifies various model implementations.
"""
from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ModelType(str, Enum):
    """Types of models supported by the system."""
    UML = "UML"
    BPMN = "BPMN"
    GOAL = "GOAL"
    BDI = "BDI"
    ARCHIMATE = "ARCHIMATE"
    TROPOS = "TROPOS"


class AgentType(str, Enum):
    """Types of agents supported by the system."""
    REACTIVE = "reactive"
    DELIBERATIVE = "deliberative"
    HYBRID = "hybrid"
    BUSINESS = "business"
    ENVIRONMENTAL = "environmental"
    META = "meta"
    UI = "ui"


class BaseAgent(BaseModel):
    """
    Base agent model that serves as the foundation for all agent types.
    Combines functionality from both agent.py and mdd_mas_model.py
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the agent")
    name: str = Field(..., description="Name of the agent")
    type: AgentType = Field(..., description="Type of the agent")
    beliefs: Dict[str, Any] = Field(default_factory=dict, description="Agent's current beliefs about the world")
    desires: List[str] = Field(default_factory=list, description="Agent's current desires")
    intentions: List[str] = Field(default_factory=list, description="Agent's current intentions")
    goals: List[UUID] = Field(default_factory=list, description="Agent's current goals")
    roles: List[str] = Field(default_factory=list, description="Roles assigned to the agent")
    capabilities: List[str] = Field(default_factory=list, description="Agent's capabilities")
    resources: Dict[str, Any] = Field(default_factory=dict, description="Resources available to the agent")
    state: Dict[str, Any] = Field(default_factory=dict, description="Current state of the agent")

    @field_validator('type')
    def validate_agent_type(cls, value):
        if not isinstance(value, AgentType):
            if value not in [t.value for t in AgentType]:
                raise ValueError(f'Agent type must be one of {[t.value for t in AgentType]}')
            return AgentType(value)
        return value


class BaseGoal(BaseModel):
    """Base goal model that represents objectives in the system."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    type: str = Field(default="achievement")
    priority: int = Field(default=1)
    status: str = Field(default="active")
    parent_goal: Optional[UUID] = None
    subgoals: List[UUID] = Field(default_factory=list)
    dependencies: List[UUID] = Field(default_factory=list)
    conditions: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, Any] = Field(default_factory=dict)


class BasePlan(BaseModel):
    """Base plan model that represents action sequences."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    goal_id: UUID
    steps: List[Dict[str, Any]] = Field(default_factory=list)
    status: str = Field(default="pending")
    preconditions: Dict[str, Any] = Field(default_factory=dict)
    postconditions: Dict[str, Any] = Field(default_factory=dict)
    resources: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, Any] = Field(default_factory=dict)


class BaseAction(BaseModel):
    """Base action model that represents atomic operations."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    preconditions: Dict[str, Any] = Field(default_factory=dict)
    effects: Dict[str, Any] = Field(default_factory=dict)
    status: str = Field(default="pending")
    resources: Dict[str, Any] = Field(default_factory=dict)


class BaseModel(BaseModel):
    """Base model that represents different types of models in the system."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: ModelType
    content: Dict[str, Any]
    version: int = Field(default=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    dependencies: List[UUID] = Field(default_factory=list)

    @field_validator('type')
    def validate_model_type(cls, value):
        if not isinstance(value, ModelType):
            if value not in [t.value for t in ModelType]:
                raise ValueError(f'Model type must be one of {[t.value for t in ModelType]}')
            return ModelType(value)
        return value


class BusinessProcess(BaseModel):
    """Model representing business processes."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    bpmn_xml: str
    participants: List[UUID] = Field(default_factory=list)
    steps: List[Dict[str, Any]] = Field(default_factory=list)
    status: str = Field(default="draft")
    metrics: Dict[str, Any] = Field(default_factory=dict)


class Communication(BaseModel):
    """Model representing communication between agents."""
    id: UUID = Field(default_factory=uuid4)
    sender: UUID
    receiver: UUID
    type: str
    content: Any
    timestamp: float
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PerformanceMetrics(BaseModel):
    """Model for tracking system performance metrics."""
    id: UUID = Field(default_factory=uuid4)
    timestamp: float
    agent_count: int
    average_response_time: float
    goals_achieved: int
    resource_utilization: Dict[str, float] = Field(default_factory=dict)
    error_rates: Dict[str, float] = Field(default_factory=dict)
    custom_metrics: Dict[str, Any] = Field(default_factory=dict)


class ModelRepository(BaseModel):
    """Model representing a repository of models."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    models: List[BaseModel] = Field(default_factory=list)
    version_control: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SystemIntegration(BaseModel):
    """Model representing integration with external systems."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    system_type: str
    integration_type: str
    connection_details: Dict[str, Any]
    status: str = Field(default="inactive")
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ReusableComponent(BaseModel):
    """Model representing reusable system components."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    type: str
    description: str
    content: Dict[str, Any]
    version: int = Field(default=1)
    dependencies: List[UUID] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class OnboardingProcess(BaseModel):
    """Model representing the business onboarding process."""
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
    status: str = Field(default="draft")
    metadata: Dict[str, Any] = Field(default_factory=dict)
