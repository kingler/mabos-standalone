import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.agent_design_agent import AgentDesignAgent

class TestAgentDesignAgent(unittest.TestCase):

    def setUp(self):
        self.agent = AgentDesignAgent()

    def test_design_agents(self):
        domain_requirements = {"requirement1": "details1"}
        result = self.agent.design_agents(domain_requirements)
        self.assertIn("agent_types", result)
        self.assertIn("agent_gbis", result)
        self.assertIn("agent_behaviors", result)
        self.assertIn("tropos_models", result)

if __name__ == '__main__':
    unittest.main()