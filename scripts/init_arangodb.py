from arango import ArangoClient

def init_database():
    # Initialize client
    client = ArangoClient(hosts="http://localhost:8529")
    
    # Connect to _system database as root user
    sys_db = client.db('_system', username='root', password='yourpassword')
    
    # Create a new database if it doesn't exist
    if not sys_db.has_database('mdd_knowledge_base'):
        sys_db.create_database('mdd_knowledge_base')
    
    # Connect to the new database
    db = client.db('mdd_knowledge_base', username='root', password='yourpassword')
    
    # Create vertex collections if they don't exist
    vertex_collections = [
        'knowledge_nodes',
        'business_goals',
        'model_artifacts',
        'ontologies'
    ]
    
    for collection in vertex_collections:
        if not db.has_collection(collection):
            db.create_collection(collection)
    
    # Create edge collection
    if not db.has_collection('knowledge_edges'):
        db.create_collection('knowledge_edges', edge=True)  # Create as edge collection
    
    # Create graph if it doesn't exist
    if not db.has_graph('knowledge_graph'):
        graph = db.create_graph('knowledge_graph')
        
        # Add edge definitions
        graph.create_edge_definition(
            edge_collection='knowledge_edges',
            from_vertex_collections=['knowledge_nodes'],
            to_vertex_collections=['knowledge_nodes']
        )

if __name__ == "__main__":
    init_database()
