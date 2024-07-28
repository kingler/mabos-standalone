import openai
from typing import List, Dict, Any, Optional
import json
from tenacity import retry, stop_after_attempt, wait_random_exponential
from app.models.ontology_types import OntologyStructure, ConceptType, RelationshipType, create_concept, create_relationship, validate_ontology_structure

class OntologyGenerator:
    """
    A class for generating and refining ontologies using OpenAI's GPT models.
    """

    def __init__(self, api_key: str):
        """
        Initialize the OntologyGenerator with an OpenAI API key.

        Args:
            api_key (str): The OpenAI API key for authentication.
        """
        self.api_key = api_key
        openai.api_key = api_key

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(3))
    def _make_openai_request(self, messages: List[Dict[str, str]], max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """
        Make a request to OpenAI's API with retry logic.

        Args:
            messages (List[Dict[str, str]]): The messages to send to the API.
            max_tokens (int): The maximum number of tokens to generate.
            temperature (float): The sampling temperature to use.

        Returns:
            str: The generated response content.

        Raises:
            openai.error.OpenAIError: If the API request fails after retries.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except openai.error.OpenAIError as e:
            raise openai.error.OpenAIError(f"OpenAI API request failed: {str(e)}")

    def generate_ontology(self, domain_description: str) -> OntologyStructure:
        """
        Generate an ontology structure based on a domain description.

        Args:
            domain_description (str): A description of the domain for which to generate the ontology.

        Returns:
            OntologyStructure: The generated ontology structure.

        Raises:
            json.JSONDecodeError: If the generated ontology cannot be parsed as JSON.
            ValueError: If the generated ontology structure is invalid.
        """
        prompt = f"""
        Given the following domain description, generate an ontology structure including classes, properties, relationships, and axioms.
        Format the output as a JSON structure with the following keys:
        - classes: list of class names
        - properties: list of property names
        - relationships: list of dictionaries with 'subject', 'predicate', and 'object' keys
        - axioms: list of logical axioms or rules

        Domain description: {domain_description}

        Output the ontology structure in JSON format:
        """

        messages = [
            {"role": "system", "content": "You are an AI assistant specializing in ontology generation."},
            {"role": "user", "content": prompt}
        ]

        ontology_str = self._make_openai_request(messages)
        
        try:
            ontology = json.loads(ontology_str)
            if not self.validate_ontology(ontology):
                raise ValueError("Generated ontology structure is invalid.")
            return ontology
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Failed to parse generated ontology: {e}", ontology_str, 0)

    def refine_ontology(self, current_ontology: OntologyStructure, new_information: str) -> OntologyStructure:
        """
        Refine and expand an existing ontology based on new information.

        Args:
            current_ontology (OntologyStructure): The current ontology structure.
            new_information (str): New information to incorporate into the ontology.

        Returns:
            OntologyStructure: The refined ontology structure.

        Raises:
            json.JSONDecodeError: If the refined ontology cannot be parsed as JSON.
            ValueError: If the refined ontology structure is invalid.
        """
        prompt = f"""
        Given the current ontology structure and new information, refine and expand the ontology.
        Current ontology:
        {json.dumps(current_ontology, indent=2)}

        New information:
        {new_information}

        Output the refined ontology structure in JSON format:
        """

        messages = [
            {"role": "system", "content": "You are an AI assistant specializing in ontology refinement."},
            {"role": "user", "content": prompt}
        ]

        refined_ontology_str = self._make_openai_request(messages)
        
        try:
            refined_ontology = json.loads(refined_ontology_str)
            if not self.validate_ontology(refined_ontology):
                raise ValueError("Refined ontology structure is invalid.")
            return refined_ontology
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Failed to parse refined ontology: {e}", refined_ontology_str, 0)

    def validate_ontology(self, ontology: OntologyStructure) -> bool:
        """
        Validate the structure of an ontology.

        Args:
            ontology (OntologyStructure): The ontology structure to validate.

        Returns:
            bool: True if the ontology is valid, False otherwise.
        """
        required_keys = {'classes', 'properties', 'relationships', 'axioms'}
        if any(key not in ontology for key in required_keys):
            return False
        
        if not all(isinstance(ontology[key], list) for key in required_keys):
            return False
        
        if not all({'subject', 'predicate', 'object'}.issubset(rel.keys()) for rel in ontology['relationships'] if isinstance(rel, dict)):
            return False
        
        return True

    def merge_ontologies(self, ontology1: OntologyStructure, ontology2: OntologyStructure) -> OntologyStructure:
        """
        Merge two ontologies into a single ontology.

        Args:
            ontology1 (OntologyStructure): The first ontology to merge.
            ontology2 (OntologyStructure): The second ontology to merge.

        Returns:
            OntologyStructure: The merged ontology.

        Raises:
            ValueError: If either of the input ontologies is invalid.
        """
        if not self.validate_ontology(ontology1) or not self.validate_ontology(ontology2):
            raise ValueError("One or both of the input ontologies are invalid.")

        merged = {
            'classes': list(set(ontology1['classes'] + ontology2['classes'])),
            'properties': list(set(ontology1['properties'] + ontology2['properties'])),
            'relationships': ontology1['relationships'] + ontology2['relationships'],
            'axioms': list(set(ontology1['axioms'] + ontology2['axioms']))
        }
        
        # Remove duplicate relationships
        unique_relationships = []
        seen = set()
        for rel in merged['relationships']:
            rel_tuple = (rel['subject'], rel['predicate'], rel['object'])
            if rel_tuple not in seen:
                seen.add(rel_tuple)
                unique_relationships.append(rel)
        merged['relationships'] = unique_relationships

        return merged

    def create_concept(self, name: str, description: Optional[str] = None) -> ConceptType:
        """
        Create a concept structure.

        Args:
            name (str): The name of the concept.
            description (Optional[str]): The description of the concept. Defaults to None.

        Returns:
            ConceptType: A concept structure.
        """
        return create_concept(name, description)

    def create_relationship(self, name: str, domain: str, range: str, description: Optional[str] = None) -> RelationshipType:
        """
        Create a relationship structure.

        Args:
            name (str): The name of the relationship.
            domain (str): The domain of the relationship.
            range (str): The range of the relationship.
            description (Optional[str]): The description of the relationship. Defaults to None.

        Returns:
            RelationshipType: A relationship structure.
        """
        return create_relationship(name, domain, range, description)
    
    @staticmethod
    def test_validate_ontology_structure():
        # Test case 1: Valid ontology structure
        valid_ontology: OntologyStructure = {
            "concepts": ["Concept1", "Concept2"],
            "relationships": [{"subject": "Concept1", "predicate": "relatedTo", "object": "Concept2"}]
        }
        assert validate_ontology_structure(valid_ontology) == True, "Test case 1 failed"

        # Test case 2: Missing 'concepts' key
        invalid_ontology_1: OntologyStructure = {
            "relationships": [{"subject": "Concept1", "predicate": "relatedTo", "object": "Concept2"}]
        }
        assert validate_ontology_structure(invalid_ontology_1) == False, "Test case 2 failed"

        # Test case 3: Missing 'relationships' key
        invalid_ontology_2: OntologyStructure = {
            "concepts": ["Concept1", "Concept2"]
        }
        assert validate_ontology_structure(invalid_ontology_2) == False, "Test case 3 failed"

        # Test case 4: Empty ontology structure
        invalid_ontology_3: OntologyStructure = {}
        assert validate_ontology_structure(invalid_ontology_3) == False, "Test case 4 failed"

        # Test case 5: Additional keys in the ontology structure
        valid_ontology_with_extra_keys: OntologyStructure = {
            "concepts": ["Concept1", "Concept2"],
            "relationships": [{"subject": "Concept1", "predicate": "relatedTo", "object": "Concept2"}],
            "extra_key": "extra_value"
        }
        assert validate_ontology_structure(valid_ontology_with_extra_keys) == True, "Test case 5 failed"

        print("All test cases passed!")

if __name__ == "__main__":
    OntologyGenerator.test_validate_ontology_structure()