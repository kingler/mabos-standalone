from typing import List

from fastapi import APIRouter, HTTPException

from app.models.agent.intention import (Intention, IntentionCreate,
                                             IntentionUpdate)
from app.services import intention_service

router = APIRouter()

@router.post("/intentions", response_model=Intention)
async def create_intention(intention: IntentionCreate):
    return intention_service.create_intention(intention)

@router.get("/intentions", response_model=List[Intention])
async def get_intentions():
    return intention_service.get_intentions()

@router.get("/intentions/{intention_id}", response_model=Intention)
async def get_intention(intention_id: str):
    if intention := intention_service.get_intention(intention_id):
        return intention
    raise HTTPException(status_code=404, detail="Intention not found")

@router.put("/intentions/{intention_id}", response_model=Intention)
async def update_intention(intention_id: str, intention: IntentionUpdate):
    if updated_intention := intention_service.update_intention(intention_id, intention):
        return updated_intention
    raise HTTPException(status_code=404, detail="Intention not found")

@router.delete("/intentions/{intention_id}", status_code=204)
async def delete_intention(intention_id: str):
    if not intention_service.delete_intention(intention_id):
        raise HTTPException(status_code=404, detail="Intention not found")
