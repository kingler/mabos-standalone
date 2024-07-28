from uuid import uuid4
from pydantic import BaseModel, Field, model_validator, SkipValidation
from typing import List, Dict, Any, Optional, Union
import rapidfuzz
from rdflib import Graph, URIRef, OWL, RDF, RDFS
from owlready2 import World, ObjectProperty, DataProperty, AnnotationProperty
import networkx as nx
from .ontology_loader import OntologyLoader
from app.models.domain_ontology_generator import DomainOntologyGenerator
from app.models.custom_inference import CustomInference
from transformers import AutoTokenizer, AutoModel
import torch 

class URIRefField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, URIRef):
            return v
        if isinstance(v, str):
            return URIRef(v)
        raise ValueError('Invalid URIRef')

class Concept(BaseModel):
    name: str
    description: Optional[str] = None
    is_a: List[str] = Field(default_factory=list)
    properties: List[str] = Field(default_factory=list)
    relationships: List[str] = Field(default_factory=list)

class UncertainConcept(Concept):
    uncertainty: float

class Relationship(BaseModel):
    name: str
    description: Optional[str] = None
    domain: str
    range: str

class UncertainRelationship(Relationship):
    uncertainty: float

class Individual(BaseModel):
    name: str
    is_a: List[Concept]
    storid: URIRefField = Field(default_factory=lambda: URIRef(f"http://example.org/individual/{uuid4()}"))

    class Config:
        arbitrary_types_allowed = True

class Ontology(BaseModel):
    generator: DomainOntologyGenerator = Field(default_factory=lambda: DomainOntologyGenerator(world=World()))
    inference: CustomInference = Field(default_factory=lambda: CustomInference(world=World(), knowledge_graph=Graph()))
    concepts: List[Union[Concept, UncertainConcept]] = Field(default_factory=list, description="Domain concepts")
    relationships: List[Union[Relationship, UncertainRelationship]] = Field(default_factory=list, description="Relationships between concepts")
    ontology_path: Optional[str] = None
    world: World = Field(default_factory=World)
    graph: SkipValidation[Graph] = Field(default_factory=Graph)
    ontology_file: str = "/mabos-standalone/app/core/ontologies/business_ontology.owl"
    loader: Optional[OntologyLoader] = None

    class Config:
        arbitrary_types_allowed = True

    @model_validator(mode='before')
    def initialize_loader(cls, values):
        ontology_file = values.get('ontology_file')
        world = values.get('world', World())
        graph = values.get('graph', Graph())
        values['loader'] = OntologyLoader(world, graph)
        if ontology_file:
            print(f"Loading ontology from: {ontology_file}")
        return values

    def __init__(self, **data):
        print("Initializing Ontology with data:", data)
        super().__init__(**data)
        print("Ontology initialized successfully")

    def load_ontology(self, ontology_path: Optional[str] = None) -> None:
        self.loader.load_ontology(ontology_path or self.ontology_file)

    def get_classes(self) -> List[str]:
        return self.loader.get_classes()

    def get_properties(self) -> List[str]:
        return self.loader.get_properties()

    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        return self.loader.query_ontology(query)

    def generate_domain_ontology(self, user_data: Dict[str, Any]) -> None:
        concepts = user_data.get("concepts", [])
        relationships = user_data.get("relationships", [])
        
        for concept_data in concepts:
            concept = Concept(**concept_data)
            self.world.create_class(concept.name)
        
        for relationship_data in relationships:
            relationship = Relationship(**relationship_data)
            domain_class = self.world[relationship.domain]
            range_class = self.world[relationship.range]
            with domain_class:
                ObjectProperty(relationship.name, range=range_class)
        
        self.apply_domain_rules(user_data)

    def apply_domain_rules(self, user_data: Dict[str, Any]) -> None:
        rules = user_data.get("domain_rules", [])
        
        for rule in rules:
            self._apply_rule(rule)
        
        self.world.save()
        self.graph = self.world.as_rdflib_graph()
        self.loader = OntologyLoader(self.world, self.graph)

    def _apply_rule(self, rule: Dict[str, Any]) -> None:
        if rule["type"] == "subclass":
            self.world[rule["subclass"]].is_a.append(self.world[rule["superclass"]])
        elif rule["type"] == "property":
            self._apply_property_rule(rule)
        elif rule["type"] == "restriction":
            self._apply_restriction_rule(rule)
        elif rule["type"] == "axiom":
            self._apply_axiom_rule(rule)

    def _apply_property_rule(self, rule: Dict[str, Any]) -> None:
        with self.world[rule["domain"]]:
            if rule["property_type"] == "object":
                ObjectProperty(rule["name"], range=self.world[rule["range"]])
            elif rule["property_type"] == "data":
                DataProperty(rule["name"], range=rule["datatype"])

    def _apply_restriction_rule(self, rule: Dict[str, Any]) -> None:
        with self.world[rule["class"]]:
            if rule["restriction_type"] == "some":
                self.world[rule["class"]].is_a.append(
                    self.world[rule["property"]].some(self.world[rule["filler"]])
                )
            elif rule["restriction_type"] == "only":
                self.world[rule["class"]].is_a.append(
                    self.world[rule["property"]].only(self.world[rule["filler"]])
                )

    def _apply_axiom_rule(self, rule: Dict[str, Any]) -> None:
        self.graph.add((
            self.world[rule["subject"]].storid,
            self.world[rule["predicate"]].storid,
            self.world[rule["object"]].storid
        ))
    def apply_custom_inference_rules(self) -> None:
        Rules = [
            """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            
            INSERT {
                ?subClass rdfs:subClassOf ?superClass .
            }
            WHERE {
                ?subClass rdfs:subClassOf ?intermediateClass .
                ?intermediateClass rdfs:subClassOf ?superClass .
            }
            """
        ]
        
        for rule in Rules:
            self.graph.update(rule)

    def visualize_ontology(self) -> nx.DiGraph:
        graph = nx.DiGraph()

        for class_name in self.get_classes():
            graph.add_node(class_name, type='class')

        for property_name in self.get_properties():
            domain, range = self.loader.get_property_domain_range(property_name)
            graph.add_node(property_name, type='property')
            graph.add_edge(domain, property_name)
            graph.add_edge(property_name, range)

        return graph
    
    def align_with(self, other_ontology: 'Ontology') -> None:
        self_classes = set(self.get_classes())
        other_classes = set(other_ontology.get_classes())
        self_properties = set(self.get_properties())
        other_properties = set(other_ontology.get_properties())
        
        common_classes = self_classes.intersection(other_classes)
        common_properties = self_properties.intersection(other_properties)
        
        class_mappings = {c: c for c in common_classes}
        property_mappings = {p: p for p in common_properties}
        
        lexical_mappings = self._lexical_matching(self_classes.union(self_properties), other_classes.union(other_properties))
        class_mappings.update({k: v for k, v in lexical_mappings.items() if k in self_classes and v in other_classes})
        property_mappings.update({k: v for k, v in lexical_mappings.items() if k in self_properties and v in other_properties})
        
        structural_mappings = self._structural_matching(other_ontology)
        class_mappings.update({k: v for k, v in structural_mappings.items() if k in self_classes and v in other_classes})
        property_mappings.update({k: v for k, v in structural_mappings.items() if k in self_properties and v in other_properties})
        
        semantic_mappings = self._semantic_matching(other_ontology)
        class_mappings.update({k: v for k, v in semantic_mappings.items() if k in self_classes and v in other_classes})
        property_mappings.update({k: v for k, v in semantic_mappings.items() if k in self_properties and v in other_properties})
        
        for self_class, other_class in class_mappings.items():
            self.graph.add((URIRef(self.loader.get_class_uri(self_class)), OWL.equivalentClass, URIRef(other_ontology.loader.get_class_uri(other_class))))
        
        for self_prop, other_prop in property_mappings.items():
            self.graph.add((URIRef(self.loader.get_property_uri(self_prop)), OWL.equivalentProperty, URIRef(other_ontology.loader.get_property_uri(other_prop))))

    def merge_with(self, other_ontology: 'Ontology') -> None:
        self.align_with(other_ontology)
        
        for concept in other_ontology.concepts:
            if concept.name not in [c.name for c in self.concepts]:
                self.concepts.append(concept)
                self.graph.add((URIRef(self.loader.get_class_uri(concept.name)), RDF.type, OWL.Class))
        
        for relationship in other_ontology.relationships:
            if relationship.name not in [r.name for r in self.relationships]:
                self.relationships.append(relationship)
                self.graph.add((URIRef(self.loader.get_property_uri(relationship.name)), RDF.type, OWL.ObjectProperty))
                self.graph.add((URIRef(self.loader.get_property_uri(relationship.name)), RDFS.domain, URIRef(self.loader.get_class_uri(relationship.domain))))
                self.graph.add((URIRef(self.loader.get_property_uri(relationship.name)), RDFS.range, URIRef(self.loader.get_class_uri(relationship.range))))

        for individual in other_ontology.world.individuals():
            if individual not in self.world.individuals():
                new_individual = self.world.create_individual(individual.name, individual.is_a)
                for prop, values in individual.get_properties().items():
                    for value in values:
                        new_individual.__setattr__(prop.python_name, value)

        for data_prop in other_ontology.world.data_properties():
            if data_prop not in self.world.data_properties():
                new_data_prop = DataProperty(data_prop.name)
                new_data_prop.domain = data_prop.domain
                new_data_prop.range = data_prop.range

        for annot_prop in other_ontology.world.annotation_properties():
            if annot_prop not in self.world.annotation_properties():
                AnnotationProperty(annot_prop.name)

        for rule in other_ontology.world.rules():
            if rule not in self.world.rules():
                self.world.rule(rule.name, rule.body, rule.head)

        self.world.save()
        self.graph = self.world.as_rdflib_graph()
        self.loader = OntologyLoader(self.world, self.graph)

    def _lexical_matching(self, self_elements: set, other_elements: set) -> Dict[str, str]:
        matches = {}
        for self_elem in self_elements:
            best_match = None
            best_score = 0
            for other_elem in other_elements:
                score = rapidfuzz.fuzz.ratio(self_elem.lower(), other_elem.lower())
                if score > best_score:
                    best_score = score
                    best_match = other_elem
            
            if best_score >= 80:
                matches[self_elem] = best_match
        
        return matches

    def _structural_matching(self, other_ontology: 'Ontology') -> Dict[str, str]:
        matches = {}
        
        def get_concept_structure(concept):
            return {
                'parents': [str(parent) for parent in concept.is_a],
                'properties': [str(prop) for prop in concept.get_properties()],
                'relationships': [r.name for r in self.relationships if r.domain == concept.name or r.range == concept.name]
            }
        
        for self_concept in self.concepts:
            self_structure = get_concept_structure(self_concept)
            best_match = None
            best_score = 0
            
            for other_concept in other_ontology.concepts:
                other_structure = get_concept_structure(other_concept)
                
                parents_sim = len(set(self_structure['parents']) & set(other_structure['parents'])) / max(len(self_structure['parents']), len(other_structure['parents']), 1)
                props_sim = len(set(self_structure['properties']) & set(other_structure['properties'])) / max(len(self_structure['properties']), len(other_structure['properties']), 1)
                rels_sim = len(set(self_structure['relationships']) & set(other_structure['relationships'])) / max(len(self_structure['relationships']), len(other_structure['relationships']), 1)
                
                similarity_score = (parents_sim + props_sim + rels_sim) / 3
                
                if similarity_score > best_score:
                    best_score = similarity_score
                    best_match = other_concept.name
            
            if best_match and best_score > 0.5:
                matches[self_concept.name] = best_match
        
        return matches

    def _semantic_matching(self, other_ontology: 'Ontology') -> Dict[str, str]:
        def string_similarity(str1, str2):
            return rapidfuzz.ratio(str1, str2)

        def structural_similarity(concept1, concept2, ontology1, ontology2):
            structure1 = self._extract_structure(concept1)
            structure2 = other_ontology._extract_structure(concept2)
            return self._compare_structures(structure1, structure2)

        def _extract_structure(self, concept):
            return {
                'parents': [str(parent) for parent in concept.is_a],
                'properties': [str(prop) for prop in concept.get_properties()]
            }

        def _compare_structures(self, structure1, structure2):
            parents_sim = len(set(structure1['parents']) & set(structure2['parents'])) / max(len(structure1['parents']), len(structure2['parents']), 1)
            props_sim = len(set(structure1['properties']) & set(structure2['properties'])) / max(len(structure1['properties']), len(structure2['properties']), 1)
            return (parents_sim + props_sim) / 2

        def load_model(model_name='bert-base-uncased'):
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModel.from_pretrained(model_name)
            return tokenizer, model

        def embed_text(text, tokenizer, model):
            inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
            with torch.no_grad():
                outputs = model(**inputs)
            return outputs.last_hidden_state.mean(dim=1)

        def semantic_similarity(concept1, concept2, tokenizer, model):
            embedding1 = embed_text(str(concept1), tokenizer, model)
            embedding2 = embed_text(str(concept2), tokenizer, model)
            return torch.cosine_similarity(embedding1, embedding2).item()

        def hybrid_matching(concept1, concept2, tokenizer, model):
            string_sim = string_similarity(str(concept1), str(concept2))
            struct_sim = structural_similarity(concept1, concept2, self, other_ontology)
            sem_sim = semantic_similarity(concept1, concept2, tokenizer, model)
            return 0.3 * string_sim + 0.3 * struct_sim + 0.4 * sem_sim

        tokenizer, model = load_model()
        matched_elements = {}

        for concept1 in self.world.classes():
            best_match = None
            best_score = 0
            for concept2 in other_ontology.world.classes():
                score = hybrid_matching(concept1, concept2, tokenizer, model)
                if score > best_score:
                    best_score = score
                    best_match = concept2
            if best_match and best_score > 0.7:
                matched_elements[str(concept1)] = str(best_match)

        return matched_elements