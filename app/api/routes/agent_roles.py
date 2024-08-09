from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.core.models.agent.agent_role import AgentRole
from app.core.services.agent_role_service import AgentRolesService

router = APIRouter()

@router.get("/", response_model=List[AgentRole])
async def get_all_roles(agent_roles_service: AgentRolesService = Depends()):
    return agent_roles_service.get_all_roles()

@router.get("/{role_id}", response_model=AgentRole)
async def get_role_by_id(role_id: int, agent_roles_service: AgentRolesService = Depends()):
    role = agent_roles_service.get_role_by_id(role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.post("/", response_model=AgentRole)
async def create_role(role: AgentRole, agent_roles_service: AgentRolesService = Depends()):
    return agent_roles_service.create_role(role)

@router.put("/{role_id}", response_model=AgentRole)
async def update_role(role_id: int, role: AgentRole, agent_roles_service: AgentRolesService = Depends()):
    updated_role = agent_roles_service.update_role(role_id, role)
    if updated_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role

@router.delete("/{role_id}")
async def delete_role(role_id: int, agent_roles_service: AgentRolesService = Depends()):
    deleted = agent_roles_service.delete_role(role_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}
