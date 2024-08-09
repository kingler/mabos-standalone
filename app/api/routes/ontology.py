from fastapi import APIRouter, HTTPException
from typing import List
from app.core.models.knowledge.ontology import Ontology, Concept, Relationship
from app.core.services.ontology_service import OntologyService

router = APIRouter()
ontology_service = OntologyService()

@router.post("/load_ontology", response_model=Ontology)
async def load_ontology(file_path: str):
    try:
        return ontology_service.load_ontology(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_classes", response_model=List[str])
async def get_classes():
    try:
        return ontology_service.get_classes()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_properties", response_model=List[str])
async def get_properties():
    try:
        return ontology_service.get_properties()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_concept", response_model=Ontology)
async def add_concept(concept: Concept):
    try:
        return ontology_service.add_concept(concept)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_relationship", response_model=Ontology)
async def add_relationship(relationship: Relationship):
    try:
        return ontology_service.add_relationship(relationship)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query_ontology")
async def query_ontology(query: str):
    try:
        return ontology_service.query_ontology(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))