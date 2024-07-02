from fastapi import APIRouter, HTTPException
from typing import List
from app.models.desire import Desire, DesireCreate, DesireUpdate
from app.services import desire_service

router = APIRouter()

@router.post("/desires", response_model=Desire)
async def create_desire(desire: DesireCreate):
    return desire_service.create_desire(desire)

@router.get("/desires", response_model=List[Desire])
async def get_desires():
    return desire_service.get_desires()

@router.get("/desires/{desire_id}", response_model=Desire)
async def get_desire(desire_id: str):
    if desire := desire_service.get_desire(desire_id):
        return desire
    raise HTTPException(status_code=404, detail="Desire not found")

@router.put("/desires/{desire_id}", response_model=Desire)
async def update_desire(desire_id: str, desire: DesireUpdate):
    if updated_desire := desire_service.update_desire(desire_id, desire):
        return updated_desire
    raise HTTPException(status_code=404, detail="Desire not found")

@router.delete("/desires/{desire_id}", status_code=204)
async def delete_desire(desire_id: str):
    if not desire_service.delete_desire(desire_id):
        raise HTTPException(status_code=404, detail="Desire not found")
