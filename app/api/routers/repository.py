from fastapi import APIRouter, Depends, HTTPException

from app.models.repository import RepositoryConfig
from app.services.repository_service import RepositoryService

router = APIRouter()

def get_repository_service() -> RepositoryService:
    return RepositoryService()

@router.get("/config", response_model=RepositoryConfig)
def get_config(service: RepositoryService = Depends(get_repository_service)):
    return service.config

@router.post("/config")
def update_config(config: RepositoryConfig, service: RepositoryService = Depends(get_repository_service)):
    service.config = config
    return {"message": "Configuration updated successfully"}

@router.get("/path/{key}")
def get_path(key: str, service: RepositoryService = Depends(get_repository_service)):
    path = service.get_path(key)
    if not path:
        raise HTTPException(status_code=404, detail="Path not found")
    return {"path": path}

@router.post("/path/{key}")
def set_path(key: str, path: str, service: RepositoryService = Depends(get_repository_service)):
    service.set_path(key, path)
    return {"message": f"Path for {key} updated successfully"}

@router.get("/auth")
def get_auth_credentials(service: RepositoryService = Depends(get_repository_service)):
    return service.get_auth_credentials()

@router.post("/auth")
def set_auth_credentials(username: str, password: str, service: RepositoryService = Depends(get_repository_service)):
    service.set_auth_credentials(username, password)
    return {"message": "Auth credentials updated successfully"}