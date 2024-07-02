from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any

from uuid import UUID
from app.models.agent_types import Agent, EnvironmentalAgent, ProactiveAgent, ReactiveAgent
from app.models.belief import Belief
from app.models.desire import Desire
from app.models.intention import Intention
from app.services.agent_service import AgentService
from app.services.environment_service import EnvironmentService
from app.services.strategy_service import StrategyService
from app.services.reactive_service import ReactiveService
from app.exceptions import AgentNotFoundError

router = APIRouter()
agent_service = AgentService()

def get_agent_service():
    return AgentService()

def get_environment_service(agent_service: AgentService = Depends(get_agent_service)):
    return EnvironmentService(agent_service)

def get_strategy_service(agent_service: AgentService = Depends(get_agent_service)):
    return StrategyService(agent_service)

def get_reactive_service(agent_service: AgentService = Depends(get_agent_service)):
    return ReactiveService(agent_service)

def get_agent_or_404(agent_id: UUID, agent_service: AgentService):
    agent = agent_service.get_agent(agent_id)
    if agent is None:
        raise AgentNotFoundError(agent_id)
    return agent

@router.post("/agents/", response_model=Agent)
async def create_agent(name: str):
    return agent_service.create_agent(name)

@router.get("/agents/{agent_id}", response_model=Agent)
async def get_agent(agent_id: str):
    agent = get_agent_or_404(agent_id, agent_service)
    return agent

@router.get("/agents/", response_model=List[Agent])
async def list_agents():
    return agent_service.list_agents()

@router.post("/agents/{agent_id}/beliefs", response_model=Agent)
async def add_belief(agent_id: str, belief: Belief):
    agent = get_agent_or_404(agent_id, agent_service)
    return agent_service.add_belief(agent_id, belief)

@router.post("/agents/{agent_id}/desires", response_model=Agent)
async def add_desire(agent_id: str, desire: Desire):
    agent = get_agent_or_404(agent_id, agent_service)
    return agent_service.add_desire(agent_id, desire)

@router.post("/agents/{agent_id}/intentions", response_model=Agent)
async def add_intention(agent_id: str, intention: Intention):
    agent = get_agent_or_404(agent_id, agent_service)
    return agent_service.add_intention(agent_id, intention)

@router.get("/{agent_id}", response_model=Agent)
async def get_agent(agent_id: UUID, agent_service: AgentService = Depends(get_agent_service)):
    agent = get_agent_or_404(agent_id, agent_service)
    return agent

@router.put("/{agent_id}", response_model=Agent)
async def update_agent(agent_id: UUID, update_data: Dict[str, Any], agent_service: AgentService = Depends(get_agent_service)):
    agent = get_agent_or_404(agent_id, agent_service)
    return agent_service.update_agent(agent_id, update_data)

@router.delete("/{agent_id}")
async def delete_agent(agent_id: UUID, agent_service: AgentService = Depends(get_agent_service)):
    success = agent_service.delete_agent(agent_id)
    if not success:
        raise AgentNotFoundError(agent_id)
    return {"message": "Agent deleted successfully"}

@router.post("/environmental", response_model=EnvironmentalAgent)
async def create_environmental_agent(agent: EnvironmentalAgent, agent_service: AgentService = Depends(get_agent_service)):
    return agent_service.create_agent_with_behavior(agent, "environmental")

@router.post("/proactive", response_model=ProactiveAgent)
async def create_proactive_agent(agent: ProactiveAgent, agent_service: AgentService = Depends(get_agent_service)):
    return agent_service.create_agent_with_behavior(agent, "proactive")

@router.post("/reactive", response_model=ReactiveAgent)
async def create_reactive_agent(agent: ReactiveAgent, agent_service: AgentService = Depends(get_agent_service)):
    return agent_service.create_agent_with_behavior(agent, "reactive")

@router.put("/environmental/{agent_id}/update_state", response_model=EnvironmentalAgent)
async def update_environment_state(agent_id: UUID, new_state: dict, env_service: EnvironmentService = Depends(get_environment_service)):
    agent = env_service.update_environment_state(agent_id, new_state)
    if agent is None:
        raise AgentNotFoundError(agent_id)
    return agent

@router.post("/proactive/{agent_id}/propose_strategy", response_model=dict)
async def propose_strategy(agent_id: UUID, strategy: dict, strategy_service: StrategyService = Depends(get_strategy_service)):
    proposed_strategy = strategy_service.propose_strategy(agent_id, strategy)
    if proposed_strategy is None:
        raise AgentNotFoundError(agent_id)
    return proposed_strategy

@router.post("/reactive/{agent_id}/handle_event", response_model=dict)
async def handle_event(agent_id: UUID, event: dict, reactive_service: ReactiveService = Depends(get_reactive_service)):
    response = reactive_service.handle_event(agent_id, event)
    if response is None:
        raise AgentNotFoundError(agent_id)
    return response