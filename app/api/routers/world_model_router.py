from typing import Any, Dict
from uuid import UUID

from fastapi import APIRouter, Depends

from app.models.system.world_model import WorldModel
from app.services.world_model_service import WorldModelService

router = APIRouter()

def get_world_model_service():
    world_model = WorldModel()  # You might want to use dependency injection to get a singleton instance
    return WorldModelService(world_model)

@router.get("/state")
async def get_state(service: WorldModelService = Depends(get_world_model_service)):
    return service.get_state()

@router.put("/state")
async def update_state(updates: Dict[str, Any], service: WorldModelService = Depends(get_world_model_service)):
    return service.update_state(updates)

@router.get("/agents")
async def get_agents(service: WorldModelService = Depends(get_world_model_service)):
    return service.get_agents()

@router.post("/agents/{agent_id}")
async def add_agent(agent_id: UUID, agent_data: Dict[str, Any], service: WorldModelService = Depends(get_world_model_service)):
    return service.add_agent(agent_id, agent_data)

@router.put("/agents/{agent_id}")
async def update_agent(agent_id: UUID, updates: Dict[str, Any], service: WorldModelService = Depends(get_world_model_service)):
    return service.update_agent(agent_id, updates)

@router.get("/objects")
async def get_objects(service: WorldModelService = Depends(get_world_model_service)):
    return service.get_objects()

@router.post("/objects/{object_id}")
async def add_object(object_id: str, object_data: Dict[str, Any], service: WorldModelService = Depends(get_world_model_service)):
    return service.add_object(object_id, object_data)

@router.put("/objects/{object_id}")
async def update_object(object_id: str, updates: Dict[str, Any], service: WorldModelService = Depends(get_world_model_service)):
    return service.update_object(object_id, updates)

@router.get("/relationships")
async def get_relationships(service: WorldModelService = Depends(get_world_model_service)):
    return service.get_relationships()

@router.post("/relationships")
async def add_relationship(relationship: Dict[str, Any], service: WorldModelService = Depends(get_world_model_service)):
    return service.add_relationship(relationship)

@router.post("/ontology/query")
async def query_ontology(query: str, service: WorldModelService = Depends(get_world_model_service)):
    return service.query_ontology(query)

@router.post("/ontology/update")
async def update_ontology(new_information: str, service: WorldModelService = Depends(get_world_model_service)):
    return service.update_ontology(new_information)

@router.get("/agents/{agent_id}/view")
async def get_agent_view(agent_id: UUID, service: WorldModelService = Depends(get_world_model_service)):
    return service.get_agent_view(agent_id)