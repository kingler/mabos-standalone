from fastapi import APIRouter, HTTPException
from typing import List
from app.models.goal import Goal
from app.services.goal_service import GoalService

router = APIRouter()
goal_service = GoalService()

@router.post("/goals/", response_model=Goal)
async def create_goal(description: str, priority: int):
    return goal_service.create_goal(description, priority)

@router.get("/goals/{goal_id}", response_model=Goal)
async def get_goal(goal_id: str):
    goal = goal_service.get_goal(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal

@router.get("/goals/", response_model=List[Goal])
async def list_goals():
    return goal_service.list_goals()

@router.post("/goals/{goal_id}/decompose", response_model=Goal)
async def decompose_goal(goal_id: str):
    goal = goal_service.decompose_goal(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal

@router.put("/goals/{goal_id}/status", response_model=Goal)
async def update_goal_status(goal_id: str, is_achieved: bool):
    goal = goal_service.update_goal_status(goal_id, is_achieved)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal