import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.monitoring_agent import MonitoringAgent

class TestMonitoringAgent(unittest.TestCase):

    def setUp(self):
        self.agent = MonitoringAgent()

    @patch('app.agents.meta_agents.monitoring_agent.psutil')
    @patch('app.agents.meta_agents.monitoring_agent.time')
    def test_collect_performance_metrics(self, mock_time, mock_psutil):
        mock_agent = MagicMock()
        mock_agent.run_simulation.return_value = None
        mock_psutil.Process().memory_info().rss = 1024 * 1024
        mock_psutil.cpu_percent.return_value = 50
        self.agent._collect_agent_metrics([mock_agent])
        self.assertIn(mock_agent.id, self.agent.performance_metrics)

if __name__ == '__main__':
    unittest.main()