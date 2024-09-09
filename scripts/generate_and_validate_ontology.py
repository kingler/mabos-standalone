import asyncio
import json
from app.models.knowledge.ontology.ontology_generator import OntologyGenerator
from app.models.knowledge.ontology.ontology_version_control import OntologyVersionControl
from app.config.config import CONFIG

async def main():
    # Load the business description
    business_description_path = CONFIG.BUSINESS_DESCRIPTION_PATH
    with open(business_description_path, 'r') as file:
        business_description = file.read()

    # Initialize the OntologyGenerator
    ontology_generator = OntologyGenerator()

    # Generate the ontology
    ontology = await ontology_generator.generate_ontology(business_description)

    # Validate the ontology
    validation_result = await ontology_generator.validate_ontology(ontology)

    # Serialize the ontology to JSON
    ontology_json = ontology.to_json()

    # Save the JSON to a file
    output_path = "/path/to/output/ontology.json"
    with open(output_path, 'w') as file:
        file.write(ontology_json)

    # Save the validation result to a file
    validation_output_path = "/path/to/output/validation_result.json"
    with open(validation_output_path, 'w') as file:
        json.dump(validation_result, file)

    print(f"Ontology saved to {output_path}")
    print(f"Validation result saved to {validation_output_path}")

if __name__ == "__main__":
    asyncio.run(main())
