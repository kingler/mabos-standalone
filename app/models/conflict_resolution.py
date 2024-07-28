from typing import List, Dict, Any, Optional
from app.models.knowledge_base import KnowledgeBase
from app.models.ontology import Ontology
from app.models.rules_engine import Rules

class ConflictResolution:
    """
    A class to detect and resolve conflicts in the knowledge base.
    """

    def __init__(self, knowledge_base: KnowledgeBase, ontology: Ontology, domain_rules: Rules):
        """
        Initialize the ConflictResolution with knowledge base, ontology, and domain rules.

        Args:
            knowledge_base (KnowledgeBase): The knowledge base to check for conflicts.
            ontology (Ontology): The ontology to use for logical consistency checks.
            domain_rules (DomainRules): The domain-specific rules to apply.
        """
        self.knowledge_base = knowledge_base
        self.ontology = ontology
        self.domain_rules = domain_rules

    def detect_conflicts(self) -> List[Dict[str, Any]]:
        """
        Detect conflicts in the knowledge base.

        Returns:
            List[Dict[str, Any]]: A list of detected conflicts.
        """
        conflicts = []
        beliefs = self.knowledge_base.get_all_beliefs()
        
        for i, belief1 in enumerate(beliefs):
            for belief2 in beliefs[i+1:]:
                if self._are_contradictory(belief1, belief2):
                    conflicts.append({
                        "type": "contradiction",
                        "belief1": belief1,
                        "belief2": belief2
                    })
                elif self._are_logically_inconsistent(belief1, belief2):
                    conflicts.append({
                        "type": "logical_inconsistency",
                        "belief1": belief1,
                        "belief2": belief2
                    })
                elif self._have_temporal_conflict(belief1, belief2):
                    conflicts.append({
                        "type": "temporal_conflict",
                        "belief1": belief1,
                        "belief2": belief2
                    })
        
        # Check for ontology violations
        for belief in beliefs:
            if not self.ontology.is_consistent_with_ontology(belief):
                conflicts.append({
                    "type": "ontology_violation",
                    "belief": belief
                })
        
        return conflicts

    def _are_contradictory(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        """
        Check if two beliefs are contradictory.

        Args:
            belief1 (Dict[str, Any]): The first belief.
            belief2 (Dict[str, Any]): The second belief.

        Returns:
            bool: True if the beliefs are contradictory, False otherwise.
        """
        if belief1.get('predicate') != belief2.get('predicate'):
            return False

        if isinstance(belief1.get('value'), bool) and isinstance(belief2.get('value'), bool):
            return belief1['value'] != belief2['value']

        if isinstance(belief1.get('value'), (int, float)) and isinstance(belief2.get('value'), (int, float)):
            threshold = max(abs(belief1['value']), abs(belief2['value'])) * 0.1
            return abs(belief1['value'] - belief2['value']) > threshold

        if isinstance(belief1.get('value'), str) and isinstance(belief2.get('value'), str):
            opposites = {
                'true': 'false',
                'yes': 'no',
                'on': 'off',
                'active': 'inactive',
                'enabled': 'disabled'
            }
            return belief1['value'].lower() in opposites and belief2['value'].lower() == opposites[belief1['value'].lower()]

        if isinstance(belief1.get('value'), list) and isinstance(belief2.get('value'), list):
            return len(set(belief1['value']) & set(belief2['value'])) == 0

        return False

    def _are_logically_inconsistent(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        """
        Check if two beliefs are logically inconsistent.

        Args:
            belief1 (Dict[str, Any]): The first belief.
            belief2 (Dict[str, Any]): The second belief.

        Returns:
            bool: True if the beliefs are logically inconsistent, False otherwise.
        """
        if belief1.get('predicate') == 'is_a' and belief2.get('predicate') == 'is_a':
            if belief1.get('subject') == belief2.get('subject'):
                if self.ontology.are_mutually_exclusive(belief1.get('object'), belief2.get('object')):
                    return True

        if belief1.get('predicate') == belief2.get('predicate'):
            property_type = self.ontology.get_property_type(belief1.get('predicate'))
            if property_type == 'functional':
                if belief1.get('value') != belief2.get('value'):
                    return True
            elif property_type == 'inverse_functional':
                if belief1.get('value') == belief2.get('value') and belief1.get('subject') != belief2.get('subject'):
                    return True

        if self.domain_rules.violates_rule(belief1, belief2):
            return True

        if self.ontology.is_transitive(belief1.get('predicate')):
            transitive_beliefs = self.knowledge_base.get_transitive_beliefs(belief1)
            if any(self._are_contradictory(belief2, tb) for tb in transitive_beliefs):
                return True

        return False

    def _have_temporal_conflict(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> bool:
        """
        Check if two beliefs have a temporal conflict.

        Args:
            belief1 (Dict[str, Any]): The first belief.
            belief2 (Dict[str, Any]): The second belief.

        Returns:
            bool: True if the beliefs have a temporal conflict, False otherwise.
        """
        if belief1.get('predicate') == belief2.get('predicate') and belief1.get('value') != belief2.get('value'):
            time1 = belief1.get('time', {})
            time2 = belief2.get('time', {})
            return self._time_periods_overlap(time1, time2)
        return False

    def _time_periods_overlap(self, time1: Dict[str, Any], time2: Dict[str, Any]) -> bool:
        """
        Check if two time periods overlap.

        Args:
            time1 (Dict[str, Any]): The first time period.
            time2 (Dict[str, Any]): The second time period.

        Returns:
            bool: True if the time periods overlap, False otherwise.
        """
        start1, end1 = time1.get('start'), time1.get('end')
        start2, end2 = time2.get('start'), time2.get('end')
        
        if not all([start1, end1, start2, end2]):
            return False
        
        return start1 <= end2 and start2 <= end1

    def resolve_conflicts(self, conflicts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Resolve the detected conflicts.

        Args:
            conflicts (List[Dict[str, Any]]): The list of detected conflicts.

        Returns:
            List[Dict[str, Any]]: A list of resolved conflicts.
        """
        resolved_conflicts = []
        for conflict in conflicts:
            resolution = self._resolve_single_conflict(conflict)
            if resolution:
                resolved_conflicts.append(resolution)
        return resolved_conflicts

    def _resolve_single_conflict(self, conflict: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Resolve a single conflict.

        Args:
            conflict (Dict[str, Any]): The conflict to resolve.

        Returns:
            Optional[Dict[str, Any]]: The resolution for the conflict, or None if unresolvable.
        """
        conflict_type = conflict.get('type')
        belief1 = conflict.get('belief1')
        belief2 = conflict.get('belief2')

        if conflict_type == 'contradiction':
            return self._resolve_contradiction(belief1, belief2)
        elif conflict_type == 'logical_inconsistency':
            return self._resolve_logical_inconsistency(belief1, belief2)
        elif conflict_type == 'temporal_conflict':
            return self._resolve_temporal_conflict(belief1, belief2)
        elif conflict_type == 'ontology_violation':
            return self._resolve_ontology_violation(belief1)
        else:
            print(f"Unknown conflict type: {conflict_type}")
            return None

    def _resolve_contradiction(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve a contradiction between two beliefs.

        Args:
            belief1 (Dict[str, Any]): The first belief.
            belief2 (Dict[str, Any]): The second belief.

        Returns:
            Dict[str, Any]: The resolution action and the belief to keep.
        """
        if belief1.get('confidence', 0) > belief2.get('confidence', 0):
            return {'action': 'keep', 'belief': belief1}
        else:
            return {'action': 'keep', 'belief': belief2}

    def _resolve_logical_inconsistency(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve a logical inconsistency between two beliefs.

        Args:
            belief1 (Dict[str, Any]): The first belief.
            belief2 (Dict[str, Any]): The second belief.

        Returns:
            Dict[str, Any]: The resolution action and the belief to keep.
        """
        if self.ontology.is_more_specific(belief1.get('object'), belief2.get('object')):
            return {'action': 'keep', 'belief': belief1}
        else:
            return {'action': 'keep', 'belief': belief2}

    def _resolve_temporal_conflict(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve a temporal conflict between two beliefs.

        Args:
            belief1 (Dict[str, Any]): The first belief.
            belief2 (Dict[str, Any]): The second belief.

        Returns:
            Dict[str, Any]: The resolution action and the belief to keep.
        """
        time1 = belief1.get('time', {})
        time2 = belief2.get('time', {})
        if time1.get('end', float('inf')) > time2.get('end', float('inf')):
            return {'action': 'keep', 'belief': belief1}
        else:
            return {'action': 'keep', 'belief': belief2}

    def _resolve_ontology_violation(self, belief: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve an ontology violation for a belief.

        Args:
            belief (Dict[str, Any]): The belief violating the ontology.

        Returns:
            Dict[str, Any]: The resolution action and the adjusted or removed belief.
        """
        if self.ontology.can_adjust_belief(belief):
            adjusted_belief = self.ontology.adjust_belief(belief)
            return {'action': 'adjust', 'belief': adjusted_belief}
        else:
            return {'action': 'remove', 'belief': belief}