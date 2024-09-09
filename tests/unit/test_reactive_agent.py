import unittest
from unittest.mock import patch, MagicMock
from app.agents.core_agents.reactive_agent import ReactiveAgent

class TestReactiveAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ReactiveAgent(agent_id="123", name="ReactiveAgent", api_key="test_api_key", llm_service="test_llm_service", agent_communication_service="test_communication_service")

    def test_add_rule(self):
        self.agent.add_rule("stimulus1", "response1")
        self.assertIn({"stimulus": "stimulus1", "response": "response1"}, self.agent.stimulus_response_rules)

    def test_perceive(self):
        self.agent.beliefs = [MagicMock(description="stimulus1")]
        self.agent.add_rule("stimulus1", "response1")
        self.agent.can_execute_action = MagicMock(return_value=True)
        self.agent.execute_action = MagicMock()
        self.agent.perceive()
        self.agent.execute_action.assert_called_with("response1")

    def test_can_execute_action(self):
        self.agent.get_action_requirements = MagicMock(return_value={"resource1": 1})
        self.agent.resources = {"resource1": 1}
        result = self.agent.can_execute_action("action1")
        self.assertTrue(result)

    def test_execute_action(self):
        self.agent.can_execute_action = MagicMock(return_value=True)
        self.agent.update_environment = MagicMock()
        self.agent.execute_action("action1")
        self.agent.update_environment.assert_called_with("action1")

if __name__ == '__main__':
    unittest.main()