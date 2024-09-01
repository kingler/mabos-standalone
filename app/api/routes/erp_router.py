from typing import Any, Dict
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.erp.erp_models import ERPModule, ERPSystem
from app.core.services.erp_service import ERPService

router = APIRouter()

def get_erp_service():
    return ERPService()

@router.post("/erp", response_model=ERPSystem)
async def create_erp_system(name: str, erp_service: ERPService = Depends(get_erp_service)):
    return await erp_service.create_erp_system(name)

@router.post("/erp/{erp_id}/modules", response_model=ERPModule)
async def add_module(erp_id: UUID, module_type: str, requirements: Dict[str, Any], erp_service: ERPService = Depends(get_erp_service)):
    try:
        module = await erp_service.generate_module(module_type, requirements)
        return await erp_service.add_module(erp_id, module)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/erp/{erp_id}", response_model=ERPSystem)
async def get_erp_system(erp_id: UUID, erp_service: ERPService = Depends(get_erp_service)):
    try:
        return await erp_service.get_erp_system(erp_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/erp/{erp_id}/modules/{module_id}", response_model=ERPModule)
async def update_module(erp_id: UUID, module_id: UUID, updates: Dict[str, Any], erp_service: ERPService = Depends(get_erp_service)):
    try:
        return await erp_service.update_module(erp_id, module_id, updates)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/erp/{erp_id}/modules/{module_id}")
async def delete_module(erp_id: UUID, module_id: UUID, erp_service: ERPService = Depends(get_erp_service)):
    try:
        await erp_service.delete_module(erp_id, module_id)
        return {"message": "Module deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))