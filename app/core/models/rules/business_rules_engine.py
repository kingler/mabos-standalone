import json
import git
from typing import Dict, Any
from rules import Rules
from core.agents.core_agents.business_agent import BusinessAgent

class BusinessRule:
    def __init__(self, name: str, condition: str, action: str):
        self.name = name
        self.condition = condition
        self.action = action

class BusinessRulesEngine:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.rules = Rules()
        self.repo = git.Repo(repo_path)

    def load_rules(self, version: str):
        self.repo.git.checkout(version)
        with open(f"{self.repo_path}/business_rules.json", "r") as file:
            rules_data = json.load(file)
            for rule in rules_data:
                self.rules.add_rule(
                    condition=lambda agent, cond=rule["condition"]: eval(cond, globals(), self._get_agent_context(agent)),
                    action=lambda agent, act=rule["action"]: self._execute_action(agent, act)
                )

    def _get_agent_context(self, agent: BusinessAgent) -> Dict[str, Any]:
        context = {
            "purchase_history": agent.beliefs.get("purchase_history", Belief(description="purchase_history", certainty=1.0, value=[])).value,
            "email": agent.beliefs.get("email", Belief(description="email", certainty=1.0, value="")).value,
            "loyalty_points": agent.beliefs.get("loyalty_points", Belief(description="loyalty_points", certainty=1.0, value=0)).value,
        }
        return context

    def _execute_action(self, agent: BusinessAgent, action: str):
        if action == "add_vip_flag":
            agent.update_belief("is_vip", True)
        elif action == "standardize_email":
            agent.update_belief("email", agent.beliefs["email"].value.lower())
        elif action == "apply_loyalty_discount":
            discount = min(agent.beliefs["loyalty_points"].value // 100, 20)  # Max 20% discount
            agent.update_belief("discount", discount)

    def execute_rules(self, agent: BusinessAgent):
        self.rules.evaluate(agent)

# Helper functions used in business rules
def sum(purchase_history):
    return sum(purchase_history)

def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
if __name__ == "__main__":
    # Initialize the business rules engine
    engine = BusinessRulesEngine("path/to/business-rules-repo")
    engine.load_rules("main")  # Load the latest version of the rules

    # Create a business agent
    agent = BusinessAgent(business_id="B001", any_field="Some value")

    # Update agent's beliefs
    agent.update_belief("purchase_history", [100, 200, 150, 300])
    agent.update_belief("email", "John.Doe@Example.com")
    agent.update_belief("loyalty_points", 500)

    print("Original agent data:", agent.beliefs)

    # Execute business rules
    engine.execute_rules(agent)

    print("Agent data after applying business rules:", agent.beliefs)
