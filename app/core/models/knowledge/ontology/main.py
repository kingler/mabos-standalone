import asyncio

from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.knowledge_graph import KnowledgeGraph
from app.core.models.knowledge.ontology.ontology_manager import OntologyManager
from app.core.services.db.database import SessionLocal
from app.core.tools.llm_manager import LLMManager


async def main():
    llm_manager = LLMManager()
    storage_backend = SessionLocal()
    graph_database = KnowledgeGraph(KnowledgeBase())
    
    ontology_manager = OntologyManager(llm_manager, storage_backend, graph_database)
    
    initial_ontology = await ontology_manager.create_ontology("An e-commerce platform selling electronics")
    print("Initial ontology created:", initial_ontology)
    
    update_result = await ontology_manager.process_nl_command("Add a new concept 'Smartphone' as a subclass of 'Electronics'")
    print("Ontology updated:", update_result)
    
    reasoning_result = await ontology_manager.perform_reasoning("What are the potential relationships between 'Smartphone' and 'Customer'?")
    print("Reasoning result:", reasoning_result)

if __name__ == "__main__":
    asyncio.run(main())
