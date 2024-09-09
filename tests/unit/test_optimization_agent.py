import unittest
from unittest.mock import patch, MagicMock
from app.agents.meta_agents.optimization_agent import OptimizationAgent

class TestOptimizationAgent(unittest.TestCase):

    def setUp(self):
        self.agent = OptimizationAgent()

    def test_suggest_optimizations(self):
        bottlenecks = ["high execution time", "high memory usage"]
        result = self.agent.suggest_optimizations(bottlenecks)
        self.assertIn("high execution time", result)
        self.assertIn("high memory usage", result)

    def test_implement_optimizations(self):
        mas_implementation = {"component1": "details1"}
        optimizations = {"component1": {"action": "optimize"}}
        result = self.agent.implement_optimizations(mas_implementation, optimizations)
        self.assertIn("component1", result)

    def test_provide_insights(self):
        performance_metrics = {"metric1": "value1"}
        optimizations = {"optimization1": "details1"}
        result = self.agent.provide_insights(performance_metrics, optimizations)
        self.assertIn("metric1", result)

    def test_optimize_mas(self):
        mas_implementation = {"component1": "details1"}
        feedback = {"metric1": "value1"}
        result = self.agent.optimize_mas(mas_implementation, feedback)
        self.assertIn("component1", result)

if __name__ == '__main__':
    unittest.main()