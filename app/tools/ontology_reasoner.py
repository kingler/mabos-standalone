import asyncio
import json
from typing import Any, Dict

from tenacity import retry, stop_after_attempt, wait_exponential

from app.models.knowledge.ontology.ontology import Ontology
from app.tools.llm_manager import LLMManager


class OntologyReasoner:
    def __init__(self, llm_manager: LLMManager, ontology: Ontology):
        self.llm_manager = llm_manager
        self.ontology = ontology

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def infer_new_knowledge(self) -> Dict[str, Any]:
        prompt = f"""
        Given the following ontology:

        {self.ontology.to_json()}

        Infer new knowledge based on the existing concepts and relationships.
        Provide the inferred knowledge in JSON format with the following structure:
        {{
            "new_concepts": [
                {{
                    "name": "concept_name",
                    "description": "concept_description"
                }},
                ...
            ],
            "new_relationships": [
                {{
                    "name": "relationship_name",
                    "domain": "domain_concept",
                    "range": "range_concept"
                }},
                ...
            ]
        }}
        """

        selected_model = self.llm_manager.select_model("Ontology reasoning", required_capabilities=["multilingual"])
        response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
        return json.loads(response)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def answer_query(self, query: str) -> str:
        prompt = f"""
        Given the following ontology:

        {self.ontology.to_json()}

        Answer the following query based on the ontology:

        {query}

        Provide a detailed explanation of your reasoning process.
        """

        selected_model = self.llm_manager.select_model("Ontology query answering", required_capabilities=["multilingual"])
        return await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
