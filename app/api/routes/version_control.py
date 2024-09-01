from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.mas.mas_version_control import BranchInfo, CommitInfo
from app.core.services.version_control_service import VersionControlService

router = APIRouter()

def get_vc_service():
    return VersionControlService()

@router.post("/commit")
async def commit_changes(message: str, vc_service: VersionControlService = Depends(get_vc_service)):
    try:
        vc_service.commit_changes(message)
        return {"message": "Changes committed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/branch")
async def create_branch(branch_name: str, vc_service: VersionControlService = Depends(get_vc_service)):
    try:
        vc_service.create_branch(branch_name)
        return {"message": f"Branch '{branch_name}' created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/merge")
async def merge_branch(branch_name: str, vc_service: VersionControlService = Depends(get_vc_service)):
    try:
        vc_service.merge_branch(branch_name)
        return {"message": f"Branch '{branch_name}' merged successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/branches", response_model=List[BranchInfo])
async def list_branches(vc_service: VersionControlService = Depends(get_vc_service)):
    return [BranchInfo(name=branch) for branch in vc_service.list_branches()]

@router.get("/history", response_model=List[CommitInfo])
async def get_commit_history(vc_service: VersionControlService = Depends(get_vc_service)):
    return [CommitInfo(id=commit.hexsha, message=commit.message) for commit in vc_service.get_commit_history()]