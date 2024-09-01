from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.agent.action import Action
from app.core.services.action_service import ActionService
from app.core.services.agent_service import AgentService

router = APIRouter()

def get_action_service():
    return ActionService()

def get_agent_service():
    return AgentService()

@router.post("/actions/", response_model=Action)
async def create_action(action_data: dict, service: ActionService = Depends(get_action_service)):
    return service.create_action(action_data)

@router.get("/actions/{action_id}", response_model=Action)
async def get_action(action_id: str, service: ActionService = Depends(get_action_service)):
    if action := service.get_action(action_id):
        return action
    raise HTTPException(status_code=404, detail="Action not found")

@router.put("/actions/{action_id}", response_model=Action)
async def update_action(action_id: str, action_data: dict, service: ActionService = Depends(get_action_service)):
    if action := service.update_action(action_id, action_data):
        return action
    raise HTTPException(status_code=404, detail="Action not found")

@router.delete("/actions/{action_id}")
async def delete_action(action_id: str, service: ActionService = Depends(get_action_service)):
    if service.delete_action(action_id):
        return {"message": "Action deleted successfully"}
    raise HTTPException(status_code=404, detail="Action not found")

@router.post("/actions/{action_id}/execute")
async def execute_action(
    action_id: str, 
    agent_id: str, 
    action_service: ActionService = Depends(get_action_service),
    agent_service: AgentService = Depends(get_agent_service)
):
    agent = agent_service.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    if action_service.execute_action(action_id, agent):
        return {"message": "Action executed successfully"}
    raise HTTPException(status_code=400, detail="Failed to execute action")

@router.get("/agents/{agent_id}/available_actions", response_model=List[Action])
async def get_available_actions(
    agent_id: str,
    action_service: ActionService = Depends(get_action_service),
    agent_service: AgentService = Depends(get_agent_service)
):
    agent = agent_service.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    return action_service.get_available_actions(agent)