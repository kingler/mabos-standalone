from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ArchitectureLayer(str, Enum):
    BUSINESS = "Business"
    DATA = "Data"
    APPLICATION = "Application"
    TECHNOLOGY = "Technology"

class ArchitectureBuildingBlock(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    layer: ArchitectureLayer

class BusinessService(ArchitectureBuildingBlock):
    processes: List[str] = Field(default_factory=list)
    stakeholders: List[str] = Field(default_factory=list)

class TechnologyService(ArchitectureBuildingBlock):
    infrastructure_components: List[str] = Field(default_factory=list)
    platforms: List[str] = Field(default_factory=list)

class ArchitectureViewpoint(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    stakeholders: List[str] = Field(default_factory=list)
    concerns: List[str] = Field(default_factory=list)

class ArchitectureView(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    viewpoint: UUID
    content: Dict[str, Any] = Field(default_factory=dict)

class EnterpriseArchitecture(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    business_services: List[BusinessService] = Field(default_factory=list)
    technology_services: List[TechnologyService] = Field(default_factory=list)
    viewpoints: List[ArchitectureViewpoint] = Field(default_factory=list)
    views: List[ArchitectureView] = Field(default_factory=list)

class ArchitectureRequirement(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    priority: int
    status: str

class ArchitectureRoadmap(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    milestones: List[Dict[str, Any]] = Field(default_factory=list)
    target_architecture: UUID