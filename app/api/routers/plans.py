from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.models.agent.plan import Plan, PlanStep
from app.models.system.world_model import WorldModel
from app.models.system.world_model_provider import get_world_model
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService
from app.services.plan_service import PlanService

router = APIRouter()

def get_agent_service(world_model: WorldModel = Depends(get_world_model)):
    return AgentService(world_model)

def get_goal_service():
    return GoalService()

def get_plan_service(agent_service: AgentService = Depends(get_agent_service), goal_service: GoalService = Depends(get_goal_service)):
    return PlanService(agent_service, goal_service)

@router.post("/", response_model=Plan)
async def create_plan(goal_id: str, plan_service: PlanService = Depends(get_plan_service)):
    plan = plan_service.create_plan(goal_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Goal not found")
    return plan

@router.get("/{plan_id}", response_model=Plan)
async def get_plan(plan_id: str, plan_service: PlanService = Depends(get_plan_service)):
    plan = plan_service.get_plan(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.get("/", response_model=List[Plan])
async def list_plans(plan_service: PlanService = Depends(get_plan_service)):
    return plan_service.list_plans()

@router.post("/{plan_id}/steps", response_model=Plan)
async def add_plan_step(plan_id: str, step: PlanStep, plan_service: PlanService = Depends(get_plan_service)):
    plan = plan_service.add_plan_step(plan_id, step)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.put("/{plan_id}/steps/{step_id}", response_model=Plan)
async def update_step_status(plan_id: str, step_id: str, is_completed: bool, plan_service: PlanService = Depends(get_plan_service)):
    plan = plan_service.update_step_status(plan_id, step_id, is_completed)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan or step not found")
    return plan

@router.post("/{plan_id}/execute")
async def execute_plan(plan_id: str, agent_id: str, plan_service: PlanService = Depends(get_plan_service)):
    result = plan_service.execute_plan(plan_id, agent_id)
    if not result:
        raise HTTPException(status_code=404, detail="Plan or Agent not found")
    return result