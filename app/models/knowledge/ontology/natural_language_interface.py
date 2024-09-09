from typing import Any, Dict, List

from pydantic import BaseModel

from app.models.knowledge.ontology.ontology import Ontology
from app.tools.llm_manager import LLMManager


class NaturalLanguageOntologyInterface(BaseModel):
    llm_manager: LLMManager
    ontology: Ontology

    async def process_command(self, command: str) -> str:
        # Prepare the prompt for the LLM
        prompt = f"""
        Given the following ontology structure and the user command, 
        provide the necessary steps to update the ontology:

        Ontology structure:
        {self.ontology}

        User command:
        {command}

        Steps to update the ontology:
        """

        # Get the response from the LLM
        response = await self.llm_manager.generate_text(prompt)

        # Process the LLM's response and update the ontology
        # This is a simplified version; you might need more complex logic here
        update_steps = response.split('\n')
        for step in update_steps:
            if step.startswith('Add concept:'):
                concept_name = step.split(':')[1].strip()
                self.ontology.add_concept(concept_name)
            elif step.startswith('Add relationship:'):
                rel_info = step.split(':')[1].strip().split(',')
                self.ontology.add_relationship(rel_info[0], rel_info[1], rel_info[2])

        return f"Ontology updated based on command: {command}"

    async def query_ontology(self, query: str) -> List[Dict[str, Any]]:
        # Prepare the prompt for the LLM
        prompt = f"""
        Given the following ontology structure and the user query, 
        provide the SPARQL query to retrieve the requested information:

        Ontology structure:
        {self.ontology}

        User query:
        {query}

        SPARQL query:
        """

        # Get the response from the LLM
        response = await self.llm_manager.generate_text(prompt)

        # Execute the SPARQL query on the ontology
        results = self.ontology.query(response)

        return results
