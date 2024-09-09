from typing import List

from fastapi import APIRouter, HTTPException

from app.models.business.business_plan import BusinessPlan
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.services.business_plan_service import BusinessPlanService

router = APIRouter()

# Initialize the business plan service
knowledge_base = KnowledgeBase()  # Initialize with actual knowledge base data
api_key = "your_api_key_here"
business_plan_service = BusinessPlanService(knowledge_base, api_key)

@router.post("/business_plans/", response_model=BusinessPlan)
def create_business_plan(business_plan: BusinessPlan):
    return business_plan_service.create_business_plan(business_plan)

@router.get("/business_plans/{plan_id}", response_model=BusinessPlan)
def get_business_plan(plan_id: str):
    try:
        return business_plan_service.get_business_plan(plan_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/business_plans/{plan_id}", response_model=BusinessPlan)
def update_business_plan(plan_id: str):
    try:
        return business_plan_service.update_business_plan(plan_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/business_plans/{plan_id}/actions/{action_id}", response_model=BusinessPlan)
def execute_action(plan_id: str, action_id: str):
    try:
        return business_plan_service.execute_action(plan_id, action_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))