# test_ontology.py
from typing import Dict, Any, Optional
from ...sentence_transformer import SentenceTransformerWrapper
from pydantic import BaseModel, Field, ConfigDict
from rdflib import Graph
from owlready2 import World

class Concept(BaseModel):
    name: str
    description: Optional[str] = None
    tier: int = 0

class Relationship(BaseModel):
    name: str
    domain: str
    range: str
    description: Optional[str] = None

class MinimalOntology(BaseModel):
    concepts: Dict[str, Concept] = Field(default_factory=dict)
    relationships: Dict[str, Relationship] = Field(default_factory=dict)
    graph: Graph = Field(default_factory=Graph)
    world: World = Field(default_factory=World)
    sentence_transformer: SentenceTransformerWrapper = Field(default_factory=lambda: SentenceTransformerWrapper())

    model_config = ConfigDict(arbitrary_types_allowed=True)

# Test the class
onto = MinimalOntology()
print(onto)







