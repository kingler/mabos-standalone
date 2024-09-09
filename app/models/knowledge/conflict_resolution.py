from typing import Any, Dict, List

from app.models.knowledge.knowledge_base import KnowledgeBase


class ConflictResolution:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def detect_conflicts(self) -> List[Dict[str, Any]]:
        conflicts = []
        beliefs = self.knowledge_base.get_all_beliefs()
        
        for i, belief1 in enumerate(beliefs):
            for belief2 in beliefs[i+1:]:
                if self._are_conflicting(belief1, belief2):
                    conflicts.append({
                        "type": "belief_conflict",
                        "belief1": belief1,
                        "belief2": belief2
                    })
        
        return conflicts

    def resolve_conflicts(self, conflicts: List[Dict[str, Any]]):
        for conflict in conflicts:
            if conflict["type"] == "belief_conflict":
                self._resolve_belief_conflict(conflict["belief1"], conflict["belief2"])

    def _are_conflicting(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        # Check if beliefs have the same subject but contradictory predicates
        return (belief1.get("subject") == belief2.get("subject") and
                belief1.get("predicate") != belief2.get("predicate"))

    def _resolve_belief_conflict(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve a conflict between two beliefs by keeping the more recent one.

        Args:
            belief1 (Dict[str, Any]): The first conflicting belief.
            belief2 (Dict[str, Any]): The second conflicting belief.

        Returns:
            Dict[str, Any]: The belief that should be kept.
        """
        if belief1.get("timestamp", 0) > belief2.get("timestamp", 0):
            return belief1
        else:
            return belief2