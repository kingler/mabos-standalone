from pyArango.connection import Connection
from dotenv import load_dotenv
import os

load_dotenv()

def get_arango_client():
    arango_url = os.getenv("ARANGO_URL", "http://localhost:8529")
    arango_username = os.getenv("ARANGO_USERNAME", "root")
    arango_password = os.getenv("ARANGO_PASSWORD", "difyai123456")
    conn = Connection(arangoURL=arango_url, username=arango_username, password=arango_password)
    return conn

def get_arango_db(client, db_name="dify"):
    if not client.hasDatabase(db_name):
        client.createDatabase(db_name)
    return client[db_name]
