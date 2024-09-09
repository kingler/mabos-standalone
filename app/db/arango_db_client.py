import json
import logging
from app.config.settings import get_settings
from arango import ArangoClient

from app.utils.uuid_encoder import UUIDEncoder  # Update this import

class ArangoDBClient:
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password
        self.client = self._connect()  # Initialize the client
        self.db = None  # Initialize the db attribute

    def _connect(self):
        from arango import ArangoClient
        return ArangoClient(hosts=self.url)

    def connect(self):
        try:
            settings = get_settings()
            logging.info(f"Connecting to ArangoDB at {self.url} with username {settings.db_username}")
            self.db = self.client.db(settings.db_name, username=settings.db_username, password=settings.db_password)
            if self.db:
                logging.info("ArangoDBClient connected successfully")
                self.ensure_collections()
            else:
                logging.error("Failed to connect to the database.")
                raise Exception("Failed to connect to the database.")
        except Exception as e:
            logging.error(f"Error in ArangoDBClient.connect: {str(e)}")
            raise
        
    def close(self):
        if self.client:
            # Replace with actual close logic
            self.client = None
            logging.info("ArangoDBClient connection closed")

    def execute_query(self, query: str, bind_vars: dict = None):
        if self.db is None:
            logging.error("Database connection is not established.")
            raise Exception("Database connection is not established.")
        
        try:
            if bind_vars:
                bind_vars = json.loads(json.dumps(bind_vars, cls=UUIDEncoder))
            cursor = self.db.aql.execute(query, bind_vars=bind_vars)
            return list(cursor)
        except Exception as e:
            logging.error(f"Error executing query: {str(e)}")
            raise

    def ensure_collections(self):
        try:
            if not self.db.has_collection('business_profiles'):
                self.db.create_collection('business_profiles')
                logging.info("Created 'business_profiles' collection")
            else:
                logging.info("'business_profiles' collection already exists")
        except Exception as e:
            logging.error(f"Error in ensure_collections: {str(e)}")
            raise