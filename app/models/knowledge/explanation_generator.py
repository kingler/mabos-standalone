from typing import Any, Dict, List

from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.reasoning_engine import \
    ReasoningEngine


class ExplanationGenerator:
    def __init__(self, knowledge_base: KnowledgeBase, reasoning_engine: ReasoningEngine):
        self.knowledge_base = knowledge_base
        self.reasoning_engine = reasoning_engine

    def generate_explanation(self, decision: Dict[str, Any]) -> str:
        # Implement explanation generation logic
        explanation = f"The decision '{decision['action']}' was made based on the following factors:\n"
        
        # Use reasoning engine to get the reasoning chain
        reasoning_chain = self.reasoning_engine.get_reasoning_chain(decision)
        
        for step in reasoning_chain:
            explanation += f"- {step['description']}\n"
            if 'supporting_facts' in step:
                for fact in step['supporting_facts']:
                    explanation += f"  * {fact}\n"
        
        return explanation

    def provide_evidence(self, explanation: str) -> Dict[str, Any]:
        # Provide supporting evidence for the explanation
        evidence = {
            "facts": [],
            "rules": [],
            "sources": []
        }
        
        # Extract key concepts from the explanation
        concepts = self.extract_concepts(explanation)
        
        # Find relevant facts in the knowledge base
        for concept in concepts:
            facts = self.knowledge_base.get_facts_by_concept(concept)
            evidence["facts"].extend(facts)
        
        # Find relevant rules used in the reasoning
        rules = self.reasoning_engine.get_rules_used(explanation)
        evidence["rules"].extend(rules)
        
        # Find sources of information
        for fact in evidence["facts"]:
            source = self.knowledge_base.get_source(fact)
            if source:
                evidence["sources"].append(source)
        
        return evidence

    def extract_concepts(self, text: str) -> List[str]:
        # This is a placeholder method. In a real implementation,
        # you might use NLP techniques to extract key concepts.
        return [word.strip() for word in text.split() if len(word.strip()) > 3]