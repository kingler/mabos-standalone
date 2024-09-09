# mabos/agents/business_plan_agent.py
from pydantic import BaseModel

from app.agents.core_agents.broker import Broker
from app.models.communication import AgentCommunication
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.knowledge.knowledge_graph import KnowledgeGraph
from app.tools.reasoning_engine import Reasoning
from app.models.skills import (CommunicationSkill, ExecutionSkill,
                                    LearningSkill, PerceptionSkill,
                                    PlanningSkill)


class BusinessPlanTemplate(BaseModel):
    executive_summary: str
    company_description: str
    market_analysis: dict
    organization_management: str
    service_product_line: str
    marketing_sales: str
    funding_request: str
    financial_projections: dict
    appendix: str

class BusinessPlanAgent(BaseModel):
    location: str
    knowledge_base: KnowledgeBase
    knowledge_graph: KnowledgeGraph
    communication: AgentCommunication
    reasoning: Reasoning
    skills: dict

    def __init__(self, location):
        self.location = location
        self.knowledge_base = KnowledgeBase()
        self.knowledge_graph = KnowledgeGraph()
        self.communication = AgentCommunication(self, self.knowledge_base, self.knowledge_graph)
        self.reasoning = Reasoning(self.knowledge_base, self.knowledge_graph)
        self.skills = {
            "planning": PlanningSkill(self),
            "execution": ExecutionSkill(self),
            "communication": CommunicationSkill(self),
            "learning": LearningSkill(self),
            "perception": PerceptionSkill(self)
        }

    def develop_business_plan(self, plan_details):
        # Directly return the comprehensive business plan using the template
        return BusinessPlanTemplate(
            executive_summary=plan_details.get('executive_summary', '...'),
            company_description=plan_details.get('company_description', '...'),
            market_analysis=plan_details.get('market_analysis', {}),
            organization_management=plan_details.get('organization_management', '...'),
            service_product_line=plan_details.get('service_product_line', '...'),
            marketing_sales=plan_details.get('marketing_sales', '...'),
            funding_request=plan_details.get('funding_request', '...'),
            financial_projections=plan_details.get('financial_projections', {}),
            appendix=plan_details.get('appendix', '...')
        )

    def send_message(self, recipient, message):
        broker = Broker()
        broker.register_agent(recipient, self.location)
        broker.route_message(self, recipient, message)