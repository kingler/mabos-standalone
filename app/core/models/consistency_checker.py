from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.ontology.ontology import Ontology
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from app.core.models.rules import Rules

class InconsistencyResolver(ABC):
    @abstractmethod
    def resolve(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        pass

class ContradictionResolver(InconsistencyResolver):
    def resolve(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        if belief1.get('timestamp', 0) > belief2.get('timestamp', 0):
            self.knowledge_base.remove_belief(belief2)
        else:
            self.knowledge_base.remove_belief(belief1)
        return True

class LogicalInconsistencyResolver(InconsistencyResolver):
    def resolve(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        if self.ontology.is_more_specific(belief1, belief2):
            self.knowledge_base.remove_belief(belief2)
            return True
        elif self.ontology.is_more_specific(belief2, belief1):
            self.knowledge_base.remove_belief(belief1)
            return True
        return False

class ConsistencyChecker:
    def __init__(self, knowledge_base: KnowledgeBase, ontology: Ontology, domain_rules: Rules):
        self.knowledge_base = knowledge_base
        self.ontology = ontology
        self.domain_rules = domain_rules
        self.resolvers = {
            "contradiction": ContradictionResolver(),
            "logical_inconsistency": LogicalInconsistencyResolver(),
            # Add more resolvers as needed
        }

    def check_consistency(self):
        inconsistencies = []
        beliefs = self.knowledge_base.get_all_beliefs()
        
        for i, belief1 in enumerate(beliefs):
            for belief2 in beliefs[i+1:]:
                # Check for direct contradictions
                if self._are_contradictory(belief1, belief2):
                    inconsistencies.append({
                        "type": "contradiction",
                        "belief1": belief1,
                        "belief2": belief2
                    })
                
                # Check for logical inconsistencies
                elif self._are_logically_inconsistent(belief1, belief2):
                    inconsistencies.append({
                        "type": "logical_inconsistency",
                        "belief1": belief1,
                        "belief2": belief2
                    })
                
                # Check for domain-specific rule violations
                rule_violations = self.domain_rules.check_rules(belief1, belief2)
                if rule_violations:
                    inconsistencies.extend(rule_violations)
        
        return inconsistencies

    def _are_contradictory(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        """
        Check if two beliefs are directly contradictory.

        Args:
            belief1 (Dict[str, Any]): The first belief to compare.
            belief2 (Dict[str, Any]): The second belief to compare.

        Returns:
            bool: True if the beliefs are contradictory, False otherwise.
        """
        if belief1.get("subject") == belief2.get("subject"):
            if belief1.get("predicate") == belief2.get("predicate"):
                return belief1.get("object") != belief2.get("object")
            elif belief1.get("predicate") == f"not_{belief2.get('predicate')}":
                return True
        return False

    def _are_logically_inconsistent(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        # Implement logic to check if two beliefs are logically inconsistent
        # This could involve using the ontology to check for incompatible concepts
        return self.ontology.are_incompatible(belief1, belief2)

    def resolve_inconsistencies(self, inconsistencies: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        resolved_inconsistencies = []
        for inconsistency in inconsistencies:
            resolver = self.resolvers.get(inconsistency["type"])
            if resolver and resolver.resolve(inconsistency["belief1"], inconsistency["belief2"]):
                resolved_inconsistencies.append(inconsistency)
        return resolved_inconsistencies