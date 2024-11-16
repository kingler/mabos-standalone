import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Now import the required modules
import pandas as pd
from arango import ArangoClient
from arango import exceptions as arango_exceptions
from app.config.config import get_settings

def seed_arango_db():
    settings = get_settings()
    client = ArangoClient(hosts=settings.database_url)
    db = client.db(settings.db_name, username=settings.db_username, password=settings.db_password)

    # Define the collections to seed
    collections_to_seed = [
        'agents', 'knowledge_triples', 'goals', 'plans', 'actions',
        'beliefs', 'desires', 'intentions', 'roles', 'skills', 'tasks',
        'business_models', 'mdd_models', 'togaf_models', 'archimate_models', 'tropos_models',
        'environments', 'world_models', 'organizations', 'ontology', 'inconsistencies',
        'rules', 'business_entities', 'business_processes'
    ]

    # Clear existing data
    clear_collections(db, collections_to_seed)

    # Seed collections
    for collection_name in collections_to_seed:
        seed_collection(db, collection_name)

    # Seed edges
    seed_edges(db)

def clear_collections(db, collections_to_clear):
    for collection_name in collections_to_clear:
        if db.has_collection(collection_name):
            collection = db.collection(collection_name)
            collection.truncate()
            print(f"Cleared collection: {collection_name}")

def seed_collection(db, collection_name):
    csv_path = f'app/db/seed_data/{collection_name}.csv'
    if not os.path.exists(csv_path):
        print(f"CSV file for {collection_name} not found. Skipping.")
        return

    df = pd.read_csv(csv_path)
    collection = db.collection(collection_name)

    for _, row in df.iterrows():
        doc = row.to_dict()
        doc['_key'] = str(doc['_key'])  # Ensure _key is a string
        try:
            collection.insert(doc)
        except arango_exceptions.DocumentInsertError as e:
            if e.error_code == 1210:  # Unique constraint violated
                collection.update(doc)
            else:
                raise

    print(f"Seeded {len(df)} documents into {collection_name}")

def seed_edges(db):
    edge_collections = [
        'agent_knowledge', 'agent_goals', 'goal_plans', 'plan_actions',
        'agent_beliefs', 'agent_desires', 'agent_intentions',
        'agent_roles', 'agent_skills', 'agent_tasks',
        'mdd_relationships', 'environment_world_model', 'organization_agents',
        'knowledge_inconsistencies',
        'rule_applications', 'business_entity_relationships', 'process_entity_relationships'
    ]

    for edge_collection_name in edge_collections:
        csv_path = f'app/db/seed_data/{edge_collection_name}.csv'
        if not os.path.exists(csv_path):
            print(f"CSV file for {edge_collection_name} not found. Skipping.")
            continue

        df = pd.read_csv(csv_path)
        edge_collection = db.collection(edge_collection_name)

        for _, row in df.iterrows():
            edge = {
                '_from': row['_from'],
                '_to': row['_to'],
                'type': row['type'] if 'type' in row else edge_collection_name
            }
            try:
                edge_collection.insert(edge)
            except arango_exceptions.DocumentInsertError as e:
                if e.error_code == 1210:  # Unique constraint violated
                    edge_collection.update(edge)
                else:
                    raise

        print(f"Seeded {len(df)} edges into {edge_collection_name}")

if __name__ == "__main__":
    seed_arango_db()