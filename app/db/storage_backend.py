from app.db.arangodb import get_arango_client
from app.tools.togaf_questions import generate_db_name
from pyArango.collection import Collection
from pyArango.document import Document
from typing import Dict, Any, List
from app.agents.core_agents.llm_agent import LLMAgent

class StorageBackend:
    def __init__(self, business_name: str, llm_agent: LLMAgent):
        self.client = get_arango_client()
        self.db_name = generate_db_name(business_name, llm_agent)
        self.db = self.client[self.db_name]

    def create_collection(self, collection_name: str) -> Collection:
        if not self.db.hasCollection(collection_name):
            return self.db.createCollection(name=collection_name)
        return self.db[collection_name]

    def insert_document(self, collection_name: str, document: Dict[str, Any]) -> Document:
        collection = self.create_collection(collection_name)
        doc = collection.createDocument(document)
        doc.save()
        return doc

    def get_document(self, collection_name: str, key: str) -> Document:
        collection = self.db[collection_name]
        return collection[key]

    def update_document(self, collection_name: str, key: str, update_data: Dict[str, Any]) -> Document:
        doc = self.get_document(collection_name, key)
        doc.update(update_data)
        doc.save()
        return doc

    def delete_document(self, collection_name: str, key: str) -> bool:
        doc = self.get_document(collection_name, key)
        doc.delete()
        return True

    def query(self, aql_query: str, bind_vars: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        return self.db.AQLQuery(aql_query, bindVars=bind_vars, rawResults=True)

class GraphDatabase(StorageBackend):
    def __init__(self, business_name: str, llm_agent: LLMAgent):
        super().__init__(business_name, llm_agent)

    def create_vertex(self, collection_name: str, vertex_data: Dict[str, Any]) -> Document:
        return self.insert_document(collection_name, vertex_data)

    def create_edge(self, edge_collection_name: str, from_vertex: str, to_vertex: str, edge_data: Dict[str, Any]) -> Document:
        edge_collection = self.create_collection(edge_collection_name)
        edge = edge_collection.createEdge()
        edge._from = from_vertex
        edge._to = to_vertex
        edge.update(edge_data)
        edge.save()
        return edge

    def get_neighbors(self, vertex_id: str, edge_collection_name: str, direction: str = "outbound") -> List[Dict[str, Any]]:
        aql_query = f"""
        FOR v, e IN 1..1 {direction} '{vertex_id}'
        GRAPH '{edge_collection_name}'
        RETURN {{vertex: v, edge: e}}
        """
        return self.query(aql_query)

    def shortest_path(self, start_vertex: str, end_vertex: str, edge_collection_name: str) -> List[Dict[str, Any]]:
        aql_query = f"""
        FOR v, e IN OUTBOUND SHORTEST_PATH '{start_vertex}' TO '{end_vertex}'
        GRAPH '{edge_collection_name}'
        RETURN {{vertex: v, edge: e}}
        """
        return self.query(aql_query)