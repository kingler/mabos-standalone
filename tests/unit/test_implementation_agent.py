import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.implementation_agent import ImplementationAgent
from app.models.agent.agent import Agent
from app.models.agent.belief import Belief
from app.models.agent.desire import Desire
from app.models.agent.intention import Intention
from app.models.agent.action import Action
from app.models.agent.agent_role import AgentRole

class TestImplementationAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ImplementationAgent(name="Implementer")

    def test_add_belief(self):
        self.agent.add_belief("Proper implementation is crucial for MAS success")
        self.assertEqual(len(self.agent.beliefs), 1)
        self.assertEqual(self.agent.beliefs[0].description, "Proper implementation is crucial for MAS success")

    def test_create_agent(self):
        agent_config = {
            "agent_id": "123",
            "name": "TestAgent",
            "agent_type": "reactive",
            "beliefs": [{"description": "Test belief", "certainty": 1.0}],
            "desires": [{"description": "Test desire", "priority": 1}],
            "intentions": [{"goal": {"description": "Test goal", "priority": 1}}],
            "available_actions": [{"name": "Test action", "description": "Test action description"}],
            "roles": ["Test role"]
        }
        new_agent = self.agent.create_agent("reactive", agent_config)
        self.assertIsInstance(new_agent, Agent)
        self.assertEqual(new_agent.agent_id, "123")
        self.assertEqual(new_agent.name, "TestAgent")

    def test_retire_agent(self):
        agent_config = {
            "agent_id": "123",
            "name": "TestAgent",
            "agent_type": "reactive",
            "beliefs": [],
            "desires": [],
            "intentions": [],
            "available_actions": [],
            "roles": []
        }
        self.agent.create_agent("reactive", agent_config)
        self.agent.retire_agent("reactive", "123")
        self.assertEqual(len(self.agent.active_agents["reactive"]), 0)

if __name__ == '__main__':
    unittest.main()