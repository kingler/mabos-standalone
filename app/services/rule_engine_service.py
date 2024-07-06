from typing import Dict, Any

from app.core.reasoning_engine import ReasoningEngine


class RulesService:
    @staticmethod
    def get_all_rules():
        # Logic to get all rules
        rules = []
        # Assuming rules are stored in a database or file
        # Retrieve all rules from the storage
        # For example, if using a database:
        # db_rules = db.query("SELECT * FROM rules")
        # for rule in db_rules:
        #     rules.append(rule)
        return rules

    @staticmethod
    def create_rule(rule: dict):
        # Logic to create a new rule
        # Assuming rules are stored in a database or file
        # Validate the rule data
        if not rule.get('name') or not rule.get('condition') or not rule.get('action'):
            raise ValueError("Invalid rule data")
        
        # Save the rule to the storage
        # For example, if using a database:
        # db.execute("INSERT INTO rules (name, condition, action) VALUES (?, ?, ?)", 
        #            (rule['name'], rule['condition'], rule['action']))
        
        # Return the created rule
        return rule


class RuleEngineService:
    @staticmethod
    def execute(context: dict):
        # Logic to execute the rule engine
        rules = RulesService.get_all_rules()
        
        for rule in rules:
            # Evaluate the rule condition against the context
            if eval(rule['condition'], context):
                # Execute the rule action
                exec(rule['action'], context)
        
        # Return the updated context after rule execution
        return context


def _rule_based_reasoning(self, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Perform rule-based reasoning using the rules engine.

    Args:
        context (Dict[str, Any]): The context for reasoning.

    Returns:
        Dict[str, Any]: The results of rule-based reasoning.
    """
    # def post(category: str, fact: Dict[str, Any]):
    #     # Placeholder for the actual implementation of the post function
    #     print(f"Posting to {category}: {fact}")

    # results = {}
    # for fact in context.get('facts', []):
    #     post('business', fact)
    #     # Collect results from the rules engine
    #     results[fact['subject']] = 'processed'
    # return results


if __name__ == "__main__":
    # Example usage
    context = {
        "facts": [
            {"subject": "user", "predicate": "has", "object": "account"},
            {"subject": "user", "predicate": "has", "object": "credit_card"},
        ]
    }
    reasoning_engine = ReasoningEngine()
    results = reasoning_engine.reason(context)
    print("Results:", results)
