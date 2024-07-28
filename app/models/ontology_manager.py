from owlready2 import *
from typing import List, Dict
from app.models.ontology_types import OntologyStructure, QueryResult

class OntologyManager:
    """
    Manages ontology operations including loading, updating, querying, and saving.
    """

    def __init__(self, ontology_path: str):
        """
        Initialize the OntologyManager with the given ontology path.

        Args:
            ontology_path (str): The file path to the ontology.
        """
        self.ontology_path = ontology_path
        self.world = World()
        self.onto = self.world.get_ontology(f"file://{ontology_path}").load()
        self.graph = self.world.as_rdflib_graph()

    def update_ontology_from_generated(self, generated_ontology: OntologyStructure) -> None:
        """
        Update the ontology with generated ontology structure.

        Args:
            generated_ontology (OntologyStructure): The generated ontology structure to be added.

        Raises:
            KeyError: If required keys are missing in the generated_ontology.
            ValueError: If there are issues with the ontology elements.
        """
        required_keys = ['classes', 'properties', 'relationships', 'axioms']
        if not all(key in generated_ontology for key in required_keys):
            raise KeyError("Generated ontology is missing required keys.")

        with self.onto:
            # Add classes
            for class_name in generated_ontology['classes']:
                if not isinstance(class_name, str):
                    raise ValueError(f"Invalid class name: {class_name}")
                if class_name not in self.onto.classes():
                    types.new_class(class_name, (Thing,))

            # Add properties
            for prop in generated_ontology['properties']:
                if not isinstance(prop, str):
                    raise ValueError(f"Invalid property: {prop}")
                if prop not in self.onto.properties():
                    types.new_class(prop, (ObjectProperty,))

            # Add relationships
            for rel in generated_ontology['relationships']:
                if not all(key in rel for key in ['subject', 'predicate', 'object']):
                    raise KeyError(f"Invalid relationship structure: {rel}")
                subject = self.onto[rel['subject']]
                predicate = self.onto[rel['predicate']]
                obj = self.onto[rel['object']]
                if not all([subject, predicate, obj]):
                    raise ValueError(f"Invalid relationship elements: {rel}")
                predicate[subject].append(obj)

            # Add axioms (simplified representation)
            for axiom in generated_ontology['axioms']:
                if not isinstance(axiom, str):
                    raise ValueError(f"Invalid axiom: {axiom}")
                self.onto.add_annotation_property(axiom)

        self.save_ontology()

    def save_ontology(self) -> None:
        """
        Save the ontology to the file specified by ontology_path.
        """
        self.onto.save(file=self.ontology_path, format="rdfxml")

    def query_ontology(self, sparql_query: str) -> QueryResult:
        """
        Execute a SPARQL query on the ontology.

        Args:
            sparql_query (str): The SPARQL query string.

        Returns:
            QueryResult: The result of the SPARQL query.
        """
        return list(self.graph.query(sparql_query))

    def get_class_hierarchy(self) -> List[str]:
        """
        Get the class hierarchy of the ontology.

        Returns:
            List[str]: A list of class names in the ontology.
        """
        return [c.name for c in self.onto.classes()]

    def get_properties(self) -> List[str]:
        """
        Get all properties in the ontology.

        Returns:
            List[str]: A list of property names in the ontology.
        """
        return [p.name for p in self.onto.properties()]

    def get_individuals(self, class_name: str) -> List[str]:
        """
        Get all individuals of a specific class.

        Args:
            class_name (str): The name of the class.

        Returns:
            List[str]: A list of individual names for the specified class.

        Raises:
            KeyError: If the specified class does not exist in the ontology.
        """
        if class_name not in self.onto.classes():
            raise KeyError(f"Class '{class_name}' does not exist in the ontology.")
        return [i.name for i in self.onto[class_name].instances()]

    def add_individual(self, class_name: str, individual_name: str) -> None:
        """
        Add a new individual to a specific class.

        Args:
            class_name (str): The name of the class to add the individual to.
            individual_name (str): The name of the individual to add.

        Raises:
            KeyError: If the specified class does not exist in the ontology.
            ValueError: If the individual already exists in the ontology.
        """
        if class_name not in self.onto.classes():
            raise KeyError(f"Class '{class_name}' does not exist in the ontology.")
        if individual_name in self.onto.individuals():
            raise ValueError(f"Individual '{individual_name}' already exists in the ontology.")
        with self.onto:
            self.onto[class_name](individual_name)
        self.save_ontology()

    def remove_individual(self, individual_name: str) -> None:
        """
        Remove an individual from the ontology.

        Args:
            individual_name (str): The name of the individual to remove.

        Raises:
            KeyError: If the specified individual does not exist in the ontology.
        """
        if individual_name not in self.onto.individuals():
            raise KeyError(f"Individual '{individual_name}' does not exist in the ontology.")
        with self.onto:
            destroy_entity(self.onto[individual_name])
        self.save_ontology()

    def get_class_relations(self, class_name: str) -> Dict[str, List[str]]:
        """
        Get all relations (object properties) for a specific class.

        Args:
            class_name (str): The name of the class.

        Returns:
            Dict[str, List[str]]: A dictionary where keys are relation names and values are lists of related class names.

        Raises:
            KeyError: If the specified class does not exist in the ontology.
        """
        if class_name not in self.onto.classes():
            raise KeyError(f"Class '{class_name}' does not exist in the ontology.")
        
        relations = {}
        for prop in self.onto.object_properties():
            domain = prop.domain
            range = prop.range
            if class_name in [c.name for c in domain]:
                relations[prop.name] = [c.name for c in range]
        return relations