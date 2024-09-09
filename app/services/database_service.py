from arango import ArangoClient
from app.config.config import get_settings
from app.db.arangodb import get_arango_db

class DatabaseService:
    def __init__(self):
        self.db = get_arango_db()

    async def get_collection(self, collection_name):
        return self.db.collection(collection_name)

    async def query(self, query_string, bind_vars=None):
        return await self.db.aql.execute(query_string, bind_vars=bind_vars)

    # Add other database-related methods as needed