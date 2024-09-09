import unittest
import asyncio
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.tactical_meta_agent import TacticalMetaAgent
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService
from app.services.plan_service import PlanService
from app.models.agent.plan import Plan

class TestTacticalMetaAgent(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.get_event_loop()
        self.agent_service = MagicMock()
        self.goal_service = MagicMock()
        self.plan_service = MagicMock()
        self.plan_service.get_plan_progress = MagicMock(return_value={"progress": 50, "expected_progress": 60})
        self.plan_service.get_all_plans = MagicMock(return_value=[MagicMock(spec=Plan)])
        self.goal_service.break_down_goal = MagicMock(return_value=["sub_goal1", "sub_goal2"])
        self.agent = TacticalMetaAgent(
            self.agent_service, 
            self.goal_service, 
            self.plan_service, 
            agent_id="test_id", 
            name="test_name", 
            api_key="test_api_key", 
            llm_service="test_llm_service", 
            agent_communication_service="test_communication_service"
        )

    def test_decompose_strategic_goals(self):
        strategic_goals = [MagicMock()]
        result = self.agent.decompose_strategic_goals(strategic_goals)
        self.assertIsInstance(result, list)

    def test_generate_tactical_plans(self):
        tactical_goals = [MagicMock()]
        result = self.agent.generate_tactical_plans(tactical_goals)
        self.assertIsInstance(result, list)

    def test_coordinate_agents(self):
        self.loop.run_until_complete(self._test_coordinate_agents())

    async def _test_coordinate_agents(self):
        # Your async test code here
        pass

    def test_monitor_tactical_execution(self):
        tactical_plans = [MagicMock(spec=Plan, id="plan1"), MagicMock(spec=Plan, id="plan2")]
        result = self.agent.monitor_tactical_execution(tactical_plans)
        self.assertIn("plan1", result)
        self.assertIn("plan2", result)
        self.assertEqual(result["plan1"]["progress"], 50)
        self.assertEqual(result["plan1"]["expected_progress"], 60)

    def test_adjust_tactics(self):
        execution_status = {"progress": 40, "expected_progress": 50}
        result = self.agent.adjust_tactics(execution_status)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()