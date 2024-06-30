from fastapi import APIRouter, HTTPException
from typing import List
from app.models.agent import Agent, Belief, Desire, Intention
from app.services.agent_service import AgentService

router = APIRouter()
agent_service = AgentService()

@router.post("/agents/", response_model=Agent)
async def create_agent(name: str):
    return agent_service.create_agent(name)

@router.get("/agents/{agent_id}", response_model=Agent)
async def get_agent(agent_id: str):
    agent = agent_service.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.get("/agents/", response_model=List[Agent])
async def list_agents():
    return agent_service.list_agents()

@router.post("/agents/{agent_id}/beliefs", response_model=Agent)
async def add_belief(agent_id: str, belief: Belief):
    agent = agent_service.add_belief(agent_id, belief)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.post("/agents/{agent_id}/desires", response_model=Agent)
async def add_desire(agent_id: str, desire: Desire):
    agent = agent_service.add_desire(agent_id, desire)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.post("/agents/{agent_id}/intentions", response_model=Agent)
async def add_intention(agent_id: str, intention: Intention):
    agent = agent_service.add_intention(agent_id, intention)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent