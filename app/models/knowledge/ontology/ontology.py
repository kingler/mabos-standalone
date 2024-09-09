from typing import Any, Dict, List, Optional

from owlready2 import World
from pydantic import BaseModel, ConfigDict, Field, SkipValidation
from rdflib import RDF, RDFS, Graph, Literal, Namespace

from app.models.sentence_transformer import SentenceTransformerWrapper
from app.models.knowledge.base import OntologyInterface


class Concept(BaseModel):
    name: str
    attributes: Dict[str, str]  # attribute name and type
    sbvr_reference: Optional[str] = None  # Reference to SBVR concept

class Relationship(BaseModel):
    name: str
    source: str
    target: str
    sbvr_reference: Optional[str] = None  # Reference to SBVR relationship

class Term(BaseModel):
    name: str
    definition: str
    synonyms: List[str] = Field(default_factory=list)
    related_concepts: List[str] = Field(default_factory=list)

class Name(BaseModel):
    value: str

class VerbConceptWording(BaseModel):
    text: str
    verb_concept: str

class StructuralRule(BaseModel):
    text: str
    modality: str

class OperativeRule(BaseModel):
    text: str
    modality: str

class Proposition(BaseModel):
    text: str

class Sentence(BaseModel):
    text: str

class Module(BaseModel):
    name: str
    exclusion_set: List[str] = Field(default_factory=list)
    body_text: str

class DomainOntology(BaseModel):
    entities: List[str] = Field(default_factory=list)
    attributes: List[str] = Field(default_factory=list)
    relationships: List[str] = Field(default_factory=list)

class DataModel(BaseModel):
    name: str

class DerivedModel(BaseModel):
    name: str

class FIBOMapping(BaseModel):
    entity: str
    fibo_concept: str

class Ontology(OntologyInterface):
    concepts: Dict[str, Any] = Field(default_factory=dict)
    relationships: Dict[str, Any] = Field(default_factory=dict)
    terms: Dict[str, Term] = Field(default_factory=dict)
    names: Dict[str, Name] = Field(default_factory=dict)
    verb_concept_wordings: Dict[str, VerbConceptWording] = Field(default_factory=dict)
    structural_rules: Dict[str, StructuralRule] = Field(default_factory=dict)
    operative_rules: Dict[str, OperativeRule] = Field(default_factory=dict)
    propositions: Dict[str, Proposition] = Field(default_factory=dict)
    sentences: Dict[str, Sentence] = Field(default_factory=dict)
    modules: Dict[str, Module] = Field(default_factory=dict)
    domain_ontologies: Dict[str, DomainOntology] = Field(default_factory=dict)
    data_models: Dict[str, DataModel] = Field(default_factory=dict)
    derived_models: Dict[str, DerivedModel] = Field(default_factory=dict)
    fibo_mappings: Dict[str, FIBOMapping] = Field(default_factory=dict)
    graph: Graph = Field(default_factory=Graph)
    sentence_transformer: Optional[Any] = None
    ns: SkipValidation[Namespace] = Field(default_factory=lambda: Namespace("http://example.org/ontology#"))

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def initialize_sentence_transformer(self):
        if self.sentence_transformer is None:
            from app.models.sentence_transformer import \
                SentenceTransformerWrapper
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

    def add_term(self, name: str, definition: str, synonyms: List[str] = None, related_concepts: List[str] = None):
        term = Term(name=name, definition=definition, synonyms=synonyms or [], related_concepts=related_concepts or [])
        self.terms[name] = term
        self.graph.add((self.ns[name], RDF.type, RDFS.Resource))
        self.graph.add((self.ns[name], RDFS.label, Literal(name)))
        self.graph.add((self.ns[name], RDFS.comment, Literal(definition)))
        for synonym in term.synonyms:
            self.graph.add((self.ns[name], RDFS.label, Literal(synonym)))
        for concept in term.related_concepts:
            self.graph.add((self.ns[name], RDFS.seeAlso, self.ns[concept]))

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
        match reasoner_type:
            case "RDFS":
                # Implement RDFS reasoning
                rdfs_rules = [
                    (RDFS.subClassOf, RDFS.subClassOf, RDFS.subClassOf),
                    (RDFS.subPropertyOf, RDFS.subPropertyOf, RDFS.subPropertyOf),
                    (RDFS.domain, RDFS.domain, RDFS.domain),
                    (RDFS.range, RDFS.range, RDFS.range),
                    (RDF.type, RDFS.domain, RDFS.Class),
                    (RDF.type, RDFS.range, RDFS.Class),
                    (RDFS.subClassOf, RDFS.domain, RDFS.Class),
                    (RDFS.subClassOf, RDFS.range, RDFS.Class),
                    (RDFS.subPropertyOf, RDFS.domain, RDF.Property),
                    (RDFS.subPropertyOf, RDFS.range, RDF.Property),
                    (RDFS.domain, RDFS.domain, RDF.Property),
                    (RDFS.domain, RDFS.range, RDFS.Class),
                    (RDFS.range, RDFS.domain, RDF.Property),
                    (RDFS.range, RDFS.range, RDFS.Class)
                ]
                
                for rule in rdfs_rules:
                    self.graph.add(rule)
                
                # Apply RDFS inference rules
                self.graph.transitive_closure()
            case "OWL":
                # Implement OWL reasoning
                from rdflib.plugins.sparql import prepareQuery

                # Define OWL inference rules (simplified version)
                owl_rules = [
                    # Transitive properties
                    prepareQuery("""
                        INSERT { ?x ?p ?z }
                        WHERE {
                            ?p a owl:TransitiveProperty .
                            ?x ?p ?y .
                            ?y ?p ?z .
                        }
                    """),
                    # Inverse properties
                    prepareQuery("""
                        INSERT { ?y ?p2 ?x }
                        WHERE {
                            ?p1 owl:inverseOf ?p2 .
                            ?x ?p1 ?y .
                        }
                    """),
                    # Symmetric properties
                    prepareQuery("""
                        INSERT { ?y ?p ?x }
                        WHERE {
                            ?p a owl:SymmetricProperty .
                            ?x ?p ?y .
                        }
                    """)
                ]
                
                # Apply OWL inference rules
                for rule in owl_rules:
                    self.graph.update(rule)
            case _:
                raise ValueError(f"Unsupported reasoner type: {reasoner_type}")

    def query(self, sparql_query: str) -> List[Dict[str, Any]]:
        results = self.graph.query(sparql_query)
        return [dict(zip(result.vars, [str(term) for term in result])) for result in results]

    def save(self, file_path: str):
        self.graph.serialize(destination=file_path, format="turtle")

    def load(self, file_path: str):
        self.graph.parse(file_path, format="turtle")
        # Populate concepts, relationships, and terms from the loaded graph
        
# Test the class
onto = Ontology()
print(onto)