from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.agent.goal import Goal
from app.core.models.agent.plan import Plan
from app.core.services.planning_service import PlanningService

router = APIRouter()

def get_planning_service():
    # In a real application, you would use dependency injection here
    domain_knowledge = {}  # Load this from a configuration or database
    return PlanningService(domain_knowledge)

@router.post("/plan", response_model=Plan)
async def generate_plan(goal: Goal, current_state: Dict[str, str], planning_service: PlanningService = Depends(get_planning_service)):
    try:
        return planning_service.generate_plan(goal, current_state)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@router.post("/execute", response_model=bool)
async def execute_plan(plan: Plan, current_state: Dict[str, str], planning_service: PlanningService = Depends(get_planning_service)):
    return planning_service.execute_plan(plan, current_state)

@router.post("/library/add", response_model=Plan)
async def add_plan_to_library(plan: Plan, planning_service: PlanningService = Depends(get_planning_service)):
    planning_service.add_plan_to_library(plan)
    return plan

@router.delete("/library/{goal_id}/{plan_id}")
async def remove_plan_from_library(goal_id: str, plan_id: str, planning_service: PlanningService = Depends(get_planning_service)):
    planning_service.remove_plan_from_library(plan_id, goal_id)
    return {"message": "Plan removed successfully"}

@router.get("/library/{goal_id}", response_model=List[Plan])
async def get_plans_for_goal(goal_id: str, planning_service: PlanningService = Depends(get_planning_service)):
    return planning_service.get_plans_for_goal(goal_id)

@router.put("/library", response_model=Plan)
async def update_plan_in_library(plan: Plan, planning_service: PlanningService = Depends(get_planning_service)):
    planning_service.update_plan_in_library(plan)
    return plan