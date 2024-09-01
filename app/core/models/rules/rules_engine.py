from __future__ import annotations

import logging
import os
import sys
from typing import TYPE_CHECKING, Any, Callable, Dict, List

import git
from business_rule_engine import RuleParser

from app.core.agents.core_agents.llm_agent import LLMAgent
from app.core.models.knowledge.vocabulary_manager import VocabularyManager
from app.core.models.rules.rules import Rule, Rules  # Add this import
from app.core.tools.llm_manager import LLMManager

if TYPE_CHECKING:
    from app.core.agents.core_agents.llm_agent import LLMAgent

class RulesEngine:
    def __init__(self, llm_manager: LLMManager, llm_agent: 'LLMAgent', repo_path: str, vocabulary_manager: VocabularyManager):
        self.llm_manager = llm_manager
        self.llm_agent = llm_agent
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)
        self.vocabulary_manager = vocabulary_manager
        self.parser = RuleParser()
        self.rules = Rules()  # Use the Rules class instead of a string

    def initialize_llm_agent(self):
        from app.core.agents.core_agents.llm_agent import LLMAgent
        self.llm_agent = LLMAgent()

    async def generate_rules_from_description(self, description: str) -> str:
        prompt = f"Based on the following business description, generate business rules:\n\n{description}\n\nGenerate rules in the following format:\n\nrule \"rule name\"\nwhen\n    condition\nthen\n    action\nend\n\nProvide multiple rules, each separated by a newline."
        rules_str = await self.llm_manager.generate_text(prompt)
        self.rules = Rules.from_dict(self._parse_rules_string(rules_str))  # Parse and store rules
        return rules_str

    def _parse_rules_string(self, rules_str: str) -> List[Dict[str, str]]:
        # Implement parsing logic to convert rules_str to a list of dictionaries
        # This is a placeholder implementation
        rules_list = []
        for rule in rules_str.split("rule ")[1:]:
            name, rest = rule.split("\nwhen\n", 1)
            condition, action = rest.split("\nthen\n")
            rules_list.append({
                "name": name.strip('"'),
                "condition": condition.strip(),
                "action": action.split("\nend")[0].strip()
            })
        return rules_list

    async def interpret_and_store_rules(self, business_description: str):
        rules_str = await self.generate_rules_from_description(business_description)
        self.parser.parsestr(rules_str)
        self._store_rules_in_repo(rules_str)

    def _store_rules_in_repo(self, rules_str: str):
        rules_path = os.path.join(self.repo_path, "rules", "business_rules.txt")
        with open(rules_path, "w") as f:
            f.write(rules_str)
        self.repo.index.add([rules_path])
        self.repo.index.commit("Update business rules")

    def add_rule(self, condition: str, action: str):
        self.rules.add_rule(condition, action)
        rule_text = f"rule \"{condition}\"\nwhen\n    {condition}\nthen\n    {action}\nend"
        self.parser.parsestr(rule_text)

    def register_function(self, func: Callable):
        self.parser.register_function(func)

    def evaluate_rules(self, params: Dict[str, Any], set_default_arg: bool = False, default_arg: Any = None):
        try:
            return self.parser.execute(params, set_default_arg=set_default_arg, default_arg=default_arg)
        except ValueError as e:
            print(f"Error evaluating rules: {e}")
            return None

    def evaluate_rules_with_control(self, params: Dict[str, Any], set_default_arg: bool = False, default_arg: Any = None):
        results = []
        for rule in self.parser:
            try:
                rvalue_condition, rvalue_action = rule.execute(params, set_default_arg=set_default_arg, default_arg=default_arg)
                if rule.status:
                    results.append((rule.name, rvalue_action))
            except Exception as e:
                print(f"Error executing rule {rule.name}: {e}")
        return results

    async def reason_about_rules(self, query: str) -> str:
        prompt = f"Given the following business rules:\n\n{self.rules.to_dict()}\n\nAnswer the following query: {query}"
        return await self.llm_manager.generate_text(prompt)

    @staticmethod
    def enable_debug_logging():
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Example usage
if __name__ == "__main__":
    from app.core.agents.core_agents.llm_agent import LLMAgent
    from app.core.models.knowledge.vocabulary_manager import VocabularyManager
    from app.core.tools.llm_manager import LLMManager

    def order_more(items_to_order):
        print(f"Ordering {items_to_order} new items")
        return items_to_order

    def apply_discount(order_total, discount_rate):
        return order_total * (1 - discount_rate)

    llm_manager = LLMManager()
    llm_agent = LLMAgent("agent1", "Business Rule Agent", "your_api_key", None, None)
    vocabulary_manager = VocabularyManager()  # You might need to initialize this properly
    engine = RulesEngine(llm_manager, llm_agent, "/path/to/your/repo", vocabulary_manager)

    # Enable debug logging if needed
    # RulesEngine.enable_debug_logging()

    # Register custom functions
    engine.register_function(order_more)
    engine.register_function(apply_discount)

    # Define rules
    rules = """
    rule "order new items"
    when
        products_in_stock < 20
    then
        order_more(50)
    end

    rule "apply discount"
    when
        customer_loyalty_points >= 500 AND order_total >= 100
    then
        apply_discount(order_total, 0.1)
    end
    """

    # Parse rules
    engine.parser.parsestr(rules)

    # Evaluate rules
    params = {
        "products_in_stock": 15,
        "customer_loyalty_points": 600,
        "order_total": 200
    }

    result = engine.evaluate_rules(params)
    print(f"Rules evaluation result: {result}")

    # Evaluate rules with more control
    detailed_results = engine.evaluate_rules_with_control(params)
    for rule_name, action_result in detailed_results:
        print(f"Rule '{rule_name}' executed with result: {action_result}")

    # Reason about rules
    reasoning_query = "What happens when a customer with 1000 loyalty points places an order for $300?"
    reasoning_result = engine.reason_about_rules(reasoning_query)
    print(f"Reasoning result: {reasoning_result}")