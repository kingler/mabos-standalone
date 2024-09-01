import os
import logging
from dotenv import load_dotenv
from pyArango.connection import Connection
from requests.exceptions import RequestException

load_dotenv()

def get_arango_client():
    arango_url = os.getenv("ARANGO_URL")
    arango_username = os.getenv("ARANGO_USERNAME")
    arango_password = os.getenv("ARANGO_PASSWORD")
    try:
        return Connection(arangoURL=arango_url, username=arango_username, password=arango_password)
    except RequestException as e:
        logging.error(f"Failed to connect to ArangoDB: {e}")
        raise ConnectionError(f"Unable to connect to ArangoDB at {arango_url}. Please check if the database is running and the connection details are correct.")

def get_arango_db(client, business_shorthand, onboarding_date):
    db_name = f"{business_shorthand}_{onboarding_date}_db"
    if not client.hasDatabase(db_name):
        client.createDatabase(db_name)
    return client[db_name]
