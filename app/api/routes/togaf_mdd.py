from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.mdd.mdd_mas_model import Model
from app.core.models.mdd.togaf_mdd_models import (ArchitectureRequirement,
                                                  ArchitectureRoadmap,
                                                  ArchitectureView,
                                                  ArchitectureViewpoint,
                                                  BusinessService,
                                                  EnterpriseArchitecture,  # Keep this import
                                                  TechnologyService)
from app.core.services.mdd_mas_services import (ModelingService,
                                                get_modeling_service)
from app.core.services.togaf_mdd_services import (
    ArchitectureRequirementService, ArchitectureRoadmapService,
    EnterpriseArchitectureService, TOGAFIntegrationService)

router = APIRouter()

def get_ea_service():
    return EnterpriseArchitectureService()

def get_req_service():
    return ArchitectureRequirementService()

def get_roadmap_service():
    return ArchitectureRoadmapService()

def get_togaf_integration_service(
    ea_service: EnterpriseArchitectureService = Depends(get_ea_service),
    modeling_service: ModelingService = Depends(get_modeling_service)
):
    return TOGAFIntegrationService(ea_service, modeling_service)

@router.post("/enterprise-architectures", response_model=EnterpriseArchitecture)
async def create_enterprise_architecture(
    ea: EnterpriseArchitecture,
    service: EnterpriseArchitectureService = Depends(get_ea_service)
):
    return await service.create_enterprise_architecture(ea)

@router.post("/enterprise-architectures/{ea_id}/business-services", response_model=EnterpriseArchitecture)
async def add_business_service(
    ea_id: UUID,
    service: BusinessService,
    ea_service: EnterpriseArchitectureService = Depends(get_ea_service)
):
    return await ea_service.add_business_service(ea_id, service)

@router.post("/enterprise-architectures/{ea_id}/technology-services", response_model=EnterpriseArchitecture)
async def add_technology_service(
    ea_id: UUID,
    service: TechnologyService,
    ea_service: EnterpriseArchitectureService = Depends(get_ea_service)
):
    return await ea_service.add_technology_service(ea_id, service)

@router.post("/enterprise-architectures/{ea_id}/viewpoints", response_model=ArchitectureViewpoint)
async def create_viewpoint(
    ea_id: UUID,
    viewpoint: ArchitectureViewpoint,
    ea_service: EnterpriseArchitectureService = Depends(get_ea_service)
):
    return await ea_service.create_viewpoint(ea_id, viewpoint)

@router.post("/enterprise-architectures/{ea_id}/views", response_model=ArchitectureView)
async def create_view(
    ea_id: UUID,
    view: ArchitectureView,
    ea_service: EnterpriseArchitectureService = Depends(get_ea_service)
):
    return await ea_service.create_view(ea_id, view)

@router.post("/requirements", response_model=ArchitectureRequirement)
async def create_requirement(
    requirement: ArchitectureRequirement,
    service: ArchitectureRequirementService = Depends(get_req_service)
):
    return await service.create_requirement(requirement)

@router.put("/requirements/{req_id}/status", response_model=ArchitectureRequirement)
async def update_requirement_status(
    req_id: UUID,
    status: str,
    service: ArchitectureRequirementService = Depends(get_req_service)
):
    return await service.update_requirement_status(req_id, status)

@router.post("/roadmaps", response_model=ArchitectureRoadmap)
async def create_roadmap(
    roadmap: ArchitectureRoadmap,
    service: ArchitectureRoadmapService = Depends(get_roadmap_service)
):
    return await service.create_roadmap(roadmap)

@router.post("/roadmaps/{roadmap_id}/milestones", response_model=ArchitectureRoadmap)
async def add_milestone(
    roadmap_id: UUID,
    milestone: Dict[str, Any],
    service: ArchitectureRoadmapService = Depends(get_roadmap_service)
):
    return await service.add_milestone(roadmap_id, milestone)

@router.post("/integration/ea-to-models/{ea_id}", response_model=List[Model])
async def generate_models_from_ea(
    ea_id: UUID,
    service: TOGAFIntegrationService = Depends(get_togaf_integration_service)
):
    return await service.generate_models_from_ea(ea_id)

@router.post("/integration/models-to-ea/{ea_id}", response_model=EnterpriseArchitecture)
async def update_ea_from_models(
    ea_id: UUID,
    model_ids: List[UUID],
    service: TOGAFIntegrationService = Depends(get_togaf_integration_service)
):
    return await service.update_ea_from_models(ea_id, model_ids)

@router.post("/integration/align-agents/{ea_id}", response_model=Dict[UUID, List[UUID]])
async def align_agents_with_business_services(
    ea_id: UUID,
    service: TOGAFIntegrationService = Depends(get_togaf_integration_service)
):
    return await service.align_agents_with_business_services(ea_id)