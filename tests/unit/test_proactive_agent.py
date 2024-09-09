import unittest
from unittest.mock import patch, MagicMock
from app.agents.core_agents.proactive_agent import ProactiveAgent
from app.models.agent.goal import Goal
from app.models.agent.plan import Plan, PlanStep

class TestProactiveAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ProactiveAgent(agent_id="123", name="ProactiveAgent")

    def test_add_goal(self):
        goal = Goal(description="Test goal", priority=1)
        self.agent.add_goal(goal)
        self.assertIn(goal, self.agent.goals)

    def test_remove_goal(self):
        goal = Goal(description="Test goal", priority=1)
        self.agent.add_goal(goal)
        self.agent.remove_goal(goal)
        self.assertNotIn(goal, self.agent.goals)

    def test_deliberate(self):
        goal = Goal(description="Test goal", priority=1)
        self.agent.add_goal(goal)
        self.agent.deliberate()
        self.assertTrue(any(intention.goal == goal for intention in self.agent.intentions))

    def test_plan(self):
        goal = Goal(description="Test goal", priority=1)
        self.agent.add_goal(goal)
        self.agent.deliberate()
        self.agent.plan()
        self.assertTrue(any(plan.goal_id == goal.id for plan in self.agent.plans))

    def test_execute(self):
        goal = Goal(description="Test goal", priority=1)
        self.agent.add_goal(goal)
        self.agent.deliberate()
        self.agent.plan()
        self.agent.execute()
        self.assertTrue(any(plan.is_completed for plan in self.agent.plans))

if __name__ == '__main__':
    unittest.main()