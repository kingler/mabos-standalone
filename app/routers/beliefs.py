from fastapi import APIRouter, Depends
from app.models import knowledge_base
from app.services.belief_service import BeliefService
from app.models.belief import Belief

router = APIRouter()

def get_belief_service():
    # This would be replaced with proper dependency injection
    return BeliefService(knowledge_base)

@router.post("/beliefs/", response_model=Belief)
async def create_belief(belief_data: dict, service: BeliefService = Depends(get_belief_service)):
    return service.create_belief(belief_data)

@router.put("/beliefs/{belief_id}", response_model=Belief)
async def update_belief(belief_id: str, new_data: dict, service: BeliefService = Depends(get_belief_service)):
    return service.update_belief(belief_id, new_data)

@router.post("/beliefs/{belief_id}/revise", response_model=Belief)
async def revise_belief(belief_id: str, new_evidence: dict, service: BeliefService = Depends(get_belief_service)):
    return service.revise_belief(belief_id, new_evidence)

# Add other endpoints as needed