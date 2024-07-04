from typing import List, Dict, Any, Optional, Tuple
from pydantic import BaseModel, Field
from rdflib import OWL, RDF, RDFS, Graph
from owlready2 import World
from .ontology_loader import OntologyLoader
from app.core.domain_ontology_generator import DomainOntologyGenerator
from app.core.custom_inference import CustomInference

class Concept(BaseModel):
    name: str
    description: Optional[str] = None

class Relationship(BaseModel):
    name: str
    domain: str
    range: str
    description: Optional[str] = None

class Ontology(BaseModel):
    concepts: List[Concept] = Field(description="Domain concepts")
    relationships: List[Relationship] = Field(description="Relationships between concepts")
    ontology_path: Optional[str] = None

    def __init__(self, ontology_path: Optional[str] = None, world: Optional[World] = None, graph: Optional[Graph] = None):
        super().__init__()
        self.ontology_path = ontology_path
        self.world = world or World()
        self.graph = graph or Graph()
        self.loader = OntologyLoader(self.world, self.graph)
        self.generator = DomainOntologyGenerator(self.world)
        self.inference = CustomInference(self.world)

    def load_ontology(self, ontology_path: Optional[str] = None) -> None:
        """
        Load the ontology from the given path.
        
        Args:
            ontology_path (Optional[str]): The path to the ontology file.
        """
        if ontology_path:
            self.ontology_path = ontology_path
        
        if self.ontology_path:
            self.loader.load_ontology(self.ontology_path)
        else:
            raise ValueError("No ontology path provided.")

    def get_classes(self) -> List[str]:
        return [cls.name for cls in self.world.classes()]

    def get_properties(self) -> List[str]:
        return [prop.name for prop in self.world.properties()]

    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        results = self.graph.query(query)
        return [dict(zip(row.labels, row)) for row in results]
        
        
    def generate_domain_ontology(self, user_data: Dict[str, Any]) -> None:
        """
        Generate a domain ontology based on user data.
        
        Args:
            user_data (Dict[str, Any]): The user data to generate the ontology.
        """
        # Extract relevant information from user data
        concepts = user_data.get("concepts", [])
        relationships = user_data.get("relationships", [])
        
        # Create concepts in the ontology
        for concept_data in concepts:
            concept = Concept(**concept_data)
            self.world.create_class(concept.name)
        
        # Create relationships between concepts
        for relationship_data in relationships:
            relationship = Relationship(**relationship_data)
            self.world.create_property(relationship.name, relationship.domain, relationship.range)
        
        # Apply any additional domain-specific rules or constraints
        self.apply_domain_rules(user_data)

    def apply_custom_inference_rules(self) -> None:
        """
        Apply custom inference rules to the ontology.
        """
        # Define custom inference rules
        rules = [
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
            """,
            # Add more custom inference rules here
        ]
        
        # Apply each custom inference rule
        for rule in rules:
            self.graph.update(rule)

    def visualize_ontology(self) -> Any:
        """
        Visualize the ontology as a directed graph.
        
        Returns:
            Any: The directed graph representation of the ontology.
        """
        import networkx as nx

        graph = nx.DiGraph()

        # Add nodes for classes
        for class_name in self.get_classes():
            graph.add_node(class_name, type='class')

        # Add nodes and edges for properties
        for property_name in self.get_properties():
            domain, range = self.loader.get_property_domain_range(property_name)
            graph.add_node(property_name, type='property')
            graph.add_edge(domain, property_name)
            graph.add_edge(property_name, range)

        return graph
    
    def align_with(self, other_ontology: 'Ontology'):
        """
        Align this ontology with another ontology.
        
        Args:
            other_ontology (Ontology): The ontology to align with.
        """
        # Get the classes and properties from both ontologies
        self_classes = set(self.get_classes())
        other_classes = set(other_ontology.get_classes())
        self_properties = set(self.get_properties())
        other_properties = set(other_ontology.get_properties())
        
        # Find the common classes and properties
        common_classes = self_classes.intersection(other_classes)
        common_properties = self_properties.intersection(other_properties)
        
        # Create alignment mappings
        class_mappings = {c: c for c in common_classes}
        property_mappings = {p: p for p in common_properties}
        
        # TODO: Implement more advanced alignment techniques, such as:
        # - Lexical matching of class and property names
        # - Structural matching based on class hierarchies and property domains/ranges
        # - Semantic matching using external knowledge sources
        
        # Apply the alignment mappings to the current ontology
        for self_class, other_class in class_mappings.items():
            self.graph.add((self.loader.get_class_uri(self_class), OWL.equivalentClass, other_ontology.loader.get_class_uri(other_class)))
        
        for self_prop, other_prop in property_mappings.items():
            self.graph.add((self.loader.get_property_uri(self_prop), OWL.equivalentProperty, other_ontology.loader.get_property_uri(other_prop)))

    def merge_with(self, other_ontology: 'Ontology'):
        """
        Merge this ontology with another ontology.
        
        Args:
            other_ontology (Ontology): The ontology to merge with.
        """
        # Align the ontologies before merging
        self.align_with(other_ontology)
        
        # Add concepts from the other ontology
        for concept in other_ontology.concepts:
            if concept.name not in [c.name for c in self.concepts]:
                self.concepts.append(concept)
                self.graph.add((self.loader.get_class_uri(concept.name), RDF.type, OWL.Class))
        
        # Add relationships from the other ontology
        for relationship in other_ontology.relationships:
            if relationship.name not in [r.name for r in self.relationships]:
                self.relationships.append(relationship)
                self.graph.add((self.loader.get_property_uri(relationship.name), RDF.type, OWL.ObjectProperty))
                self.graph.add((self.loader.get_property_uri(relationship.name), RDFS.domain, self.loader.get_class_uri(relationship.domain)))
                self.graph.add((self.loader.get_property_uri(relationship.name), RDFS.range, self.loader.get_class_uri(relationship.range)))
        
        # TODO: Handle merging of individuals and other ontology elements
        
        # Update the ontology loader to include the merged elements
        self.loader = OntologyLoader(self.graph)
