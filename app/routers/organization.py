# app/routers/organization.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.models.organization import Organization, OrganizationCreate, OrganizationUpdate
from app.services import organization_service

router = APIRouter()

@router.post("/organizations", response_model=Organization)
async def create_organization(organization: OrganizationCreate):
    return organization_service.create_organization(organization)

@router.get("/organizations", response_model=List[Organization])
async def get_organizations():
    return organization_service.get_organizations()

@router.get("/organizations/{organization_id}", response_model=Organization)
async def get_organization(organization_id: str):
    if organization := organization_service.get_organization(organization_id):
        return organization
    raise HTTPException(status_code=404, detail="Organization not found")

@router.put("/organizations/{organization_id}", response_model=Organization)
async def update_organization(organization_id: str, organization: OrganizationUpdate):
    if updated_organization := organization_service.update_organization(organization_id, organization):
        return updated_organization
    raise HTTPException(status_code=404, detail="Organization not found")

@router.delete("/organizations/{organization_id}", status_code=204)
async def delete_organization(organization_id: str):
    if not organization_service.delete_organization(organization_id):
        raise HTTPException(status_code=404, detail="Organization not found")