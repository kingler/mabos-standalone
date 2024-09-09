import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.requirements_analysis_agent import RequirementsAnalysisAgent

class TestRequirementsAnalysisAgent(unittest.TestCase):

    def setUp(self):
        self.agent = RequirementsAnalysisAgent(
            agent_id="123", 
            name="ReqAnalyzer", 
            api_key="test_api_key", 
            llm_service="test_llm_service", 
            agent_communication_service="test_communication_service")

    def test_reason(self):
        self.agent.add_belief("Stakeholder feedback received")
        self.agent.reason()
        self.assertTrue(any(goal.description == "Revise requirements based on feedback" for goal in self.agent.goals))

    def test_plan(self):
        self.agent.add_goal("Revise requirements based on feedback", priority=8)
        self.agent.plan()
        self.assertTrue(any(plan.goal_id == self.agent.goals[0].id for plan in self.agent.plans))

if __name__ == '__main__':
    unittest.main()