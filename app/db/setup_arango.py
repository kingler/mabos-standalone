import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from arango import ArangoClient
from app.config.config import get_settings

def setup_arango_db():
    settings = get_settings()
    client = ArangoClient(hosts=settings.database_url)
    sys_db = client.db('_system', username=settings.db_username, password=settings.db_password)

    # Create database if it doesn't exist
    if not sys_db.has_database(settings.db_name):
        sys_db.create_database(settings.db_name)
    
    db = client.db(settings.db_name, username=settings.db_username, password=settings.db_password)

    # Create collections
    collections = [
        'agents', 'knowledge_triples', 'ontology', 'plans', 'agent_goals', 'business_goals', 'actions', 'inconsistencies'
    ]
    for collection in collections:
        if not db.has_collection(collection):
            db.create_collection(collection)

    # Create graph
    if not db.has_graph('mabos_graph'):
        graph = db.create_graph('mabos_graph')
        
        # Create edge definitions
        edge_definitions = [
            {
                'edge_collection': 'agent_knowledge',
                'from_vertex_collections': ['agents'],
                'to_vertex_collections': ['knowledge_triples']
            },
            {
                'edge_collection': 'agent_goals_edges',
                'from_vertex_collections': ['agents'],
                'to_vertex_collections': ['agent_goals']
            },
            {
                'edge_collection': 'business_goals_edges',
                'from_vertex_collections': ['business_goals'],
                'to_vertex_collections': ['agent_goals']
            },
            {
                'edge_collection': 'goal_plans',
                'from_vertex_collections': ['agent_goals', 'business_goals'],
                'to_vertex_collections': ['plans']
            },
            {
                'edge_collection': 'plan_actions',
                'from_vertex_collections': ['plans'],
                'to_vertex_collections': ['actions']
            },
            {
                'edge_collection': 'knowledge_inconsistencies',
                'from_vertex_collections': ['knowledge_triples'],
                'to_vertex_collections': ['inconsistencies']
            }
        ]
        
        for edge_definition in edge_definitions:
            graph.create_edge_definition(
                edge_collection=edge_definition['edge_collection'],
                from_vertex_collections=edge_definition['from_vertex_collections'],
                to_vertex_collections=edge_definition['to_vertex_collections']
            )

if __name__ == "__main__":
    setup_arango_db()