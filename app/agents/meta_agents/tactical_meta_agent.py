from typing import Any, Dict, List
from app.models.agent.agent import Agent
from app.models.agent.goal import Goal
from app.models.agent.plan import Plan
from app.services.agent_service import AgentService
from app.services.goal_service import GoalService
from app.services.plan_service import PlanService
from app.agents.meta_agents.meta_agents import MetaAgent
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.ontology_reasoner import OntologyReasoner
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.llm_manager import LLMManager
from app.models.knowledge.ontology.ontology import Ontology
import asyncio

class TacticalMetaAgent(MetaAgent):
    def __init__(self, agent_id: str, name: str, api_key: str, llm_service: Any, agent_communication_service: Any):
        super().__init__(
            agent_id=agent_id,
            name=name,
            api_key=api_key,
            llm_service=llm_service,
            agent_communication_service=agent_communication_service
        )
        self.agent_type = "tactical_meta"
        self.knowledge_base = KnowledgeBase()
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key)
        self.llm_manager = LLMManager()
        self.ontology = Ontology()  # Initialize with your tactical ontology
        self.ontology_reasoner = OntologyReasoner(self.llm_manager, self.ontology)
        self.agent_service = AgentService()
        self.goal_service = GoalService()
        self.plan_service = PlanService()

        self._init_beliefs()
        self._init_desires()
        self._init_goals()
        self._init_plans()

    def _init_beliefs(self):
        self.add_belief("Effective tactical planning is crucial for achieving strategic goals")
        self.add_belief("Adaptability in tactical execution leads to better overall performance")

    def _init_desires(self):
        self.add_desire("Develop and execute effective tactical plans", priority=10)
        self.add_desire("Ensure alignment between tactical actions and strategic goals", priority=9)

    def _init_goals(self):
        self.add_goal("Decompose strategic goals into tactical objectives", priority=9)
        self.add_goal("Generate detailed tactical plans", priority=8)
        self.add_goal("Coordinate agent actions for plan execution", priority=8)
        self.add_goal("Monitor and adjust tactical plans", priority=7)

    def _init_plans(self):
        self.create_plan(
            self.goals[0].id,
            [
                "Analyze strategic goals",
                "Identify key tactical objectives",
                "Prioritize tactical objectives",
                "Develop action plans for each objective"
            ]
        )

    async def reason(self):
        print("Starting reasoning process for tactical planning")
        
        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        updated_beliefs = await self.reasoning_engine.reason({"beliefs": current_beliefs})
        
        for belief in updated_beliefs.get("beliefs", []):
            self.add_belief(belief["content"])

        new_knowledge = await self.ontology_reasoner.infer_new_knowledge()
        
        for concept in new_knowledge.get("new_concepts", []):
            self.add_belief(f"New tactical concept: {concept['name']} - {concept['description']}")
        
        for relationship in new_knowledge.get("new_relationships", []):
            self.add_belief(f"New tactical relationship: {relationship['name']} between {relationship['domain']} and {relationship['range']}")

        tactical_query = "What are the key considerations for effective tactical planning in this MAS?"
        tactical_considerations = await self.ontology_reasoner.answer_query(tactical_query)
        self.add_belief(f"Key tactical considerations: {tactical_considerations}")

        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        new_desires = await self.reasoning_engine.generate_desires(current_beliefs)
        
        for desire in new_desires:
            self.add_desire(desire["description"], desire["priority"])

        print("Reasoning process for tactical planning completed")

    async def plan(self):
        print("Starting planning process for tactical management")
        for goal in self.goals:
            if goal.description == "Generate detailed tactical plans":
                self.create_plan(
                    goal.id,
                    [
                        "Analyze tactical objectives",
                        "Identify required resources",
                        "Develop step-by-step action plans",
                        "Assign responsibilities to agents",
                        "Set milestones and deadlines"
                    ]
                )
        
        current_state = self.get_current_state()
        optimized_plan = await self.reasoning_engine.reason_and_plan(self.goals[0].description, current_state)
        
        if optimized_plan.get("plan"):
            self.update_plan(self.goals[0].id, optimized_plan["plan"].steps)
        
        print("Planning process for tactical management completed")

    async def execute(self):
        print("Starting execution process for tactical management")
        for plan in self.plans:
            for task in plan.steps:
                if task.status == "pending":
                    print(f"Executing task: {task.description}")
                    try:
                        execution_result = await self.reasoning_engine.simulate_action(task.description, self.get_current_state())
                        self.update_task_status(task.id, "completed")
                        
                        for key, value in execution_result.items():
                            self.add_belief(f"Tactical task result - {key}: {value}")
                    except Exception as e:
                        print(f"Error executing tactical task {task.description}: {str(e)}")
                        self.update_task_status(task.id, "failed")
        print("Execution process for tactical management completed")

    def get_current_state(self) -> Dict[str, Any]:
        return {
            "beliefs": [belief.to_dict() for belief in self.beliefs],
            "desires": [desire.to_dict() for desire in self.desires],
            "goals": [goal.to_dict() for goal in self.goals],
            "plans": [plan.to_dict() for plan in self.plans],
        }

    async def run(self):
        while True:
            await self.reason()
            await self.plan()
            await self.execute()
            await asyncio.sleep(300)  # Sleep for 5 minutes, adjust as needed for tactical planning frequency

    async def decompose_strategic_goals(self, strategic_goals: List[Goal]) -> List[Goal]:
        tactical_goals = []
        for strategic_goal in strategic_goals:
            sub_goals = await self.goal_service.break_down_goal(strategic_goal)
            tactical_goals.extend(sub_goals)
        
        # Use the reasoning engine to refine and prioritize tactical goals
        refined_tactical_goals = await self.reasoning_engine.reason_about_goals(tactical_goals)
        
        return refined_tactical_goals

    async def generate_tactical_plans(self, tactical_goals: List[Goal]) -> List[Plan]:
        tactical_plans = []
        for goal in tactical_goals:
            plan = await self.plan_service.create_plan(goal)
            tactical_plans.append(plan)
        
        # Use the reasoning engine to optimize tactical plans
        optimized_plans = await self.reasoning_engine.optimize_plans(tactical_plans)
        
        return optimized_plans

    async def coordinate_agents(self, tactical_plans: List[Plan]) -> Dict[str, Any]:
        coordination_results = {}
        for plan in tactical_plans:
            assigned_agents = await self.agent_service.assign_agents_to_plan(plan)
            for agent in assigned_agents:
                await self.agent_communication_service.send_plan(agent.id, plan)
            coordination_results[plan.id] = {"assigned_agents": assigned_agents}
        
        # Use the reasoning engine to optimize agent coordination
        optimized_coordination = await self.reasoning_engine.optimize_agent_coordination(coordination_results)
        
        return optimized_coordination

    async def monitor_tactical_execution(self, tactical_plans: List[Plan]) -> Dict[str, Any]:
        execution_status = {}
        for plan in tactical_plans:
            progress = await self.plan_service.get_plan_progress(plan.id)
            execution_status[plan.id] = progress
        
        # Use the reasoning engine to analyze execution status and suggest adjustments
        analysis_and_suggestions = await self.reasoning_engine.analyze_tactical_execution(execution_status)
        
        return analysis_and_suggestions

    async def adjust_tactics(self, execution_status: Dict[str, Any]) -> List[Plan]:
        adjusted_plans = []
        for plan_id, status in execution_status.items():
            if status['progress'] < status['expected_progress']:
                original_plan = await self.plan_service.get_plan(plan_id)
                adjusted_plan = await self.reasoning_engine.adjust_tactical_plan(original_plan, status)
                adjusted_plans.append(adjusted_plan)
            else:
                original_plan = await self.plan_service.get_plan(plan_id)
                adjusted_plans.append(original_plan)
        
        return adjusted_plans
