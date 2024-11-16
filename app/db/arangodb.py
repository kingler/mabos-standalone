import logging
from arango import ArangoClient
from app.config.config import CONFIG

def get_arango_client():
    """Get an ArangoDB client instance."""
    try:
        # Create a client connection
        client = ArangoClient(hosts=f'http://{CONFIG.ARANGO_HOST}:{CONFIG.ARANGO_PORT}')
        
        # Connect to _system database first
        sys_db = client.db('_system', username=CONFIG.ARANGO_USER, password=CONFIG.ARANGO_PASSWORD)
        
        # Create target database if it doesn't exist
        if not sys_db.has_database(CONFIG.ARANGO_DATABASE):
            sys_db.create_database(CONFIG.ARANGO_DATABASE)
            logging.info(f"Created database: {CONFIG.ARANGO_DATABASE}")
        
        # Connect to the target database
        db = client.db(CONFIG.ARANGO_DATABASE, username=CONFIG.ARANGO_USER, password=CONFIG.ARANGO_PASSWORD)
        logging.info(f"Connected to database: {CONFIG.ARANGO_DATABASE}")
        
        return db
    except Exception as e:
        logging.error(f"Failed to connect to database: {str(e)}")
        raise

def get_arango_db():
    """Get an ArangoDB database instance."""
    try:
        return get_arango_client()
    except Exception as e:
        logging.error(f"Failed to get database: {str(e)}")
        raise ConnectionError(f"Unable to connect to database '{CONFIG.ARANGO_DATABASE}'. Error: {str(e)}")

def ensure_collections(db):
    """Ensure required collections exist."""
    try:
        # Regular collections
        regular_collections = [
            'business_profiles',
            'business_goals',
            'agents',
            'models',
            'ontologies',
            'questions',
            'answers',
            'knowledge_nodes'
        ]
        
        for collection_name in regular_collections:
            if not db.has_collection(collection_name):
                db.create_collection(collection_name)
                logging.info(f"Created '{collection_name}' collection")
            else:
                logging.info(f"'{collection_name}' collection already exists")

        # Edge collections
        edge_collections = [
            'knowledge_edges',
            'parent_child'
        ]
        
        for collection_name in edge_collections:
            if not db.has_collection(collection_name):
                db.create_collection(collection_name, edge=True)
                logging.info(f"Created '{collection_name}' edge collection")
            else:
                logging.info(f"'{collection_name}' edge collection already exists")
                
        # Create graph if it doesn't exist
        if not db.has_graph('knowledge_graph'):
            graph = db.create_graph('knowledge_graph')
            # Create edge definition
            if not graph.has_edge_definition('knowledge_edges'):
                graph.create_edge_definition(
                    edge_collection='knowledge_edges',
                    from_vertex_collections=['knowledge_nodes'],
                    to_vertex_collections=['knowledge_nodes']
                )
                logging.info("Created 'knowledge_edges' edge definition")
                
    except Exception as e:
        logging.error(f"Error in ensure_collections: {str(e)}")
        raise
