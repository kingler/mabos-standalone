from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, ConfigDict, SkipValidation
from rdflib import Graph, Literal, Namespace, RDF, RDFS
from owlready2 import World
from app.core.models.sentence_transformer import SentenceTransformerWrapper


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
    concepts: Dict[str, Any] = Field(default_factory=dict)
    relationships: Dict[str, Any] = Field(default_factory=dict)
    graph: Graph = Field(default_factory=Graph)
    sentence_transformer: Optional[Any] = None
    ns: SkipValidation[Namespace] = Field(default_factory=lambda: Namespace("http://example.org/ontology#"))

    model_config = ConfigDict(arbitrary_types_allowed=True)

   ## def __init__(self, **data):
        ## super().__init__(**data)
        ## self.ns = Namespace("http://example.org/ontology#")

    def initialize_sentence_transformer(self):
        if self.sentence_transformer is None:
            from app.core.models.sentence_transformer import SentenceTransformerWrapper
            self.sentence_transformer = SentenceTransformerWrapper()

    def add_concept(self, name: str, description: str):
        self.concepts[name] = {"description": description}
        self.graph.add((self.ns[name], RDF.type, RDFS.Class))
        self.graph.add((self.ns[name], RDFS.label, Literal(name)))
        self.graph.add((self.ns[name], RDFS.comment, Literal(description)))

    def add_relationship(self, name: str, domain: str, range: str):
        self.relationships[name] = {"domain": domain, "range": range}
        self.graph.add((self.ns[name], RDF.type, RDF.Property))
        self.graph.add((self.ns[name], RDFS.domain, self.ns[domain]))
        self.graph.add((self.ns[name], RDFS.range, self.ns[range]))

    def get_concept_embedding(self, concept: str):
        self.initialize_sentence_transformer()
        return self.sentence_transformer.encode(self.concepts[concept]["description"])

    def find_similar_concepts(self, query: str, top_k: int = 5):
        self.initialize_sentence_transformer()
        query_embedding = self.sentence_transformer.encode(query)
        similarities = []
        for concept, data in self.concepts.items():
            concept_embedding = self.sentence_transformer.encode(data["description"])
            similarity = self.sentence_transformer.cosine_similarity(query_embedding, concept_embedding)
            similarities.append((concept, similarity))
        return sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]

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
 
        
# Test the class
onto = Ontology()
print(onto)        