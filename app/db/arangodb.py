import logging
from arango import ArangoClient
from app.config.config import get_settings

settings = get_settings()

def get_arango_client():
    return ArangoClient(hosts=settings.database_url)

def get_arango_db():
    client = get_arango_client()
    try:
        db = client.db(settings.db_name, username=settings.db_username, password=settings.db_password)
        logging.info(f"Connected to database: {settings.db_name}")
        return db
    except Exception as e:
        logging.error(f"Failed to connect to database: {e}")
        raise ConnectionError(f"Unable to connect to database '{settings.db_name}'. Error: {str(e)}")
