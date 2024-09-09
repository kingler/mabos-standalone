import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.meta_mas import MetaMAS
from app.agents.meta_agents.implementation_agent import ImplementationAgent

class TestMetaMAS(unittest.TestCase):

    def setUp(self):
        self.meta_mas = MetaMAS()

    @patch('app.agents.meta_agents.meta_mas.MetaMAS.goal_achieved', return_value=True)
    def test_run_meta_mas(self, mock_goal_achieved):
        self.meta_mas.run_meta_mas()
        self.assertTrue(mock_goal_achieved.called)

    def test_facilitate_communication(self):
        agent1 = MagicMock()
        agent2 = MagicMock()
        agent1.beliefs = [MagicMock(description="belief1", certainty=1.0)]
        self.meta_mas.agents = [agent1, agent2]
        self.meta_mas.facilitate_communication()
        self.assertTrue(agent2.add_belief.called)

    def test_update_global_state(self):
        agent1 = MagicMock()
        agent1.tasks = [MagicMock(status="completed"), MagicMock(status="pending")]
        self.meta_mas.agents = [agent1]
        with patch('builtins.print') as mocked_print:
            self.meta_mas.update_global_state()
            mocked_print.assert_called_with("Overall progress: 50.00%")

if __name__ == '__main__':
    unittest.main()