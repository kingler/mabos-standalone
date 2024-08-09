import asyncio
from app.core.models.knowledge.ontology.ontology_generator import OntologyGenerator
from app.core.models.knowledge.ontology.ontology import Ontology

async def onboard_business(business_description: str) -> Ontology:
    generator = OntologyGenerator()
    ontology = await generator.generate_ontology(business_description)

    # Enhance ontology with embeddings
    for concept in ontology.concepts:
        ontology.get_concept_embedding(concept)

    return ontology

def find_similar_concepts(ontology: Ontology, query: str, top_k: int = 5):
    return ontology.find_similar_concepts(query, top_k)

# Example usage (can be commented out or removed in production)
if __name__ == "__main__":
    business_description = "Our e-commerce business sells electronics products online. We have customers who can browse our product catalog, add items to their shopping cart, and place orders."
    
    ontology = asyncio.run(onboard_business(business_description))
    
    query = "sales process"
    similar_concepts = find_similar_concepts(ontology, query)
    print(f"Concepts similar to '{query}':", similar_concepts)