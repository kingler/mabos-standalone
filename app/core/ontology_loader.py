from typing import List, Dict, Any, Optional
from rdflib import Graph
from owlready2 import World

class OntologyLoader:
    def __init__(self, world: Optional[World] = None, graph: Optional[Graph] = None):
        self.world = world or World()
        self.graph = graph or Graph()
        self.onto = None

    def load_ontology(self, ontology_path: str) -> None:
        """
        Load an ontology from the given path.

        Args:
            ontology_path (str): The path to the ontology file.
        """
        try:
            self.onto = self.world.get_ontology(ontology_path).load()
            self.graph = self.world.as_rdflib_graph()
        except Exception as e:
            raise RuntimeError(f"Failed to load ontology from {ontology_path}: {e}")

    def get_classes(self) -> List[str]:
        """
        Get a list of classes in the ontology.

        Returns:
            List[str]: A list of class names.
        """
        if not self.onto:
            raise RuntimeError("Ontology not loaded.")
        return [str(c) for c in self.onto.classes()]

    def get_properties(self) -> List[str]:
        """
        Get a list of properties in the ontology.

        Returns:
            List[str]: A list of property names.
        """
        if not self.onto:
            raise RuntimeError("Ontology not loaded.")
        return [str(p) for p in self.onto.properties()]

    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        """
        Query the ontology using SPARQL.

        Args:
            query (str): The SPARQL query string.

        Returns:
            List[Dict[str, Any]]: A list of query results.
        """
        if not self.graph:
            raise RuntimeError("Graph not initialized.")
        try:
            results = self.graph.query(query)
            return [{str(var): str(value) for var, value in result.items()} for result in results]
        except Exception as e:
            raise RuntimeError(f"Failed to query ontology: {e}")