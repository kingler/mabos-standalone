from typing import List
from app.models.business_plan import BusinessPlan
from app.models.agents.business_plan_agent import BusinessPlanAgent
from app.core.reasoner import Reasoner
from app.models.knowledge_base import KnowledgeBase

class BusinessPlanService:
    def __init__(self, knowledge_base: KnowledgeBase, api_key: str):
        self.reasoner = Reasoner(knowledge_base, api_key)
        self.business_plans = {}

    def create_business_plan(self, business_plan: BusinessPlan) -> BusinessPlan:
        agent = BusinessPlanAgent(business_plan, self.reasoner)
        self.business_plans[business_plan.id] = agent
        return business_plan

    def get_business_plan(self, plan_id: str) -> BusinessPlan:
        agent = self.business_plans.get(plan_id)
        if not agent:
            raise ValueError(f"Business plan with id {plan_id} not found")
        return agent.business_plan

    def update_business_plan(self, plan_id: str) -> BusinessPlan:
        agent = self.business_plans.get(plan_id)
        if not agent:
            raise ValueError(f"Business plan with id {plan_id} not found")
        agent.update_plan()
        return agent.business_plan

    def execute_action(self, plan_id: str, action_id: str) -> BusinessPlan:
        agent = self.business_plans.get(plan_id)
        if not agent:
            raise ValueError(f"Business plan with id {plan_id} not found")
        agent.execute_action(action_id)
        return agent.business_plan