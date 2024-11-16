from fastapi import APIRouter, HTTPException
from typing import List
from app.models.business.business_goal import BusinessGoal
from app.services.business_goal_service import BusinessGoalService

router = APIRouter()
business_goal_service = BusinessGoalService()

@router.post("/business-goals/", response_model=BusinessGoal)
async def create_business_goal(name: str, description: str, priority: str, parent_goal_id: str = None):
    return business_goal_service.create_goal(name, description, priority, parent_goal_id)

@router.get("/business-goals/{goal_id}", response_model=BusinessGoal)
async def get_business_goal(goal_id: str):
    goal = business_goal_service.get_goal(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Business goal not found")
    return goal

@router.get("/business-goals/", response_model=List[BusinessGoal])
async def list_business_goals():
    return business_goal_service.list_goals()

@router.put("/business-goals/{goal_id}", response_model=BusinessGoal)
async def update_business_goal(goal_id: str, goal_data: dict):
    updated_goal = business_goal_service.update_goal(goal_id, **goal_data)
    if not updated_goal:
        raise HTTPException(status_code=404, detail="Business goal not found")
    return updated_goal

@router.delete("/business-goals/{goal_id}")
async def delete_business_goal(goal_id: str):
    if not business_goal_service.delete_goal(goal_id):
        raise HTTPException(status_code=404, detail="Business goal not found")
    return {"message": "Business goal deleted successfully"}