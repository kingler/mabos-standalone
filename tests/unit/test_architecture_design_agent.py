import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.architecture_design_agent import ArchitectureDesignAgent

class TestArchitectureDesignAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ArchitectureDesignAgent()

    def test_process(self):
        input_data = {"key": "value"}
        result = self.agent.process(input_data)
        self.assertIn("mas_structure", result)
        self.assertIn("communication_protocols", result)
        self.assertIn("interaction_patterns", result)
        self.assertIn("data_flow_design", result)
        self.assertIn("storage_mechanisms", result)

if __name__ == '__main__':
    unittest.main()