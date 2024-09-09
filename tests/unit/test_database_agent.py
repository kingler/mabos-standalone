import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.database_agent import DatabaseAgent
from app.models.agent.action import Action
from app.models.agent.agent import Agent

class TestDatabaseAgent(unittest.TestCase):

    def setUp(self):
        self.agent = DatabaseAgent(agent_id="123", name="DatabaseAgent", role="TestRole")

    @patch('app.services.database_service.DatabaseService')
    def test_create_action(self, mock_database_service):
        action = Action(name="TestAction", description="Test action description")
        mock_database_service.create_action.return_value = action
        result = self.agent.create_action(action)
        self.assertEqual(result, action)

    @patch('app.services.database_service.DatabaseService')
    def test_get_all_actions(self, mock_database_service):
        actions = [Action(name="TestAction1", description="Test action 1"), Action(name="TestAction2", description="Test action 2")]
        mock_database_service.get_all_actions.return_value = actions
        result = self.agent.get_all_actions()
        self.assertEqual(result, actions)

    @patch('app.services.database_service.DatabaseService')
    def test_get_action(self, mock_database_service):
        action = Action(name="TestAction", description="Test action description")
        mock_database_service.get_action.return_value = action
        result = self.agent.get_action("123")
        self.assertEqual(result, action)

    @patch('app.services.database_service.DatabaseService')
    def test_update_action(self, mock_database_service):
        action = Action(name="TestAction", description="Test action description")
        mock_database_service.update_action.return_value = action
        result = self.agent.update_action(action)
        self.assertEqual(result, action)

    @patch('app.services.database_service.DatabaseService')
    def test_delete_action(self, mock_database_service):
        mock_database_service.delete_action.return_value = True
        result = self.agent.delete_action("123")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()