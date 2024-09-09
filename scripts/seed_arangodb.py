import json
from arango import ArangoClient
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL

# Connect to ArangoDB
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("vividwalls", username="root", password="")

# Create collections
collections = [
    "artists", "artworks", "customers", "orders", "categories", 
    "collections", "historical_sales", "print_on_demand_suppliers"
]

for collection_name in collections:
    if not db.has_collection(collection_name):
        db.create_collection(collection_name)

# Import JSON data
json_files = [
    "artists.json", "artworks.json", "customers.json", "orders.json", 
    "categories.json", "collections.json", "historical_sales.json", 
    "print_on_demand_suppliers.json"
]

for file_name in json_files:
    collection_name = file_name.split('.')[0]
    collection = db.collection(collection_name)
    
    with open(f"@data/{file_name}", "r") as file:
        data = json.load(file)
        collection.import_bulk(data)

# Create graph
if not db.has_graph("vividwalls_graph"):
    graph = db.create_graph("vividwalls_graph")
else:
    graph = db.graph("vividwalls_graph")

# Create edge definitions
edge_definitions = [
    {
        "edge_collection": "creates",
        "from_vertex_collections": ["artists"],
        "to_vertex_collections": ["artworks"]
    },
    {
        "edge_collection": "belongs_to_category",
        "from_vertex_collections": ["artworks"],
        "to_vertex_collections": ["categories"]
    },
    {
        "edge_collection": "belongs_to_collection",
        "from_vertex_collections": ["artworks"],
        "to_vertex_collections": ["collections"]
    },
    {
        "edge_collection": "places_order",
        "from_vertex_collections": ["customers"],
        "to_vertex_collections": ["orders"]
    },
    {
        "edge_collection": "contains_print",
        "from_vertex_collections": ["orders"],
        "to_vertex_collections": ["artworks"]
    }
]

for edge_def in edge_definitions:
    if not graph.has_edge_definition(edge_def["edge_collection"]):
        graph.create_edge_definition(**edge_def)

# Import RDF/OWL data
g = Graph()
g.parse("@data/vividwalls_ontology.rdf", format="xml")
g.parse("@data/vividwalls_ontology.owl", format="xml")

# Create ontology collection
if not db.has_collection("ontology"):
    ontology = db.create_collection("ontology")
else:
    ontology = db.collection("ontology")

# Import ontology data
for s, p, o in g:
    doc = {
        "subject": str(s),
        "predicate": str(p),
        "object": str(o)
    }
    ontology.insert(doc)

print("Database seeded successfully!")