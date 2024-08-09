from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from rdflib import Graph, Namespace, RDF, RDFS
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

class Ontology(BaseModel):
    concepts: Dict[str, Concept] = Field(default_factory=dict)
    relationships: Dict[str, Relationship] = Field(default_factory=dict)
    graph: Graph = Field(default_factory=Graph)
    world: World = Field(default_factory=World)

    def __init__(self, **data):
        super().__init__(**data)
        self.ns = Namespace("http://example.org/ontology#")

    def add_concept(self, concept: Concept):
        self.concepts[concept.name] = concept
        self.graph.add((self.ns[concept.name], RDF.type, RDFS.Class))
        self.graph.add((self.ns[concept.name], RDFS.label, concept.name))
        if concept.description:
            self.graph.add((self.ns[concept.name], RDFS.comment, concept.description))

    def add_relationship(self, relationship: Relationship):
        self.relationships[relationship.name] = relationship
        self.graph.add((self.ns[relationship.name], RDF.type, RDF.Property))
        self.graph.add((self.ns[relationship.name], RDFS.domain, self.ns[relationship.domain]))
        self.graph.add((self.ns[relationship.name], RDFS.range, self.ns[relationship.range]))

    def get_concept_hierarchy(self) -> Dict[int, List[str]]:
        hierarchy = {}
        for concept in self.concepts.values():
            if concept.tier not in hierarchy:
                hierarchy[concept.tier] = []
            hierarchy[concept.tier].append(concept.name)
        return hierarchy

    def reason(self, reasoner_type: str = "RDFS"):
        if reasoner_type == "RDFS":
            # Implement RDFS reasoning
            pass
        elif reasoner_type == "OWL":
            # Implement OWL reasoning
            pass

    def query(self, sparql_query: str) -> List[Dict[str, Any]]:
        results = self.graph.query(sparql_query)
        return [dict(zip(result.vars, [str(term) for term in result])) for result in results]

    def save(self, file_path: str):
        self.graph.serialize(destination=file_path, format="turtle")

    def load(self, file_path: str):
        self.graph.parse(file_path, format="turtle")
        # Populate concepts and relationships from the loaded graph