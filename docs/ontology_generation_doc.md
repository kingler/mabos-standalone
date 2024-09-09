# Using large language model (LLM) to build Ontologies

The `OntologyGenerator` class in your code is designed to generate an ontology from a business description using a large language model (LLM). Here's a step-by-step explanation of how it works:

1. **Initialization**:
   - The `OntologyGenerator` is initialized with configurations, including API keys and LLM settings.
   - It sets up the `LLMManager` and `LLMService` to interact with the LLM.

2. **Generating the Ontology**:
   - The `generate_ontology` method takes a business description as input.
   - It constructs a prompt that describes the task to the LLM, asking it to generate an ontology structure based on the business description.
   - The prompt specifies the format of the expected output, which includes concepts, relationships, and properties.

3. **Interacting with the LLM**:
   - The `LLMManager` selects an appropriate model for the task.
   - The `LLMManager` sends the prompt to the selected model and retrieves the response.
   - The response is expected to be a JSON structure that matches the specified schema.

4. **Parsing the LLM Response**:
   - The `_parse_llm_response` method attempts to parse the LLM's response as JSON.
   - It validates the structure of the parsed response to ensure it contains the required keys: `concepts`, `relationships`, and `properties`.

5. **Building the Ontology**:
   - The method iterates over the parsed response to add concepts, relationships, and properties to the `Ontology` object.
   - The `Ontology` object is then returned.

Here's the relevant part of the `OntologyGenerator` class that performs these steps:

```python:app/core/models/knowledge/ontology/ontology_generator.py
class OntologyGenerator(BaseModel):
    # ... existing code ...

    async def generate_ontology(self, business_description: str) -> Ontology:
        prompt = f"""
        Given the following business description, generate an ontology structure:
        
        Business Description: {business_description}
        
        The ontology should include:
        1. Key concepts (classes)
        2. Relationships between concepts
        3. Properties of concepts
        
        Format the output as a JSON structure with the following schema:
        {{
            "concepts": {{
                "ConceptName": "ConceptDescription",
                ...
            }},
            "relationships": {{
                "RelationshipName": {{
                    "domain": "DomainConceptName",
                    "range": "RangeConceptName"
                }},
                ...
            }},
            "properties": {{
                "ConceptName": ["Property1", "Property2", ...],
                ...
            }}
        }}
        """
        
        selected_model = self.llm_manager.select_model("Generate ontology from business description", required_capabilities=["multilingual"])
        response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
        ontology_structure = self._parse_llm_response(response)
        
        ontology = Ontology()
        
        for concept, description in ontology_structure.get("concepts", {}).items():
            ontology.add_concept(concept, description)
        
        for relationship, details in ontology_structure.get("relationships", {}).items():
            ontology.add_relationship(relationship, details["domain"], details["range"])
        
        for concept, properties in ontology_structure.get("properties", {}).items():
            for property in properties:
                ontology.add_property(concept, property)
        
        return ontology

    def _parse_llm_response(self, response: str) -> Dict[str, Any]:
        import json
        try:
            # Attempt to parse the response as JSON
            parsed_response = json.loads(response)
            
            # Validate the structure of the parsed response
            required_keys = ["concepts", "relationships", "properties"]
            if any(key not in parsed_response for key in required_keys):
                raise ValueError("Response is missing one or more required keys")
            
            return parsed_response
        except json.JSONDecodeError:
            # If JSON parsing fails, log the error and return an empty dictionary
            logging.error(f"Failed to parse LLM response as JSON: {response}")
            return {}
        except ValueError as e:
            # If the structure is invalid, log the error and return an empty dictionary
            logging.error(f"Invalid response structure: {str(e)}")
            return {}
```

### Example Usage

To use the `OntologyGenerator` to generate an ontology from a business description, you can create a script like this:

```python:app/scripts/generate_ontology.py
import asyncio
from app.models.knowledge.ontology.ontology_generator import OntologyGenerator

async def main():
    business_description = """
    VividWalls Online is a marketplace specializing in high-quality, ready-to-hang print-on-demand wall art. Our organization connects artists with art enthusiasts, offering a wide range of customizable art prints for home and office decor.
    """
    
    ontology_generator = OntologyGenerator()
    ontology = await ontology_generator.generate_ontology(business_description)
    
    print(ontology.to_json())

if __name__ == "__main__":
    asyncio.run(main())
```

This script initializes the `OntologyGenerator`, generates the ontology from the provided business description, and prints the resulting ontology in JSON format.