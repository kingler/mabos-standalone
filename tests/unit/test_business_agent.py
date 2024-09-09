import unittest
from app.agents.core_agents.business_agent import BusinessAgent
from app.models.agent.belief import Belief
from app.models.agent.desire import Desire
from app.models.agent.intention import Intention

class TestBusinessAgent(unittest.TestCase):

    def setUp(self):
        self.agent = BusinessAgent(
            agent_id="123",
            name="BusinessAgent",
            business_id="456",
            any_field="test"
        )

    def test_update_belief(self):
        self.agent.update_belief("key1", "value1")
        self.assertIn("key1", self.agent.beliefs)
        self.assertEqual(self.agent.beliefs["key1"].value, "value1")

    def test_add_desire(self):
        desire = Desire(description="desire1", priority=1)
        self.agent.add_desire(desire)
        self.assertIn(desire, self.agent.desires)

    def test_set_intention(self):
        intention = Intention(goal={"description": "goal1", "priority": 1})
        self.agent.set_intention(intention)
        self.assertIn(intention, self.agent.intentions)

if __name__ == '__main__':
    unittest.main()