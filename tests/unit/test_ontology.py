from app.core.models.knowledge.ontology import Ontology

def test_ontology():
    ontology = Ontology(
        ontology_file="/mabos-standalone/app/core/ontologies/business_ontology.owl",
        concepts=[],
        relationships=[]
    )
    print("Ontology loaded successfully")

if __name__ == "__main__":
    test_ontology()