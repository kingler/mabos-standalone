from fastapi import APIRouter, HTTPException
from typing import List
from app.models.plan import Plan, PlanStep
from app.services.plan_service import PlanService
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService

router = APIRouter()
agent_service = AgentService()
goal_service = GoalService()
plan_service = PlanService(agent_service, goal_service)

@router.post("/plans/", response_model=Plan)
async def create_plan(goal_id: str):
    plan = plan_service.create_plan(goal_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Goal not found")
    return plan

@router.get("/plans/{plan_id}", response_model=Plan)
async def get_plan(plan_id: str):
    plan = plan_service.get_plan(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.get("/plans/", response_model=List[Plan])
async def list_plans():
    return plan_service.list_plans()

@router.post("/plans/{plan_id}/steps", response_model=Plan)
async def add_plan_step(plan_id: str, step: PlanStep):
    plan = plan_service.add_plan_step(plan_id, step)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.put("/plans/{plan_id}/steps/{step_id}", response_model=Plan)
async def update_step_status(plan_id: str, step_id: str, is_completed: bool):
    plan = plan_service.update_step_status(plan_id, step_id, is_completed)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan or step not found")
    return plan

@router.post("/plans/{plan_id}/execute")
async def execute_plan(plan_id: str, agent_id: str):
    result = plan_service.execute_plan(plan_id, agent_id)
    if not result:
        raise HTTPException(status_code=404, detail="Plan or Agent not found")
    return result