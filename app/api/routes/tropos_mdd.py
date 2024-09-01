from typing import Any, Dict
from uuid import UUID

from fastapi import APIRouter, Depends
from .mas_router import get_mas_service

from app.core.models.mdd.tropos_mdd_model import (Actor,Contribution, Dependency, Plan,TroposModel)
from app.core.services.mas_services import MASService
from app.core.services.tropos_mdd_services import (TroposMASIntegrationService,TroposModelingService)

router = APIRouter()

def get_tropos_service():
    return TroposModelingService()

def get_tropos_mas_integration_service(
    tropos_service: TroposModelingService = Depends(get_tropos_service),
    mas_service: MASService = Depends(get_mas_service)
):
    return TroposMASIntegrationService(tropos_service, mas_service)

@router.post("/models", response_model=TroposModel)
async def create_tropos_model(
    model: TroposModel,
    service: TroposModelingService = Depends(get_tropos_service)
):
    return await service.create_tropos_model(model)

@router.post("/models/{model_id}/actors", response_model=TroposModel)
async def add_actor(
    model_id: UUID,
    actor: Actor,
    service: TroposModelingService = Depends(get_tropos_service)
):
    return await service.add_actor(model_id, actor)

@router.post("/models/{model_id}/dependencies", response_model=TroposModel)
async def add_dependency(
    model_id: UUID,
    dependency: Dependency,
    service: TroposModelingService = Depends(get_tropos_service)
):
    return await service.add_dependency(model_id, dependency)

@router.post("/models/{model_id}/contributions", response_model=TroposModel)
async def add_contribution(
    model_id: UUID,
    contribution: Contribution,
    service: TroposModelingService = Depends(get_tropos_service)
):
    return await service.add_contribution(model_id, contribution)

@router.post("/models/{model_id}/plans", response_model=TroposModel)
async def create_plan(
    model_id: UUID,
    plan: Plan,
    service: TroposModelingService = Depends(get_tropos_service)
):
    return await service.create_plan(model_id, plan)

@router.post("/integration/tropos-to-mas/{tropos_model_id}")
async def generate_mas_from_tropos(
    tropos_model_id: UUID,
    service: TroposMASIntegrationService = Depends(get_tropos_mas_integration_service)
):
    return await service.generate_mas_from_tropos(tropos_model_id)

@router.post("/integration/mas-to-tropos/{tropos_model_id}/{mas_id}")
async def update_tropos_from_mas(
    tropos_model_id: UUID,
    mas_id: UUID,
    service: TroposMASIntegrationService = Depends(get_tropos_mas_integration_service)
):
    return await service.update_tropos_from_mas(tropos_model_id, mas_id)

@router.post("/integration/align-tropos-togaf/{tropos_model_id}/{ea_id}", response_model=Dict[str, Any])
async def align_tropos_with_togaf(
    tropos_model_id: UUID,
    ea_id: UUID,
    service: TroposMASIntegrationService = Depends(get_tropos_mas_integration_service)
):
    return await service.align_tropos_with_togaf(tropos_model_id, ea_id)