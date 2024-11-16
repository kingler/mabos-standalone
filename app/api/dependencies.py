from app.services.question_service import QuestionService
from app.db.arango_db_client import ArangoDBClient
from app.config.config import CONFIG
#from app.services.user_service import UserService
#from app.services.analytics_service import AnalyticsService


def get_db_client():
    """Get a database client instance.
    
    Returns:
        ArangoDBClient: An initialized database client
    """
    try:
        # Create a new client instance with configuration values
        client = ArangoDBClient(
            host=CONFIG.ARANGO_HOST,
            port=CONFIG.ARANGO_PORT,
            username=CONFIG.ARANGO_USER,
            password=CONFIG.ARANGO_PASSWORD,
            database=CONFIG.ARANGO_DATABASE
        )
        return client
    except Exception as e:
        # Log the error and return None
        import logging
        logging.error(f"Failed to create database client: {str(e)}")
        return None

def get_question_service():
    """Get a question service instance.
    
    Returns:
        QuestionService: An initialized question service
    """
    db_client = get_db_client()
    if db_client:
        return QuestionService(db_client)
    return None

def get_user_service():
    """Get a user service instance.
    
    Returns:
        UserService: An initialized user service
    """
    db_client = get_db_client()
    if db_client:
        pass  # Uncomment and implement when UserService is ready
        #return UserService(db_client)
    return None

def get_analytics_service():
    """Get an analytics service instance.
    
    Returns:
        AnalyticsService: An initialized analytics service
    """
    db_client = get_db_client()
    if db_client:
        pass  # Uncomment and implement when AnalyticsService is ready
        #return AnalyticsService(db_client)
    return None
