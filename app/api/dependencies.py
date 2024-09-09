from app.services.question_service import QuestionService
from app.db.arango_db_client import ArangoDBClient
#from app.services.user_service import UserService
#from app.services.analytics_service import AnalyticsService


def get_db_client():
    # Replace with your actual ArangoDB connection details
    return ArangoDBClient(url="http://localhost:8529", username="root", password="password")

def get_question_service():
    db_client = get_db_client()
    return QuestionService(db_client)

def get_user_service():
    db_client = get_db_client()
#    return UserService(db_client)

def get_analytics_service():
    db_client = get_db_client()
#    return AnalyticsService(db_client)