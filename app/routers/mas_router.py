from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from app.models.agent import Agent
from app.services.mas_services import MASService
router = APIRouter()

def get_mas_service():
    return MASService()

@router.post("/mas/agents/", response_model=Agent)
async def add_agent(agent: Agent, mas_service: MASService = Depends(get_mas_service)):
    return mas_service.add_agent(agent)

@router.get("/mas/agents/{agent_id}", response_model=Agent)
async def get_agent(agent_id: UUID, mas_service: MASService = Depends(get_mas_service)):
    agent = mas_service.get_agent(agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.delete("/mas/agents/{agent_id}")
async def remove_agent(agent_id: UUID, mas_service: MASService = Depends(get_mas_service)):
    if not (success := mas_service.remove_agent(agent_id)):
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"message": "Agent removed successfully"}

@router.get("/mas/agents/", response_model=List[Agent])
async def list_agents(mas_service: MASService = Depends(get_mas_service)):
    return mas_service.list_agents()

@router.post("/mas/messages/")
async def send_message(sender_id: UUID, receiver_id: UUID, content: str, mas_service: MASService = Depends(get_mas_service)):
    mas_service.send_message(sender_id, receiver_id, content)
    return {"message": "Message sent successfully"}

@router.post("/mas/step/")
async def step_mas(mas_service: MASService = Depends(get_mas_service)):
    mas_service.step()
    return {"message": "MAS stepped successfully"}

@router.post("/mas/run/")
async def run_mas(steps: int, mas_service: MASService = Depends(get_mas_service)):
    mas_service.run(steps)
    return {"message": f"MAS ran for {steps} steps"}