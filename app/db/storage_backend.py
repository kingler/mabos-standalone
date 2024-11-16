import logging
from typing import Dict, Any, List
from app.agents.core_agents.llm_agent import LLMAgent
from app.db.arangodb import get_arango_client, get_arango_db, ensure_collections
from app.tools.togaf_questions import generate_db_name

class StorageBackend:
    def __init__(self, business_name: str, llm_agent: LLMAgent):
        self.db = get_arango_db()
        ensure_collections(self.db)
        self.db_name = generate_db_name(business_name, llm_agent)

    def create_collection(self, collection_name: str):
        """Create a collection if it doesn't exist."""
        try:
            if not self.db.has_collection(collection_name):
                collection = self.db.create_collection(collection_name)
                logging.info(f"Created collection: {collection_name}")
                return collection
            return self.db.collection(collection_name)
        except Exception as e:
            logging.error(f"Error creating collection {collection_name}: {str(e)}")
            raise

    def insert_document(self, collection_name: str, document: Dict[str, Any]):
        """Insert a document into a collection."""
        try:
            collection = self.create_collection(collection_name)
            result = collection.insert(document)
            logging.info(f"Inserted document into {collection_name}")
            return result
        except Exception as e:
            logging.error(f"Error inserting document: {str(e)}")
            raise

    def get_document(self, collection_name: str, key: str):
        """Get a document by key from a collection."""
        try:
            collection = self.db.collection(collection_name)
            return collection.get(key)
        except Exception as e:
            logging.error(f"Error getting document: {str(e)}")
            raise

    def update_document(self, collection_name: str, key: str, update_data: Dict[str, Any]):
        """Update a document in a collection."""
        try:
            collection = self.db.collection(collection_name)
            result = collection.update_match({'_key': key}, update_data)
            logging.info(f"Updated document in {collection_name}")
            return result
        except Exception as e:
            logging.error(f"Error updating document: {str(e)}")
            raise

    def delete_document(self, collection_name: str, key: str) -> bool:
        """Delete a document from a collection."""
        try:
            collection = self.db.collection(collection_name)
            collection.delete(key)
            logging.info(f"Deleted document from {collection_name}")
            return True
        except Exception as e:
            logging.error(f"Error deleting document: {str(e)}")
            raise

    def query(self, aql_query: str, bind_vars: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Execute an AQL query."""
        try:
            cursor = self.db.aql.execute(aql_query, bind_vars=bind_vars)
            return [doc for doc in cursor]
        except Exception as e:
            logging.error(f"Error executing query: {str(e)}")
            raise

class GraphDatabase(StorageBackend):
    def __init__(self, business_name: str, llm_agent: LLMAgent):
        super().__init__(business_name, llm_agent)

    def create_vertex(self, collection_name: str, vertex_data: Dict[str, Any]):
        """Create a vertex in a collection."""
        return self.insert_document(collection_name, vertex_data)

    def create_edge(self, edge_collection_name: str, from_vertex: str, to_vertex: str, edge_data: Dict[str, Any]):
        """Create an edge between vertices."""
        try:
            # Ensure edge collection exists
            if not self.db.has_collection(edge_collection_name):
                collection = self.db.create_collection(edge_collection_name, edge=True)
                logging.info(f"Created edge collection: {edge_collection_name}")
            else:
                collection = self.db.collection(edge_collection_name)

            # Create edge document
            edge_doc = {
                '_from': from_vertex,
                '_to': to_vertex,
                **edge_data
            }
            result = collection.insert(edge_doc)
            logging.info(f"Created edge in {edge_collection_name}")
            return result
        except Exception as e:
            logging.error(f"Error creating edge: {str(e)}")
            raise

    def get_neighbors(self, vertex_id: str, edge_collection_name: str, direction: str = "outbound") -> List[Dict[str, Any]]:
        """Get neighbors of a vertex."""
        aql_query = f"""
        FOR v, e IN 1..1 {direction} '{vertex_id}'
        GRAPH '{edge_collection_name}'
        RETURN {{vertex: v, edge: e}}
        """
        return self.query(aql_query)

    def shortest_path(self, start_vertex: str, end_vertex: str, edge_collection_name: str) -> List[Dict[str, Any]]:
        """Find shortest path between vertices."""
        aql_query = f"""
        FOR v, e IN OUTBOUND SHORTEST_PATH '{start_vertex}' TO '{end_vertex}'
        GRAPH '{edge_collection_name}'
        RETURN {{vertex: v, edge: e}}
        """
        return self.query(aql_query)
