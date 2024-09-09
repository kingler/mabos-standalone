import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.operational_meta_agent import OperationalMetaAgent
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService
from app.services.plan_service import PlanService

class TestOperationalMetaAgent(unittest.TestCase):

    def setUp(self):
        self.agent_service = MagicMock(spec=AgentService)
        self.goal_service = MagicMock(spec=GoalService)
        self.plan_service = MagicMock(spec=PlanService)
        self.agent = OperationalMetaAgent(self.agent_service, self.goal_service, self.plan_service)

    def test_interpret_tactical_plans(self):
        plan = MagicMock()
        plan.steps = [MagicMock(description="step1")]
        result = self.agent.interpret_tactical_plans([plan])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["description"], "step1")

    def test_assign_tasks(self):
        operational_tasks = [{"description": "task1"}]
        self.agent_service.get_available_agents.return_value = [MagicMock()]
        result = self.agent.assign_tasks(operational_tasks)
        self.assertIn("unassigned", result)

if __name__ == '__main__':
    unittest.main()