from typing import List, Dict, Any
from rdflib import Graph, Literal, URIRef
from .ontology import Ontology

class KnowledgeRepresentation:
    def __init__(self, ontology: Ontology):
        self.ontology = ontology
        self.graph = Graph()
        self.graph.parse(ontology.file_path)

    def add_knowledge(self, knowledge: Dict[str, Any]):
        for subject, predicate, obj in knowledge.items():
            self.graph.add((URIRef(subject), URIRef(predicate), Literal(obj)))

    def get_knowledge(self, subject: str, predicate: str) -> List[Any]:
        query = f"SELECT ?o WHERE {{ <{subject}> <{predicate}> ?o }}"
        results = self.graph.query(query)
        return [str(result[0]) for result in results]

    def remove_knowledge(self, subject: str, predicate: str, obj: str):
        self.graph.remove((URIRef(subject), URIRef(predicate), Literal(obj)))

    def integrate_knowledge(self):
        # Integrate new knowledge into the existing knowledge graph
        new_knowledge = self.get_new_knowledge()
        for subject, predicate, obj in new_knowledge:
            # Check if the subject and predicate already exist in the graph
            existing_objects = self.get_knowledge(subject, predicate)
            if obj not in existing_objects:
                # Add the new knowledge triple to the graph
                self.add_knowledge({subject: {predicate: obj}})
        
        # Perform reasoning and inference on the updated knowledge graph
        self.reason_and_infer()
        
        # Update the ontology if necessary based on the integrated knowledge
        self.update_ontology()

    def serialize(self, format: str = "turtle") -> str:
        return self.graph.serialize(format=format)
