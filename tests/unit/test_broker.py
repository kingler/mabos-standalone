import unittest
from unittest.mock import patch, MagicMock
from app.agents.core_agents.broker import Broker

class TestBroker(unittest.TestCase):

    def setUp(self):
        self.broker = Broker()

    def test_register_agent(self):
        self.broker.register_agent("Agent1", "Location1")
        self.assertIn("Agent1", self.broker.agents)
        self.assertEqual(self.broker.agents["Agent1"], "Location1")

    def test_unregister_agent(self):
        self.broker.register_agent("Agent1", "Location1")
        self.broker.unregister_agent("Agent1")
        self.assertNotIn("Agent1", self.broker.agents)

    def test_route_message(self):
        self.broker.register_agent("Agent1", "Location1")
        result = self.broker.route_message("Sender", "Agent1", "Test message")
        self.assertTrue(result)

    def test_get_agent_location(self):
        self.broker.register_agent("Agent1", "Location1")
        location = self.broker.get_agent_location("Agent1")
        self.assertEqual(location, "Location1")

    def test_list_agents(self):
        self.broker.register_agent("Agent1", "Location1")
        agents = self.broker.list_agents()
        self.assertIn("Agent1", agents)

if __name__ == '__main__':
    unittest.main()