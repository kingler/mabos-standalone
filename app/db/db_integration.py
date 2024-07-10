from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.arangodb import get_arango_db
from app.db.arango_db_client import ArangoDBClient

class DatabaseIntegration:
    def __init__(self):
        self.sql_db = next(get_db())
        self.arango_client = ArangoDBClient(host="localhost", port=8529, username="root", password="difyai123456", database="dify")

    async def execute_sql_query(self, query: str, params: dict = None):
        return self.sql_db.execute(query, params)

    async def execute_arango_query(self, query: str, bind_vars: dict = None):
        return await self.arango_client.execute_query(query, bind_vars)

    # Add more methods for specific database operations
