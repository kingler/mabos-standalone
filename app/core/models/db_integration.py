from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import Base, get_db
from app.db.arangodb import get_arango_db
from app.db.arango_db_client import ArangoDBClient
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)

class DBIntegration:
    """
    A class for handling database integration operations.
    """

    def __init__(self, db_config: Dict[str, Any]):
        """
        Initialize the DBIntegration instance.

        Args:
            db_config (Dict[str, Any]): Configuration for the database connection.
        """
        self.db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        self.engine = create_engine(self.db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.sql_db = next(get_db())
        self.arango_client = ArangoDBClient(host="localhost", port=8529, username="root", password="difyai123456", database="dify")

    def get_session(self):
        """
        Get a database session.

        Returns:
            Session: A SQLAlchemy session object.
        """
        return next(get_db())

    def create_tables(self):
        """
        Create all tables defined in the Base metadata.
        """
        Base.metadata.create_all(bind=self.engine)

    async def execute_sql_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a raw SQL query.

        Args:
            query (str): The SQL query to execute.
            params (Optional[Dict[str, Any]]): Parameters for the query.

        Returns:
            List[Dict[str, Any]]: The query results as a list of dictionaries.

        Raises:
            SQLAlchemyError: If there's an error executing the query.
        """
        try:
            return self.sql_db.execute(query, params or {})
        except SQLAlchemyError as e:
            logger.error(f"Error executing SQL query: {e}")
            raise

    async def execute_arango_query(self, query: str, bind_vars: Optional[Dict[str, Any]] = None):
        """
        Execute an ArangoDB query.

        Args:
            query (str): The AQL query to execute.
            bind_vars (Optional[Dict[str, Any]]): Bind variables for the query.

        Returns:
            The query results.

        Raises:
            Exception: If there's an error executing the query.
        """
        try:
            return await self.arango_client.execute_query(query, bind_vars)
        except Exception as e:
            logger.error(f"Error executing ArangoDB query: {e}")
            raise

    def insert_data(self, table, data: Dict[str, Any]) -> Any:
        """
        Insert data into a table.

        Args:
            table: The SQLAlchemy table model.
            data (Dict[str, Any]): The data to insert.

        Returns:
            Any: The newly inserted record.

        Raises:
            SQLAlchemyError: If there's an error inserting the data.
        """
        try:
            with self.get_session() as session:
                new_record = table(**data)
                session.add(new_record)
                session.commit()
                return new_record
        except SQLAlchemyError as e:
            logger.error(f"Error inserting data: {e}")
            raise

    def update_data(self, table, id: int, data: Dict[str, Any]) -> Optional[Any]:
        """
        Update data in a table.

        Args:
            table: The SQLAlchemy table model.
            id (int): The ID of the record to update.
            data (Dict[str, Any]): The data to update.

        Returns:
            Optional[Any]: The updated record, or None if not found.

        Raises:
            SQLAlchemyError: If there's an error updating the data.
        """
        try:
            with self.get_session() as session:
                record = session.query(table).filter(table.id == id).first()
                if record:
                    for key, value in data.items():
                        setattr(record, key, value)
                    session.commit()
                    return record
                return None
        except SQLAlchemyError as e:
            logger.error(f"Error updating data: {e}")
            raise

    def delete_data(self, table, id: int) -> bool:
        """
        Delete data from a table.

        Args:
            table: The SQLAlchemy table model.
            id (int): The ID of the record to delete.

        Returns:
            bool: True if the record was deleted, False otherwise.

        Raises:
            SQLAlchemyError: If there's an error deleting the data.
        """
        try:
            with self.get_session() as session:
                record = session.query(table).filter(table.id == id).first()
                if record:
                    session.delete(record)
                    session.commit()
                    return True
                return False
        except SQLAlchemyError as e:
            logger.error(f"Error deleting data: {e}")
            raise

    def get_data(self, table, id: int) -> Optional[Any]:
        """
        Get a single record from a table.

        Args:
            table: The SQLAlchemy table model.
            id (int): The ID of the record to retrieve.

        Returns:
            Optional[Any]: The retrieved record, or None if not found.

        Raises:
            SQLAlchemyError: If there's an error retrieving the data.
        """
        try:
            with self.get_session() as session:
                return session.query(table).filter(table.id == id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving data: {e}")
            raise

    def get_all_data(self, table) -> List[Any]:
        """
        Get all records from a table.

        Args:
            table: The SQLAlchemy table model.

        Returns:
            List[Any]: A list of all records in the table.

        Raises:
            SQLAlchemyError: If there's an error retrieving the data.
        """
        try:
            with self.get_session() as session:
                return session.query(table).all()
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving all data: {e}")
            raise
