from app.services.question_service import QuestionService
from app.db.arango_db_client import ArangoDBClient

def get_db_client():
    # Replace with your actual ArangoDB connection details
    return ArangoDBClient(url="http://localhost:8529", username="root", password="password")

def get_question_service():
    db_client = get_db_client()
    return QuestionService(db_client)