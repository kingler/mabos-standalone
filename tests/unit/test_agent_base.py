import unittest
from unittest.mock import patch, MagicMock
from app.agents.base.agent_base import AgentBase
from app.models.message import ACLMessage, Performative

class TestAgentBase(unittest.TestCase):

    def setUp(self):
        self.agent = AgentBase(agent_id="123", name="AgentBase")

    def test_perceive(self):
        environment = {"key1": "value1"}
        self.agent.perceive(environment)
        self.assertTrue(any(belief.key == "key1" for belief in self.agent.beliefs))

    def test_deliberate(self):
        self.agent.add_desire("desire1", 1)
        self.agent.deliberate()
        self.assertTrue(any(intention.goal.description == "desire1" for intention in self.agent.intentions))

    def test_plan(self):
        self.agent.add_goal("goal1", 1)
        self.agent.deliberate()
        self.agent.plan()
        self.assertTrue(any(plan.goal_id == self.agent.goals[0].id for plan in self.agent.plans))

    def test_execute(self):
        action = MagicMock()
        self.agent.intentions = [MagicMock(has_plan=MagicMock(return_value=True), get_next_action=MagicMock(return_value=action))]
        self.agent.execute()
        action.execute.assert_called()

    def test_communicate(self):
        with patch('app.agents.base.agent_base.AgentBase._send_message') as mock_send_message:
            message = {"content": "test"}
            receiver_id = "456"
            self.agent.communicate(message, receiver_id)
            mock_send_message.assert_called()

    def test_update_belief(self):
        self.agent.update_belief("key1", "value1")
        self.assertTrue(any(belief.key == "key1" for belief in self.agent.beliefs))

    def test_add_desire(self):
        self.agent.add_desire("desire1", 1)
        self.assertTrue(any(desire.description == "desire1" for desire in self.agent.desires))

    def test_add_intention(self):
        desire = MagicMock(description="desire1", priority=1)
        self.agent.add_intention(desire)
        self.assertTrue(any(intention.goal.description == "desire1" for intention in self.agent.intentions))

    def test_generate_plan(self):
        goal = MagicMock()
        result = self.agent.generate_plan(goal)
        self.assertIsNone(result)

    def test_execute_action(self):
        action = MagicMock()
        self.agent.execute_action(action)
        action.execute.assert_called()

    def test_get_belief(self):
        self.agent.update_belief("key1", "value1")
        result = self.agent.get_belief("key1")
        self.assertEqual(result, "value1")

    def test_react(self):
        with patch('app.agents.base.agent_base.AgentBase.react') as mock_react:
            self.agent.react("stimulus")
            mock_react.assert_called()

    def test_add_goal(self):
        self.agent.add_goal("goal1", 1)
        self.assertTrue(any(goal.description == "goal1" for goal in self.agent.goals))

    def test_add_action(self):
        action = MagicMock()
        self.agent.add_action(action)
        self.assertIn(action, self.agent.available_actions)

    def test_update_resources(self):
        self.agent.update_resources("resource1", 10)
        self.assertEqual(self.agent.resources["resource1"], 10)

if __name__ == '__main__':
    unittest.main()