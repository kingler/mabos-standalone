from typing import Any, Dict, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.agent import Agent
from app.config.config import get_settings
from app.core.models.mas.mas_models import Explanation
from app.core.models.rules.rules_engine import Rules
from app.core.services.mas_services import MASService

router = APIRouter()

settings = get_settings()

def get_mas_service():
    domain_rules = Rules()  # Instantiate DomainRules
    return MASService(
        num_agents=settings.num_agents,
        num_states=settings.num_states,
        state_size=settings.state_size,
        action_size=settings.action_size,
        ontology_path=settings.ontology_path,
        domain_rules=domain_rules  # Pass domain_rules instance
    )

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
    if not mas_service.remove_agent(agent_id):
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

@router.post("/check_consistency")
async def check_consistency(mas_service: MASService = Depends(get_mas_service)):
    inconsistencies = mas_service.consistency_checker.check_consistency()
    return {"inconsistencies": inconsistencies}

@router.post("/temporal_reasoning")
async def perform_temporal_reasoning(start_time: str, end_time: str, mas_service: MASService = Depends(get_mas_service)):
    results = mas_service.temporal_reasoning.reason_over_time(start_time, end_time)
    return {"results": results}

@router.post("/distributed_processing")
async def process_distributed(operation: str, data: List[Dict[str, Any]], mas_service: MASService = Depends(get_mas_service)):
    result = await mas_service.distributed_knowledge.process_distributed(operation, data)
    return {"result": result}

@router.post("/acquire_knowledge")
async def acquire_knowledge(mas_service: MASService = Depends(get_mas_service)):
    gaps = mas_service.active_knowledge_acquisition.identify_knowledge_gaps()
    queries = mas_service.active_knowledge_acquisition.generate_queries(gaps)
    return {"knowledge_gaps": gaps, "queries": queries}

@router.post("/resolve_conflicts")
async def resolve_conflicts(mas_service: MASService = Depends(get_mas_service)):
    conflicts = mas_service.conflict_resolution.detect_conflicts()
    mas_service.conflict_resolution.resolve_conflicts(conflicts)
    return {"resolved_conflicts": conflicts}

@router.post("/generate_explanation")
async def generate_explanation(decision: Dict[str, Any], mas_service: MASService = Depends(get_mas_service)):
    explanation = mas_service.explanation_generator.generate_explanation(decision)
    evidence = mas_service.explanation_generator.provide_evidence(explanation)
    return Explanation(decision=decision, reasoning=explanation, evidence=evidence)