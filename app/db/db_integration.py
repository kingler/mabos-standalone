from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from arango import ArangoClient
from dotenv import load_dotenv
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

load_dotenv()

class Answer(BaseModel):
    id: UUID
    content: str
    business_id: UUID

class Question(BaseModel):
    id: UUID
    content: str
    business_id: UUID

class SearchResult(BaseModel):
    movie: str
    cos_sim: float

class DatabaseIntegration:
    def __init__(self):
        self.url = os.getenv("ARANGO_URL", "http://localhost:8529")
        self.username = os.getenv("ARANGO_USERNAME", "root")
        self.password = os.getenv("ARANGO_PASSWORD", "yourpassword")
        self.database = os.getenv("ARANGO_DATABASE", "mabos-dbv01")
        self.client = None
        self.sys_db = None
        self.db = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.connect()

    def connect(self):
        try:
            # Create a client connection
            self.client = ArangoClient(hosts=self.url)
            
            # Connect to _system database first
            self.sys_db = self.client.db('_system', username=self.username, password=self.password)
            
            # Create target database if it doesn't exist
            if not self.sys_db.has_database(self.database):
                self.sys_db.create_database(self.database)
                logging.info(f"Created database: {self.database}")
            
            # Connect to the target database
            self.db = self.client.db(self.database, username=self.username, password=self.password)
            
            # Ensure required collections exist
            self.ensure_collections()
            logging.info(f"Connected to database: {self.database}")
            
        except Exception as e:
            logging.error(f"Error connecting to database: {str(e)}")
            raise

    def close(self):
        if self.client:
            self.client = None
            self.sys_db = None
            self.db = None
            logging.info("DatabaseIntegration connection closed")

    def execute_query(self, query: str, bind_vars: dict = None):
        if self.db is None:
            self.connect()  # Try to reconnect if connection is lost
            
        try:
            cursor = self.db.aql.execute(query, bind_vars=bind_vars)
            return list(cursor)
        except Exception as e:
            logging.error(f"Error executing query: {str(e)}")
            raise

    def ensure_collections(self):
        try:
            required_collections = [
                'business_profiles',
                'business_goals',
                'agents',
                'models',
                'ontologies',
                'questions',
                'answers',
                'knowledge_nodes',
                'knowledge_edges'
            ]
            
            for collection_name in required_collections:
                if not self.db.has_collection(collection_name):
                    self.db.create_collection(collection_name)
                    logging.info(f"Created '{collection_name}' collection")
                else:
                    logging.info(f"'{collection_name}' collection already exists")
                    
            # Create graph if it doesn't exist
            if not self.db.has_graph('knowledge_graph'):
                graph = self.db.create_graph('knowledge_graph')
                # Create edge definition
                if not graph.has_edge_definition('knowledge_edges'):
                    graph.create_edge_definition(
                        edge_collection='knowledge_edges',
                        from_vertex_collections=['knowledge_nodes'],
                        to_vertex_collections=['knowledge_nodes']
                    )
                    logging.info("Created 'knowledge_edges' edge definition")
                    
        except Exception as e:
            logging.error(f"Error in ensure_collections: {str(e)}")
            raise

    def get_collection(self, collection_name: str):
        """Get a collection by name."""
        if not self.db:
            self.connect()
        return self.db.collection(collection_name)

    def create_document(self, collection_name: str, document: dict):
        """Create a document in a collection."""
        collection = self.get_collection(collection_name)
        return collection.insert(document)

    def get_document(self, collection_name: str, document_key: str):
        """Get a document by key from a collection."""
        collection = self.get_collection(collection_name)
        return collection.get(document_key)

    def update_document(self, collection_name: str, document_key: str, update_data: dict):
        """Update a document in a collection."""
        collection = self.get_collection(collection_name)
        return collection.update_match({'_key': document_key}, update_data)

    def delete_document(self, collection_name: str, document_key: str):
        """Delete a document from a collection."""
        collection = self.get_collection(collection_name)
        return collection.delete(document_key)

    def list_documents(self, collection_name: str, filter_query: dict = None):
        """List documents in a collection with optional filtering."""
        collection = self.get_collection(collection_name)
        if filter_query:
            return list(collection.find(filter_query))
        return list(collection.all())
