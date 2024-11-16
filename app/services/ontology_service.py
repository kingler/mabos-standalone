from typing import Any, Dict, List, Optional

from app.models.knowledge.ontology.ontology import (Concept, Ontology,
                                                         Relationship)
from app.models.knowledge.ontology.ontology_loader import OntologyLoader
from app.config.config import CONFIG
from app.models.knowledge.ontology.ontology_version_control import OntologyVersionControl
from app.tools.ontology_manager import OntologyManager
from app.tools.llm_manager import LLMManager
from app.db.arango_db_client import ArangoDBClient


class OntologyService:
    def __init__(self):
        self.ontology = None
        self.llm_manager = LLMManager()
        self.db_client = ArangoDBClient(
            host=CONFIG.ARANGO_HOST,
            port=CONFIG.ARANGO_PORT,
            username=CONFIG.ARANGO_USER,
            password=CONFIG.ARANGO_PASSWORD,
            database=CONFIG.ARANGO_DATABASE
        )
        self.ontology_manager = OntologyManager.create(
            llm_manager=self.llm_manager,
            db_client=self.db_client
        )

    def load_ontology(self, ontology_path: str) -> Ontology:
        loader = OntologyLoader()
        loader.load_ontology(ontology_path)
        
        # Get concepts as a dictionary
        concepts = loader.get_classes()
        
        # Get relationships as a dictionary
        relationships = {}
        for prop in loader.get_properties():
            prop_name = str(prop)
            domain, range_ = loader.get_property_domain_range(prop)
            relationship = Relationship(
                name=prop_name,
                source=str(domain) if domain else "",
                target=str(range_) if range_ else ""
            )
            relationships[prop_name] = relationship
        
        # Create the ontology with dictionaries
        self.ontology = Ontology(
            concepts=concepts,
            relationships=relationships,
            ontology_path=ontology_path
        )
        return self.ontology

    def get_classes(self) -> List[str]:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        return list(self.ontology.concepts.keys())

    def get_properties(self) -> List[str]:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        return list(self.ontology.relationships.keys())

    def add_concept(self, concept: Concept) -> Ontology:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        self.ontology.concepts[concept.name] = concept
        return self.ontology

    def add_relationship(self, relationship: Relationship) -> Ontology:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        self.ontology.relationships[relationship.name] = relationship
        return self.ontology

    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        return self.ontology_manager.query_ontology(query)

    async def generate_ontology(self, business_description: str) -> Ontology:
        """Generate a new ontology from a business description."""
        return await self.ontology_manager.create_ontology(business_description)

    async def refine_ontology(self, ontology: Ontology) -> Ontology:
        """Refine an existing ontology."""
        if not self.ontology_manager.generator:
            raise ValueError("Ontology generator not initialized.")
        return await self.ontology_manager.generator.refine_ontology(ontology)

    async def validate_ontology(self, ontology: Ontology) -> bool:
        """Validate an ontology."""
        return await self.ontology_manager.validate_ontology(ontology)

    def save_version(self, version: str, metadata: Dict[str, Any]):
        """Save a version of the current ontology."""
        if not self.ontology:
            raise ValueError("Ontology not loaded.")
        if not self.ontology_manager.version_control:
            raise ValueError("Version control not initialized.")
        self.ontology_manager.version_control.save_version(self.ontology, version, metadata)

    def get_version(self, version: str) -> Optional[Ontology]:
        """Get a specific version of the ontology."""
        if not self.ontology_manager.version_control:
            raise ValueError("Version control not initialized.")
        return self.ontology_manager.version_control.get_version(version)

    def compare_versions(self, version1: str, version2: str) -> Dict[str, Any]:
        """Compare two versions of the ontology."""
        if not self.ontology_manager.version_control:
            raise ValueError("Version control not initialized.")
        return self.ontology_manager.version_control.compare_versions(version1, version2)
