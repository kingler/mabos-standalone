import asyncio
from typing import List

from app.models.knowledge.vocabulary_manager import VocabularyManager
from app.models.rules.rules_engine import BusinessRule
from app.tools.llm_manager import LLMManager


class SemanticFormulationGenerator:
    def __init__(self, vocabulary_manager: VocabularyManager):
        self.vocabulary_manager = vocabulary_manager

    def generate_formulation(self, rule: BusinessRule) -> str:
        # Retrieve definitions for terms in the rule formulation
        terms = rule.formulation.split()
        definitions = [self.vocabulary_manager.get_definition(term) for term in terms]

        # Generate a prompt for the LLM to create a formal semantic formulation
        prompt = f"Generate a formal semantic formulation for the rule: {rule.formulation} with modality {rule.modality}. Definitions: {definitions}"

        # Use LLMManager to generate the formal semantic formulation
        llm_manager = LLMManager()
        return asyncio.run(llm_manager.generate_text(prompt))

    def generate_formulations(self, rules: List[BusinessRule]) -> List[str]:
        return [self.generate_formulation(rule) for rule in rules]