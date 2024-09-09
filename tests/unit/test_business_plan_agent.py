import unittest
from app.agents.core_agents.business_plan_agent import BusinessPlanAgent, BusinessPlanTemplate

class TestBusinessPlanAgent(unittest.TestCase):

    def setUp(self):
        self.agent = BusinessPlanAgent(location="test_location")

    def test_develop_business_plan(self):
        plan_details = {
            "executive_summary": "summary",
            "company_description": "description",
            "market_analysis": {},
            "organization_management": "management",
            "service_product_line": "product line",
            "marketing_sales": "sales",
            "funding_request": "request",
            "financial_projections": {},
            "appendix": "appendix"
        }
        plan = self.agent.develop_business_plan(plan_details)
        self.assertIsInstance(plan, BusinessPlanTemplate)
        self.assertEqual(plan.executive_summary, "summary")

if __name__ == '__main__':
    unittest.main()