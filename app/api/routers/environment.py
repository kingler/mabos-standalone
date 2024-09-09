# app/routers/environment.py

from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.agents.core_agents.environmental_agent import EnvironmentalAgent
from app.models.system.environment import (Environment, EnvironmentCreate,
                                                EnvironmentUpdate)
from app.services.environment_service import EnvironmentService

router = APIRouter()

def get_environment_service():
    return EnvironmentService()

@router.post("/environments", response_model=Environment, status_code=201)
async def create_environment(environment: EnvironmentCreate, environment_service: EnvironmentService = Depends(get_environment_service)):
    return environment_service.create_environment(environment)

@router.get("/environments/{environment_id}", response_model=Environment)
async def get_environment(environment_id: UUID, environment_service: EnvironmentService = Depends(get_environment_service)):
    if environment := environment_service.get_environment(environment_id):
        return environment
    raise HTTPException(status_code=404, detail="Environment not found")

@router.put("/environments/{environment_id}", response_model=Environment)
async def update_environment(environment_id: UUID, environment: EnvironmentUpdate, environment_service: EnvironmentService = Depends(get_environment_service)):
    if updated_environment := environment_service.update_environment(environment_id, environment):
        return updated_environment
    raise HTTPException(status_code=404, detail="Environment not found")

@router.delete("/environments/{environment_id}")
async def delete_environment(environment_id: UUID, environment_service: EnvironmentService = Depends(get_environment_service)):
    if environment_service.delete_environment(environment_id):
        return {"message": "Environment deleted successfully"}
    raise HTTPException(status_code=404, detail="Environment not found")

@router.get("/environments/{environment_id}/agents", response_model=List[EnvironmentalAgent])
async def get_environment_agents(environment_id: UUID, environment_service: EnvironmentService = Depends(get_environment_service)):
    return environment_service.get_environment_agents(environment_id)

@router.put("/environments/{environment_id}/agents/{agent_id}", response_model=EnvironmentalAgent)
async def update_environment_agent_state(environment_id: UUID, agent_id: UUID, new_state: Dict[str, Any], environment_service: EnvironmentService = Depends(get_environment_service)):
    if updated_agent := environment_service.update_environment_agent_state(environment_id, agent_id, new_state):
        return updated_agent
    raise HTTPException(status_code=404, detail="Environmental agent not found")