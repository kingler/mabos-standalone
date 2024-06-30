from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from rdflib import Graph
from owlready2 import World
from .ontology_loader import OntologyLoader
from app.core.domain_ontology_generator import DomainOntologyGenerator
from app.core.custom_inference import CustomInference

class Ontology(BaseModel):
    concepts: List[str] = Field(description="Domain concepts")
    relationships: List[str] = Field(description="Relationships between concepts")
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
        self.loader.load_ontology(ontology_path or self.ontology_path)

    def get_classes(self) -> List[str]:
        """
        Get a list of classes in the ontology.

        Returns:
            List[str]: A list of class names.
        """
        return self.loader.get_classes()

    def get_properties(self) -> List[str]:
        """
        Get a list of properties in the ontology.

        Returns:
            List[str]: A list of property names.
        """
        return self.loader.get_properties()

    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        """
        Query the ontology using SPARQL.

        Args:
            query (str): The SPARQL query string.

        Returns:
            List[Dict[str, Any]]: A list of query results.
        """
    def generate_domain_ontology(self, user_data: Dict[str, Any]) -> None:
        """
        Generate a domain ontology based on user data.

        Args:
            user_data (Dict[str, Any]): The user data to generate the ontology.
        """
        self.generator.generate_domain_ontology(user_data)

    def apply_custom_inference_rules(self) -> None:
        """
        Apply custom inference rules to the ontology.
        """
        self.inference.apply_custom_inference_rules()

    def visualize_ontology(self) -> Any:
        """
        Visualize the ontology as a directed graph.

        Returns:
            Any: The directed graph representation of the ontology.
        """
        return self.world.as_digraph()    