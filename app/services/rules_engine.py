"""
Unified Rules Engine Service
Combines functionality from both rule_engine_service.py and rules_service.py
"""
from typing import Any, Dict, List, Union

from pydantic import BaseModel
from rdflib import URIRef

from app.tools.reasoner import Reasoner
from app.models.rules.rules_engine import RuleModel, RulesEngine


class URIRefModel(BaseModel):
    value: str

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, URIRef):
            return v
        if isinstance(v, str):
            return URIRef(v)
        raise ValueError('Invalid URIRef')

    def __repr__(self):
        return f'URIRef({self.value})'


class RulesService:
    """
    Unified service for managing and executing business rules and rule-based reasoning.
    """
    def __init__(self):
        self.rules_engine = RulesEngine()
        self.reasoning_engine = Reasoner()

    def get_all_rules(self) -> List[Dict[str, Any]]:
        """Get all registered rules."""
        return [
            {
                "name": rule.name,
                "condition": rule.condition.__name__,
                "action": rule.action.__name__
            }
            for rule in self.rules_engine.rules
        ]

    def create_rule(self, rule: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new rule.
        
        Args:
            rule: Dictionary containing rule definition with name, condition, and action
        
        Returns:
            The created rule
        
        Raises:
            ValueError: If rule data is invalid
        """
        if not rule.get('name') or not rule.get('condition') or not rule.get('action'):
            raise ValueError("Invalid rule data: must contain name, condition, and action")
        
        rule_model = RuleModel(**rule)
        self.rules_engine.add_rule(rule_model)
        
        return rule

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute rules against the provided context.
        
        Args:
            context: The execution context containing facts and data
        
        Returns:
            Updated context after rule execution
        """
        return self.rules_engine.execute(context)

    def generate_business_rules(self, business_id: str) -> Dict[str, Any]:
        """
        Generate business-specific rules.
        
        Args:
            business_id: Identifier for the business
        
        Returns:
            Generated business rules
        """
        return self.rules_engine.generate_business_rules(business_id)

    def agent_action(self, action_id: Union[str, URIRef], business_id: Union[str, URIRef]) -> Dict[str, str]:
        """
        Execute an agent action within the context of business rules.
        
        Args:
            action_id: Identifier for the action
            business_id: Identifier for the business context
        
        Returns:
            Result of the action execution
        """
        try:
            action_id = URIRef(action_id) if isinstance(action_id, str) else action_id
            business_id = URIRef(business_id) if isinstance(business_id, str) else business_id
            self.rules_engine.agent_action(action_id, business_id)
            return {"message": f"Action '{action_id}' executed successfully for business '{business_id}'"}
        except Exception as e:
            return {"error": str(e)}

    def check_agent_rules(self, belief1: Dict[str, Any], belief2: Dict[str, Any]) -> Dict[str, bool]:
        """
        Check if agent beliefs satisfy rules.
        
        Args:
            belief1: First belief to check
            belief2: Second belief to check
        
        Returns:
            Dictionary indicating if rules are satisfied
        """
        result = self.rules_engine.check_agent_rules(belief1, belief2)
        return {"rules_satisfied": result}

    def rule_based_reasoning(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform rule-based reasoning on the provided context.
        
        Args:
            context: The reasoning context containing facts
        
        Returns:
            Results of the reasoning process
        """
        return self.reasoning_engine.reason(context)


# Kept for backwards compatibility
class RuleEngineService(RulesService):
    """Legacy class name maintained for backward compatibility."""
    pass


if __name__ == "__main__":
    # Example usage
    context = {
        "facts": [
            {
                "subject": URIRef("http://example.com/user"),
                "predicate": URIRef("http://example.com/has"),
                "object": URIRef("http://example.com/account")
            },
            {
                "subject": URIRef("http://example.com/user"),
                "predicate": URIRef("http://example.com/has"),
                "object": URIRef("http://example.com/credit_card")
            },
        ]
    }
    rules_service = RulesService()
    results = rules_service.rule_based_reasoning(context)
    print("Results:", results)
