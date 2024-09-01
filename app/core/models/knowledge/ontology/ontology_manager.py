import asyncio
from typing import Any, Dict
from pydantic import BaseModel, ConfigDict, Field, SkipValidation
from app.core.models.knowledge.knowledge_graph import KnowledgeGraphIntegrator
from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.models.knowledge.ontology.ontology_aligner import OntologyAligner
from app.core.models.knowledge.ontology.ontology_version_control import OntologyVersionControl
from app.core.tools.llm_manager import LLMManager
from app.db.storage_backend import GraphDatabase, StorageBackend
from app.core.models.business.business_profile import BusinessProfile
from app.config.config import get_settings

class OntologyManager(BaseModel):
    llm_manager: LLMManager
    storage_backend: StorageBackend
    graph_database: GraphDatabase
    version_control: OntologyVersionControl = Field(init=False)

    model_config = ConfigDict(arbitrary_types_allowed=True, protected_namespaces=())

    def __init__(self, llm_manager: LLMManager, storage_backend: StorageBackend, graph_database: GraphDatabase):
        super().__init__(llm_manager=llm_manager, storage_backend=storage_backend, graph_database=graph_database)
        settings = get_settings()
        repo_path = settings.ontology_repo_path
        self.version_control = OntologyVersionControl(repo_path)
        self.graph_integrator = KnowledgeGraphIntegrator(graph_database)
        self.aligner = OntologyAligner(llm_manager)
        self.nl_interface = None
        self.reasoner = None

    async def create_ontology(self, business_description: str) -> Ontology:
        ontology = await self.generator.generate_ontology(business_description)
        refined_ontology = await self.generator.refine_ontology(ontology)
        if await self.validate_ontology(refined_ontology):
            self.update_components(refined_ontology, version="1.0", source="initial_generation")
            return refined_ontology
        raise ValueError("Generated ontology failed validation")

    async def update_ontology(self, updates: Dict[str, Any]) -> Ontology:
        current_ontology = self.version_control.get_version("latest")
        updated_ontology = current_ontology.apply_updates(updates)
        if await self.validate_ontology(updated_ontology):
            self.update_components(updated_ontology, version="increment", source="manual_update")
            return updated_ontology
        raise ValueError("Updated ontology failed validation")

    async def validate_ontology(self, ontology: Ontology) -> bool:
        validation_report = await self.generator.validate_ontology(ontology)
        return validation_report['is_valid']

    def update_components(self, ontology: Ontology, version: str, source: str):
        self.version_control.save_version(ontology, version, {"source": source})
        self.graph_integrator.update_graph_from_ontology(ontology)
        self.nl_interface.ontology = ontology
        self.reasoner.ontology = ontology

    async def process_nl_command(self, command: str) -> str:
        return await self.nl_interface.process_command(command)

    async def perform_reasoning(self, query: str) -> str:
        return await self.reasoner.answer_query(query)
    
async def initialize_ontology_manager():
    llm_manager = LLMManager()
    business_profile = await BusinessProfile.get_current()
    storage_backend = StorageBackend(business_name=business_profile.name, llm_agent=llm_manager)
    graph_database = GraphDatabase()
    
    return OntologyManager(
        llm_manager=llm_manager,
        storage_backend=storage_backend,
        graph_database=graph_database
    )

async def main():
    ontology_manager = await initialize_ontology_manager()
    # Add any other initialization or usage of ontology_manager here

if __name__ == "__main__":
    asyncio.run(main())