from owlready2 import *
from typing import List
from app.core.ontology_types import OntologyStructure, QueryResult

class OntologyManager:
    def __init__(self, ontology_path: str):
        self.ontology_path = ontology_path
        self.world = World()
        self.onto = self.world.get_ontology(f"file://{ontology_path}").load()
        self.graph = self.world.as_rdflib_graph()

    def update_ontology_from_generated(self, generated_ontology: OntologyStructure):
        with self.onto:
            # Add classes
            for class_name in generated_ontology['classes']:
                if class_name not in self.onto.classes():
                    types.new_class(class_name, (Thing,))

            # Add properties
            for prop in generated_ontology['properties']:
                if prop not in self.onto.properties():
                    types.new_class(prop, (ObjectProperty,))

            # Add relationships
            for rel in generated_ontology['relationships']:
                subject = self.onto[rel['subject']]
                predicate = self.onto[rel['predicate']]
                obj = self.onto[rel['object']]
                predicate[subject].append(obj)

            # Add axioms (simplified representation)
            for axiom in generated_ontology['axioms']:
                self.onto.add_annotation_property(axiom)

        self.save_ontology()

    def save_ontology(self):
        self.onto.save(file=self.ontology_path, format="rdfxml")

    def query_ontology(self, sparql_query: str) -> QueryResult:
        return list(self.graph.query(sparql_query))

    def get_class_hierarchy(self) -> List[str]:
        return [c.name for c in self.onto.classes()]

    def get_properties(self) -> List[str]:
        return [p.name for p in self.onto.properties()]

    def get_individuals(self, class_name: str) -> List[str]:
        return [i.name for i in self.onto[class_name].instances()]