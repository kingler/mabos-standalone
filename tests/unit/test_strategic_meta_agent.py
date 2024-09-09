import unittest
import asyncio
from unittest.mock import MagicMock
from app.agents.meta_agents.strategic_meta_agent import StrategicMetaAgent
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService
from app.services.plan_service import PlanService

class TestStrategicMetaAgent(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        self.agent_service = MagicMock(spec=AgentService)
        self.agent_service.get_available_resources = MagicMock(return_value={"resource1": 10, "resource2": 20})
        self.agent_service.allocate_resources = MagicMock(return_value={"resource1": 5, "resource2": 10})
        self.agent_service.update_available_resources = MagicMock(return_value={"resource1": 5, "resource2": 10})
        self.agent_service.get_system_performance = MagicMock(return_value={"performance": "good"})
        self.goal_service = MagicMock(spec=GoalService)
        self.goal_service.generate_strategic_goals = MagicMock(return_value=["goal1", "goal2"])
        self.goal_service.get_goal_progress = MagicMock(return_value={"goal_progress": 0.4})
        self.goal_service.estimate_required_resources = MagicMock(return_value={"resource1": 5, "resource2": 10})
        self.goal_service.get_active_goals = MagicMock(return_value=["goal1", "goal2"])
        self.plan_service = MagicMock(spec=PlanService)
        self.plan_service.get_active_plans = MagicMock(return_value=[MagicMock(id="plan1"), MagicMock(id="plan2")])
        self.plan_service.get_plans_for_goal = MagicMock(return_value=[MagicMock(id="plan1"), MagicMock(id="plan2")])
        self.plan_service.get_plan_progress = MagicMock(return_value={"progress": 50, "expected_progress": 60})
        self.agent = StrategicMetaAgent(
            self.agent_service, 
            self.goal_service, 
            self.plan_service, 
            agent_id="test_id", 
            name="test_name", 
            api_key="test_api_key", 
            llm_service="test_llm_service", 
            agent_communication_service="test_communication_service"
        )

    def test_analyze_system_state(self):
        result = self.agent.analyze_system_state()
        self.assertIsInstance(result, dict)

    def test_generate_strategic_goals(self):
        result = self.agent.generate_strategic_goals()
        self.assertIsInstance(result, list)

    def test_allocate_resources(self):
        goals = [MagicMock()]
        result = self.agent.allocate_resources(goals)
        self.assertIsInstance(result, dict)

    def test_monitor_progress(self):
        goals = [MagicMock()]
        result = self.agent.monitor_progress(goals)
        self.assertIsInstance(result, dict)

    def test_adjust_strategy(self):
        progress = {"goal1": "in_progress"}
        result = self.agent.adjust_strategy(progress)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()