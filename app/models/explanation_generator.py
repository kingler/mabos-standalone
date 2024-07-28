from typing import Dict, Any, List
from app.models.knowledge_base import KnowledgeBase
from app.models.reasoning_engine import ReasoningEngine

class ExplanationGenerator:
    """
    A class for generating explanations and providing evidence for decisions.
    """

    def __init__(self, knowledge_base: KnowledgeBase, reasoning_engine: ReasoningEngine):
        """
        Initialize the ExplanationGenerator.

        Args:
            knowledge_base (KnowledgeBase): The knowledge base to use for retrieving information.
            reasoning_engine (ReasoningEngine): The reasoning engine to use for generating logical steps.
        """
        self.knowledge_base = knowledge_base
        self.reasoning_engine = reasoning_engine

    def generate_explanation(self, decision: Dict[str, Any]) -> str:
        """
        Generate an explanation for a given decision.

        Args:
            decision (Dict[str, Any]): The decision to explain.

        Returns:
            str: The generated explanation.
        """
        explanation = f"Decision: {decision.get('action', 'No action specified')}\n\n"
        explanation += "Reasoning:\n"

        # Get relevant facts from the knowledge base
        relevant_facts = self.knowledge_base.get_relevant_facts(decision.get('context', {}))

        # Use the reasoning engine to generate logical steps
        reasoning_steps = self.reasoning_engine.generate_reasoning_steps(decision, relevant_facts)

        # Add reasoning steps to the explanation
        for step in reasoning_steps:
            explanation += f"- {step}\n"

        # Add any additional considerations or trade-offs
        if 'considerations' in decision:
            explanation += "\nAdditional Considerations:\n"
            for consideration in decision['considerations']:
                explanation += f"- {consideration}\n"

        # Include confidence level if available
        if 'confidence' in decision:
            explanation += f"\nConfidence Level: {decision['confidence']}%"

        return explanation

    def provide_evidence(self, explanation: str) -> Dict[str, Any]:
        """
        Provide evidence for the given explanation.

        Args:
            explanation (str): The explanation to provide evidence for.

        Returns:
            Dict[str, Any]: A dictionary containing various types of evidence.
        """
        evidence = {}
        
        # Extract key points from the explanation
        key_points = self._extract_key_points(explanation)
        
        # Gather supporting facts from the knowledge base
        for point in key_points:
            supporting_facts = self.knowledge_base.get_supporting_facts(point)
            if supporting_facts:
                evidence[point] = supporting_facts
        
        # Include relevant historical data or precedents
        historical_data = self.knowledge_base.get_historical_data(key_points)
        if historical_data:
            evidence['historical_data'] = historical_data
        
        # Add any relevant external sources or references
        external_sources = self.knowledge_base.get_external_sources(key_points)
        if external_sources:
            evidence['external_sources'] = external_sources
        
        # Include any relevant metrics or quantitative data
        metrics = self.knowledge_base.get_relevant_metrics(key_points)
        if metrics:
            evidence['metrics'] = metrics
        
        return evidence

    def _extract_key_points(self, explanation: str) -> List[str]:
        """
        Extract key points from the given explanation.

        Args:
            explanation (str): The explanation to extract key points from.

        Returns:
            List[str]: A list of extracted key points.
        """
        # This implementation could be enhanced with NLP techniques for better extraction
        return [line.strip('- ') for line in explanation.split('\n') if line.startswith('-')]