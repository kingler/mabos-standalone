from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.core.models.mdd.archimate_model import (BaseArchiMateElement,
                                                 Relationship)
from app.core.services.archimate_service import ArchiMateService

router = APIRouter()

def get_archimate_service():
    return ArchiMateService()

class ElementCreate(BaseModel):
    element_type: str
    id: int
    name: str
    description: str

class RelationshipCreate(BaseModel):
    id: int
    source_id: int
    target_id: int
    type: str

class ElementUpdate(BaseModel):
    name: str = None
    description: str = None

@router.post("/elements", response_model=BaseArchiMateElement)
def create_element(element: ElementCreate, service: ArchiMateService = Depends(get_archimate_service)):
    return service.create_element(**element.dict())

@router.post("/relationships", response_model=Relationship)
def create_relationship(relationship: RelationshipCreate, service: ArchiMateService = Depends(get_archimate_service)):
    return service.create_relationship(**relationship.dict())

@router.get("/elements/{element_id}", response_model=BaseArchiMateElement)
def get_element(element_id: int, service: ArchiMateService = Depends(get_archimate_service)):
    element = service.get_element(element_id)
    if not element:
        raise HTTPException(status_code=404, detail="Element not found")
    return element

@router.get("/elements", response_model=List[BaseArchiMateElement])
def get_all_elements(service: ArchiMateService = Depends(get_archimate_service)):
    return service.get_all_elements()

@router.get("/relationships", response_model=List[Relationship])
def get_relationships(service: ArchiMateService = Depends(get_archimate_service)):
    return service.get_relationships()

@router.put("/elements/{element_id}", response_model=BaseArchiMateElement)
def update_element(element_id: int, element_update: ElementUpdate, service: ArchiMateService = Depends(get_archimate_service)):
    updated_element = service.update_element(element_id, **element_update.dict(exclude_unset=True))
    if not updated_element:
        raise HTTPException(status_code=404, detail="Element not found")
    return updated_element

@router.delete("/elements/{element_id}", response_model=bool)
def delete_element(element_id: int, service: ArchiMateService = Depends(get_archimate_service)):
    if not service.delete_element(element_id):
        raise HTTPException(status_code=404, detail="Element not found")
    return True

@router.delete("/relationships/{relationship_id}", response_model=bool)
def delete_relationship(relationship_id: int, service: ArchiMateService = Depends(get_archimate_service)):
    if not service.delete_relationship(relationship_id):
        raise HTTPException(status_code=404, detail="Relationship not found")
    return True
