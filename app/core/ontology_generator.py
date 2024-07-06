import openai
from typing import List, Dict, Any
import json

class OntologyGenerator:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_ontology(self, domain_description: str) -> Dict[str, Any]:
        prompt = f"""
        Given the following domain description, generate an ontology structure including classes, concepts, and relationships.
        Format the output as a JSON structure with the following keys:
        - classes: list of class names
        - properties: list of property names
        - relationships: list of dictionaries with 'subject', 'predicate', and 'object' keys
        - axioms: list of logical axioms or rules

        Domain description: {domain_description}

        Output the ontology structure in JSON format:
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant specializing in ontology generation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7,
        )

        ontology_str = response.choices[0].message.content.strip()
        return json.loads(ontology_str)

    def refine_ontology(self, current_ontology: Dict[str, Any], new_information: str) -> Dict[str, Any]:
        prompt = f"""
        Given the current ontology structure and new information, refine and expand the ontology.
        Current ontology:
        {json.dumps(current_ontology, indent=2)}

        New information:
        {new_information}

        Output the refined ontology structure in JSON format:
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant specializing in ontology refinement."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7,
        )

        refined_ontology_str = response.choices[0].message.content.strip()
        return json.loads(refined_ontology_str)