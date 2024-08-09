from typing import List, Dict

class Rule:
    def __init__(self, condition: str, action: str):
        self.condition = condition
        self.action = action

class Rules:
    def __init__(self):
        self.rules: List[Rule] = []

    def add_rule(self, condition: str, action: str):
        self.rules.append(Rule(condition, action))

    def get_rules(self) -> List[Rule]:
        return self.rules

    def to_dict(self) -> List[Dict[str, str]]:
        return [{"condition": rule.condition, "action": rule.action} for rule in self.rules]

    @classmethod
    def from_dict(cls, rules_dict: List[Dict[str, str]]) -> 'Rules':
        rules = cls()
        for rule in rules_dict:
            rules.add_rule(rule['condition'], rule['action'])
        return rules
