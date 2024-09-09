import unittest
from unittest.mock import patch, MagicMock
from app.agents.core_agents.environmental_agent import EnvironmentalAgent
from app.models.agent.belief import Belief

class TestEnvironmentalAgent(unittest.TestCase):

    def setUp(self):
        self.agent = EnvironmentalAgent(agent_id="123", name="EnvAgent")

    def test_update_environment_state(self):
        new_state = {"temperature": 25}
        self.agent.update_environment_state(new_state)
        self.assertIn("temperature", self.agent.environment_state)
        self.assertEqual(self.agent.environment_state["temperature"], 25)

    def test_perceive(self):
        self.agent.update_environment_state({"temperature": 25})
        self.agent.perceive()
        self.assertTrue(any(belief.description == "temperature" for belief in self.agent.beliefs))

    def test_act(self):
        self.agent.update_environment_state({"temperature": 25})
        self.agent.perceive()
        self.agent.act()
        self.assertTrue(any(intention.status == "completed" for intention in self.agent.intentions))

if __name__ == '__main__':
    unittest.main()