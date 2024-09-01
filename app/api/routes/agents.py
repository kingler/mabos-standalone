from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.agents.core_agents.agent_types import (Agent, EnvironmentalAgent,
                                                     ProactiveAgent,
                                                     ReactiveAgent)
from app.core.models.agent.belief import Belief
from app.core.models.agent.desire import Desire
from app.core.models.agent.intention import Intention
from app.core.models.system.world_model import WorldModel
from app.core.models.system.world_model_provider import get_world_model
from app.core.services.agent_service import AgentService
from app.core.services.environment_service import EnvironmentService
from app.core.services.reactive_service import ReactiveService
from app.core.services.strategy_service import StrategyService

router = APIRouter()

def get_agent_service(world_model: WorldModel = Depends(get_world_model)):
    return AgentService(world_model)

def get_environment_service(agent_service: AgentService = Depends(get_agent_service)):
    return EnvironmentService(agent_service)

def get_strategy_service(agent_service: AgentService = Depends(get_agent_service)):
    return StrategyService(agent_service)

def get_reactive_service(agent_service: AgentService = Depends(get_agent_service)):
    return ReactiveService(agent_service)

@router.post("/", response_model=Agent)
async def create_agent(agent: Agent, service: AgentService = Depends(get_agent_service)):
    return service.create_agent(agent)

@router.get("/{agent_id}", response_model=Agent)
async def get_agent(agent_id: UUID, service: AgentService = Depends(get_agent_service)):
    agent = service.get_agent(agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent with id {agent_id} not found")
    return agent

@router.get("/", response_model=List[Agent])
async def list_agents(service: AgentService = Depends(get_agent_service)):
    return service.list_agents()

@router.put("/{agent_id}", response_model=Agent)
async def update_agent(agent_id: UUID, update_data: Dict[str, Any], service: AgentService = Depends(get_agent_service)):
    agent = service.update_agent(agent_id, update_data)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent with id {agent_id} not found")
    return agent

@router.delete("/{agent_id}")
async def delete_agent(agent_id: UUID, service: AgentService = Depends(get_agent_service)):
    success = service.delete_agent(agent_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Agent with id {agent_id} not found")
    return {"message": "Agent deleted successfully"}

@router.post("/{agent_id}/beliefs", response_model=Agent)
async def add_belief(agent_id: UUID, belief: Belief, service: AgentService = Depends(get_agent_service)):
    agent = service.add_belief(agent_id, belief)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent with id {agent_id} not found")
    return agent

@router.post("/{agent_id}/desires", response_model=Agent)
async def add_desire(agent_id: UUID, desire: Desire, service: AgentService = Depends(get_agent_service)):
    agent = service.add_desire(agent_id, desire)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent with id {agent_id} not found")
    return agent

@router.post("/{agent_id}/intentions", response_model=Agent)
async def add_intention(agent_id: UUID, intention: Intention, service: AgentService = Depends(get_agent_service)):
    agent = service.add_intention(agent_id, intention)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent with id {agent_id} not found")
    return agent

@router.post("/environmental", response_model=EnvironmentalAgent)
async def create_environmental_agent(agent: EnvironmentalAgent, service: AgentService = Depends(get_agent_service)):
    return service.create_agent_with_behavior(agent, "environmental")

@router.post("/proactive", response_model=ProactiveAgent)
async def create_proactive_agent(agent: ProactiveAgent, service: AgentService = Depends(get_agent_service)):
    return service.create_agent_with_behavior(agent, "proactive")

@router.post("/reactive", response_model=ReactiveAgent)
async def create_reactive_agent(agent: ReactiveAgent, service: AgentService = Depends(get_agent_service)):
    return service.create_agent_with_behavior(agent, "reactive")

@router.put("/environmental/{agent_id}/update_state", response_model=EnvironmentalAgent)
async def update_environment_state(agent_id: UUID, new_state: dict, env_service: EnvironmentService = Depends(get_environment_service)):
    agent = env_service.update_environment_state(agent_id, new_state)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Environmental agent with id {agent_id} not found")
    return agent

@router.post("/proactive/{agent_id}/propose_strategy", response_model=dict)
async def propose_strategy(agent_id: UUID, strategy: dict, strategy_service: StrategyService = Depends(get_strategy_service)):
    proposed_strategy = strategy_service.propose_strategy(agent_id, strategy)
    if proposed_strategy is None:
        raise HTTPException(status_code=404, detail=f"Proactive agent with id {agent_id} not found")
    return proposed_strategy

@router.post("/reactive/{agent_id}/handle_event", response_model=dict)
async def handle_event(agent_id: UUID, event: dict, reactive_service: ReactiveService = Depends(get_reactive_service)):
    response = reactive_service.handle_event(agent_id, event)
    if response is None:
        raise HTTPException(status_code=404, detail=f"Reactive agent with id {agent_id} not found")
    return response