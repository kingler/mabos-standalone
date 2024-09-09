import unittest
from unittest.mock import patch, MagicMock
from app.agents.core_agents.maintenance_agent import MaintenanceAgent
from app.services.repository_service import RepositoryService

class TestMaintenanceAgent(unittest.TestCase):

    def setUp(self):
        self.repository_service = MagicMock(spec=RepositoryService)
        self.agent = MaintenanceAgent(agent_id="123", name="MaintenanceAgent", repository_service=self.repository_service)

    def test_perform_maintenance(self):
        self.repository_service.cache = {"key1": "value1", "key2": "value2"}
        self.agent.is_outdated = MagicMock(side_effect=[True, False])
        self.agent.perform_maintenance()
        self.assertNotIn("key1", self.repository_service.cache)
        self.assertIn("key2", self.repository_service.cache)

if __name__ == '__main__':
    unittest.main()