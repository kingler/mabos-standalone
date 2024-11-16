import unittest
from src.reasoning.reasoning_engine import ReasoningEngine, Rule

class TestReasoningEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ReasoningEngine()

    def test_add_rule(self):
        self.engine.add_rule("temperature > 30", "turn_on_air_conditioning", 0.8)
        self.assertEqual(len(self.engine.rules), 1)
        self.assertEqual(self.engine.rules[0].condition, "temperature > 30")
        self.assertEqual(self.engine.rules[0].action, "turn_on_air_conditioning")
        self.assertEqual(self.engine.rules[0].probability, 0.8)

    def test_rule_based_reasoning(self):
        self.engine.add_rule("temperature > 30", "turn_on_air_conditioning", 0.8)
        self.engine.add_rule("humidity > 70", "turn_on_dehumidifier", 0.7)

        facts = {"temperature": 32, "humidity": 75}
        actions = self.engine.rule_based_reasoning(facts)

        self.assertEqual(len(actions), 2)
        self.assertIn("turn_on_air_conditioning", actions)
        self.assertIn("turn_on_dehumidifier", actions)

    def test_rule_based_reasoning_no_action(self):
        self.engine.add_rule("temperature > 30", "turn_on_air_conditioning", 0.8)

        facts = {"temperature": 25, "humidity": 60}
        actions = self.engine.rule_based_reasoning(facts)

        self.assertEqual(len(actions), 0)

    def test_probabilistic_reasoning(self):
        self.engine.add_rule("temperature > 30", "turn_on_air_conditioning", 0.8)
        self.engine.add_rule("humidity > 70", "turn_on_dehumidifier", 0.7)

        facts = {"temperature": 32, "humidity": 75}
        priors = {"temperature": 0.6, "humidity": 0.5}

        prob_actions = self.engine.probabilistic_reasoning(facts, priors)

        self.assertIn("turn_on_air_conditioning", prob_actions)
        self.assertIn("turn_on_dehumidifier", prob_actions)
        self.assertAlmostEqual(prob_actions["turn_on_air_conditioning"], 0.8571, places=4)
        self.assertAlmostEqual(prob_actions["turn_on_dehumidifier"], 0.7778, places=4)

    def test_probabilistic_reasoning_no_action(self):
        self.engine.add_rule("temperature > 30", "turn_on_air_conditioning", 0.8)

        facts = {"temperature": 25, "humidity": 60}
        priors = {"temperature": 0.6, "humidity": 0.5}

        prob_actions = self.engine.probabilistic_reasoning(facts, priors)

        self.assertEqual(len(prob_actions), 0)

    def test_probabilistic_reasoning_missing_prior(self):
        self.engine.add_rule("temperature > 30", "turn_on_air_conditioning", 0.8)

        facts = {"temperature": 32, "pressure": 1013}
        priors = {"temperature": 0.6}

        prob_actions = self.engine.probabilistic_reasoning(facts, priors)

        self.assertIn("turn_on_air_conditioning", prob_actions)
        self.assertAlmostEqual(prob_actions["turn_on_air_conditioning"], 0.8571, places=4)

    def test_bdi_reasoning(self):
        # This is a placeholder test as the method is not implemented yet
        beliefs = {"temperature": 32, "humidity": 75}
        desires = ["comfortable_environment"]
        intentions = []
        result = self.engine.bdi_reasoning(beliefs, desires, intentions)
        self.assertEqual(result, [])

    def test_goal_oriented_reasoning(self):
        # This is a placeholder test as the method is not implemented yet
        goal = "comfortable_environment"
        facts = {"temperature": 32, "humidity": 75}
        result = self.engine.goal_oriented_reasoning(goal, facts)
        self.assertEqual(result, [])

    def test_case_based_reasoning(self):
        # This is a placeholder test as the method is not implemented yet
        current_case = {"temperature": 32, "humidity": 75}
        case_base = []
        result = self.engine.case_based_reasoning(current_case, case_base)
        self.assertEqual(result, {})

    def test_temporal_reasoning(self):
        # This is a placeholder test as the method is not implemented yet
        timeline = [
            {"time": "09:00", "temperature": 25},
            {"time": "12:00", "temperature": 30},
            {"time": "15:00", "temperature": 32}
        ]
        result = self.engine.temporal_reasoning(timeline)
        self.assertEqual(result, [])

    def test_uncertainty_reasoning(self):
        # This is a placeholder test as the method is not implemented yet
        uncertain_facts = {"temperature": 0.7, "humidity": 0.8}
        result = self.engine.uncertainty_reasoning(uncertain_facts)
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()