from fastapi import APIRouter, HTTPException
from app.core.models.business.business_model import BusinessModel
from app.core.services.business_model_service import BusinessModelService

router = APIRouter()
business_model_service = BusinessModelService()

@router.post("/generate", response_model=BusinessModel)
async def generate_business_model(model_type: str, description: str):
    try:
        return await business_model_service.generate_model(model_type, description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@router.get("/{model_id}", response_model=BusinessModel)
async def get_business_model(model_id: str):
    if not (model := business_model_service.get_model(model_id)):
        raise HTTPException(status_code=404, detail="Business model not found")
    return model

@router.put("/{model_id}", response_model=BusinessModel)
async def update_business_model(model_id: str, model: BusinessModel):
    if updated_model := business_model_service.update_model(model_id, model):
        return updated_model
    raise HTTPException(status_code=404, detail="Business model not found")
