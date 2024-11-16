import asyncio
import logging
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field, SkipValidation
from owlready2 import World
from app.models.knowledge.knowledge_graph import EnhancedKnowledgeGraph
from app.models.knowledge.ontology.ontology import Ontology
from app.models.knowledge.ontology.ontology_aligner import OntologyAligner
from app.models.knowledge.ontology.ontology_version_control import OntologyVersionControl
from app.tools.llm_manager import LLMManager
from app.db.arango_db_client import ArangoDBClient
from app.models.business.business_profile import BusinessProfile
from app.config.config import CONFIG
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.knowledge.ontology.domain_ontology_generator import DomainOntologyGenerator


class OntologyManager(BaseModel):
    llm_manager: Optional[LLMManager] = None
    db_client: Optional[ArangoDBClient] = None
    graph_database: Optional[ArangoDBClient] = None
    version_control: Optional[OntologyVersionControl] = None
    graph_integrator: Optional[EnhancedKnowledgeGraph] = None
    aligner: Optional[OntologyAligner] = None
    nl_interface: Optional[Any] = None
    reasoner: Optional[Any] = None
    generator: Optional[DomainOntologyGenerator] = None
    knowledge_base: Optional[KnowledgeBase] = None
    world: Optional[World] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def create(cls, llm_manager: LLMManager, db_client: ArangoDBClient) -> 'OntologyManager':
        try:
            # Initialize version control
            version_control = OntologyVersionControl(repo_path=CONFIG.ontology_repo_path)
            
            # Initialize aligner
            aligner = OntologyAligner(llm_manager)
            
            # Initialize knowledge base
            knowledge_base = KnowledgeBase()
            
            # Initialize World instance
            world = World()
            world.get_ontology(CONFIG.ontology_path).load()
            
            # Initialize ontology generator
            generator = DomainOntologyGenerator(world=world, llm_manager=llm_manager)
            
            # Create instance with all components
            instance = cls(
                llm_manager=llm_manager,
                db_client=db_client,
                graph_database=db_client,
                version_control=version_control,
                aligner=aligner,
                generator=generator,
                knowledge_base=knowledge_base,
                world=world
            )
            
            # Initialize graph integrator after other components are ready
            instance.graph_integrator = EnhancedKnowledgeGraph(
                db_client=db_client,
                llm_manager=llm_manager,
                ontology_generator=generator,
                knowledge_base=knowledge_base
            )
            
            return instance
            
        except Exception as e:
            logging.error(f"Error initializing OntologyManager: {str(e)}")
            raise

    async def create_ontology(self, business_description: str) -> Ontology:
        try:
            if not self.generator:
                logging.error("Ontology generator not initialized")
                raise ValueError("Ontology generator not initialized")
                
            ontology = await self.generator.generate_ontology(business_description)
            refined_ontology = await self.generator.refine_ontology(ontology)
            if await self.validate_ontology(refined_ontology):
                self.update_components(refined_ontology, version="1.0", source="initial_generation")
                return refined_ontology
            raise ValueError("Generated ontology failed validation")
        except Exception as e:
            logging.error(f"Error creating ontology: {str(e)}")
            raise

    async def update_ontology(self, updates: Dict[str, Any]) -> Ontology:
        try:
            current_ontology = self.version_control.get_version("latest")
            updated_ontology = current_ontology.apply_updates(updates)
            if await self.validate_ontology(updated_ontology):
                self.update_components(updated_ontology, version="increment", source="manual_update")
                return updated_ontology
            raise ValueError("Updated ontology failed validation")
        except Exception as e:
            logging.error(f"Error updating ontology: {str(e)}")
            raise

    async def validate_ontology(self, ontology: Ontology) -> bool:
        try:
            if not self.generator:
                logging.error("Ontology generator not initialized")
                raise ValueError("Ontology generator not initialized")
                
            validation_report = await self.generator.validate_ontology(ontology)
            return validation_report['is_valid']
        except Exception as e:
            logging.error(f"Error validating ontology: {str(e)}")
            raise

    def update_components(self, ontology: Ontology, version: str, source: str):
        try:
            if self.version_control:
                self.version_control.save_version(ontology, version, {"source": source})
            if self.graph_integrator:
                self.graph_integrator.merge_ontology(ontology)
            if self.nl_interface:
                self.nl_interface.ontology = ontology
            if self.reasoner:
                self.reasoner.ontology = ontology
        except Exception as e:
            logging.error(f"Error updating components: {str(e)}")
            raise

    async def process_nl_command(self, command: str) -> str:
        try:
            if self.nl_interface:
                return await self.nl_interface.process_command(command)
            return ""
        except Exception as e:
            logging.error(f"Error processing NL command: {str(e)}")
            raise

    async def perform_reasoning(self, query: str) -> str:
        try:
            if self.reasoner:
                return await self.reasoner.answer_query(query)
            return ""
        except Exception as e:
            logging.error(f"Error performing reasoning: {str(e)}")
            raise
    
    def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        """Execute a query against the ontology."""
        try:
            return self.graph_database.query(query)
        except Exception as e:
            logging.error(f"Error querying ontology: {str(e)}")
            return []
    
    def add_individual(self, individual_id: str, class_type: str):
        """Add an individual to the ontology."""
        try:
            self.graph_database.create_vertex('individuals', {
                'id': individual_id,
                'type': class_type
            })
        except Exception as e:
            logging.error(f"Error adding individual: {str(e)}")
    
    def update_property(self, subject: str, predicate: str, object: Any):
        """Update a property in the ontology."""
        try:
            self.graph_database.create_edge(
                'properties',
                f'individuals/{subject}',
                f'individuals/{object}',
                {'predicate': predicate}
            )
        except Exception as e:
            logging.error(f"Error updating property: {str(e)}")

async def initialize_ontology_manager():
    try:
        llm_manager = LLMManager()
        business_profile = await BusinessProfile.get_current()
        db_client = ArangoDBClient(
            host=CONFIG.ARANGO_HOST,
            port=CONFIG.ARANGO_PORT,
            username=CONFIG.ARANGO_USER,
            password=CONFIG.ARANGO_PASSWORD,
            database=CONFIG.ARANGO_DATABASE
        )
        
        return OntologyManager.create(
            llm_manager=llm_manager,
            db_client=db_client
        )
    except Exception as e:
        logging.error(f"Error initializing ontology manager: {str(e)}")
        raise

async def main():
    try:
        ontology_manager = await initialize_ontology_manager()
        # Add any other initialization or usage of ontology_manager here
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
