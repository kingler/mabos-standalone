from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.knowledge_graph import KnowledgeGraph
from app.core.models.knowledge.knowledge_management import KnowledgeManagement

def create_knowledge_management(llm_manager, storage_backend, graph_database):
    knowledge_base = KnowledgeBase()
    knowledge_graph = KnowledgeGraph()
    return KnowledgeManagement(knowledge_base, knowledge_graph, llm_manager, storage_backend, graph_database)
