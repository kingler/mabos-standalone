from fastapi import APIRouter, Depends
from app.services.mabos_service import MABOSService
from app.core.mabos_service_model import MABOSServiceModel, MABOSServiceSummary
from app.dependencies import get_mabos_service

router = APIRouter()

@router.get("/mabos_service", response_model=MABOSServiceModel)
async def get_mabos_service_model(mabos_service: MABOSService = Depends(get_mabos_service)) -> MABOSServiceModel:
    service_dict = mabos_service.to_model()
    return MABOSServiceModel(summary=MABOSServiceSummary(**service_dict["summary"]))