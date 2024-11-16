from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, validator
from enum import Enum

class ModelType(str, Enum):
    BPMN = "bpmn"
    XUML = "xuml"
    XML = "xml"

class TranslationOutput(BaseModel):
    translated_text: str = Field(..., min_length=1)
    source_language: str = Field(..., min_length=2, max_length=5)
    target_language: str = Field(..., min_length=2, max_length=5)
    confidence: float = Field(..., ge=0.0, le=1.0)

    class Config:
        schema_extra = {
            "example": {
                "translated_text": "Bonjour le monde",
                "source_language": "en",
                "target_language": "fr",
                "confidence": 0.95
            }
        }

    @validator("source_language", "target_language")
    def validate_language_code(cls, v):
        if not v.isalpha():
            raise ValueError("Language code must contain only letters")
        return v.lower()

class KnowledgeOutput(BaseModel):
    concepts: List[str] = Field(..., min_items=1)
    relationships: List[Dict[str, str]] = Field(..., min_items=1)
    facts: List[str] = Field(..., min_items=1)
    confidence: float = Field(..., ge=0.0, le=1.0)

    class Config:
        schema_extra = {
            "example": {
                "concepts": ["Customer", "Order", "Product"],
                "relationships": [{"subject": "Customer", "predicate": "places", "object": "Order"}],
                "facts": ["Customers can place multiple orders"],
                "confidence": 0.85
            }
        }

class Concept(BaseModel):
    name: str = Field(..., min_length=1)
    attributes: List[str] = Field(default_factory=list)
    description: Optional[str] = None
    sbvr_reference: Optional[str] = None

class Property(BaseModel):
    name: str = Field(..., min_length=1)
    domain: str = Field(..., min_length=1)
    range: str = Field(..., min_length=1)
    description: Optional[str] = None

class Relationship(BaseModel):
    name: str = Field(..., min_length=1)
    source: str = Field(..., min_length=1)
    target: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)
    cardinality: Optional[str] = None
    description: Optional[str] = None
    sbvr_reference: Optional[str] = None

class OntologyOutput(BaseModel):
    concepts: List[Concept] = Field(..., min_items=1)
    properties: List[Property] = Field(..., min_items=1)
    relationships: List[Relationship] = Field(..., min_items=1)
    axioms: List[str] = Field(..., min_items=1)

    class Config:
        schema_extra = {
            "example": {
                "concepts": [{
                    "name": "Customer",
                    "attributes": ["id", "name"],
                    "description": "A person or organization that places orders"
                }],
                "properties": [{
                    "name": "hasOrder",
                    "domain": "Customer",
                    "range": "Order",
                    "description": "Represents the orders placed by a customer"
                }],
                "relationships": [{
                    "name": "places",
                    "source": "Customer",
                    "target": "Order",
                    "type": "association",
                    "cardinality": "1..*",
                    "description": "Customer places an order"
                }],
                "axioms": ["Every Order must have exactly one Customer"]
            }
        }

    @validator("concepts")
    def validate_concepts(cls, v):
        names = [c.name for c in v]
        if len(names) != len(set(names)):
            raise ValueError("Concept names must be unique")
        return v

    @validator("relationships")
    def validate_relationships(cls, v, values):
        if "concepts" not in values:
            return v
        
        concept_names = {c.name for c in values["concepts"]}
        for rel in v:
            if rel.source not in concept_names:
                raise ValueError(f"Relationship source '{rel.source}' must reference an existing concept")
            if rel.target not in concept_names:
                raise ValueError(f"Relationship target '{rel.target}' must reference an existing concept")
        return v

class ModelOutput(BaseModel):
    model_type: ModelType
    content: str = Field(..., min_length=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    validation_results: Optional[Dict[str, Any]] = None

    class Config:
        schema_extra = {
            "example": {
                "model_type": "bpmn",
                "content": "<?xml version='1.0' encoding='UTF-8'?><bpmn:definitions ...",
                "metadata": {"version": "2.0", "author": "system"},
                "validation_results": {"valid": true, "errors": []}
            }
        } 