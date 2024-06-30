import os
from dotenv import load_dotenv
import uuid
from typing import List, Dict
from app.models.plan import Plan
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService

# Load environment variables
load_dotenv()

class PlanService:
    def __init__(self, agent_service: AgentService, goal_service: GoalService):
        self.plans: Dict[str, Plan] = {}
        ##self.planner = Planner()
        self.agent_service = agent_service
        self.goal_service = goal_service

    def create_plan(self, goal_id: str) -> Plan:
        goal = self.goal_service.get_goal(goal_id)
        if not goal:
            return None

        plan_id = str(uuid.uuid4())
        new_plan = Plan(
            id=plan_id,
            goal_id=goal_id,
            steps=[],
            symbolic_plan={},
            llm_plan={}
        )
        
        context = self._get_planning_context()
        generated_plan = self.hybrid_planner.generate_plan(goal, context)
        new_plan.steps = generated_plan['steps']
        new_plan.symbolic_plan = generated_plan['symbolic_plan']
        new_plan.llm_plan = generated_plan['llm_plan']

        self.plans[plan_id] = new_plan
        return new_plan

    def get_plan(self, plan_id: str) -> Plan:
        return self.plans.get(plan_id)

    def list_plans(self) -> List[Plan]:
        return list(self.plans.values())

    def execute_plan(self, plan_id: str, agent_id: str) -> Dict:
        plan = self.plans.get(plan_id)
        agent = self.agent_service.get_agent(agent_id)
        if not plan or not agent:
            return None

        for step in plan.steps:
            # Execute each step
            # This is a placeholder and should be implemented based on your specific requirements
            pass

        # Update goal status
        self.goal_service.update_goal_status(plan.goal_id, is_achieved=True)

        return {"status": "Plan executed successfully"}

    def _get_planning_context(self) -> Dict:
        # Gather context for planning
        # This is a placeholder and should be implemented based on your specific requirements
        return {}