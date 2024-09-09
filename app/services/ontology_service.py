from typing import Any, Dict, List, Optional

from app.models.knowledge.ontology.ontology import (Concept, Ontology,
                                                         Relationship)
from app.models.knowledge.ontology.ontology_generator import OntologyVersionControl
from app.models.knowledge.ontology.ontology_loader import OntologyLoader
from app.config.config import get_settings
from app.models.knowledge.ontology.ontology_version_control import OntologyVersionControl


class OntologyService:
    def __init__(self):
        settings = get_settings()
        repo_path = settings.ontology_repo_path
        self.ontology_vc = OntologyVersionControl(repo_path)

    def load_ontology(self, ontology_path: str) -> Ontology:
        loader = OntologyLoader()
        loader.load_ontology(ontology_path)
        self.ontology = Ontology(
            concepts=[Concept(name=str(cls)) for cls in loader.get_classes()],
            relationships=[Relationship(name=str(prop), domain=str(loader.get_property_domain_range(prop)[0]), range=str(loader.get_property_domain_range(prop)[1])) for prop in loader.get_properties()],
            ontology_path=ontology_path
        )
        return self.ontology

    def get_classes(self) -> List[str]:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        return [concept.name for concept in self.ontology.concepts]

    def get_properties(self) -> List[str]:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        return [relationship.name for relationship in self.ontology.relationships]

    def add_concept(self, concept: Concept) -> Ontology:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        self.ontology.concepts.append(concept)
        return self.ontology

    def add_relationship(self, relationship: Relationship) -> Ontology:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        self.ontology.relationships.append(relationship)
        return self.ontology

    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        loader = OntologyLoader()
        loader.load_ontology(self.ontology.ontology_path)
        return loader.query_ontology(query)