import asyncio
import json

from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.models.knowledge.ontology.ontology_generator import \
    OntologyGenerator
from app.core.tools.llm_manager import LLMManager


async def onboard_business(business_description: str) -> Ontology:
    # Load the LLM configuration
    with open('config/llm_config.json') as f:
        config = json.load(f)

    llms_config = config['llms']
    api_key = config['api_keys']['openai']  # or 'anthropic' based on your needs

    # Create an instance of LLMManager with the required parameters
    llm_manager = LLMManager(llms_config=llms_config, api_key=api_key)

    generator = OntologyGenerator(llm_manager)
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