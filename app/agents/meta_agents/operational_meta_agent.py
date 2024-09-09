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

class OperationalMetaAgent(MetaAgent):
    def __init__(self, agent_id: str, name: str, api_key: str, llm_service: Any, agent_communication_service: Any):
        super().__init__(
            agent_id=agent_id,
            name=name,
            api_key=api_key,
            llm_service=llm_service,
            agent_communication_service=agent_communication_service
        )
        self.agent_type = "operational_meta"
        self.knowledge_base = KnowledgeBase()
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key)
        self.llm_manager = LLMManager()
        self.ontology = Ontology()  # Initialize with your operational ontology
        self.ontology_reasoner = OntologyReasoner(self.llm_manager, self.ontology)
        self.agent_service = AgentService()
        self.goal_service = GoalService()
        self.plan_service = PlanService()

        self._init_beliefs()
        self._init_desires()
        self._init_goals()
        self._init_plans()

    def _init_beliefs(self):
        self.add_belief("Efficient operational management is crucial for MAS performance")
        self.add_belief("Proper task allocation improves overall system efficiency")

    def _init_desires(self):
        self.add_desire("Optimize operational efficiency of the MAS", priority=10)
        self.add_desire("Ensure smooth execution of tactical plans", priority=9)

    def _init_goals(self):
        self.add_goal("Interpret and execute tactical plans", priority=9)
        self.add_goal("Manage task assignments effectively", priority=8)
        self.add_goal("Monitor and report operational status", priority=8)

    def _init_plans(self):
        self.create_plan(
            self.goals[0].id,
            [
                "Analyze tactical plans",
                "Break down plans into operational tasks",
                "Assign tasks to agents",
                "Monitor task execution",
                "Handle exceptions"
            ]
        )

    async def reason(self):
        print("Starting reasoning process for operational management")
        
        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        updated_beliefs = await self.reasoning_engine.reason({"beliefs": current_beliefs})
        
        for belief in updated_beliefs.get("beliefs", []):
            self.add_belief(belief["content"])

        new_knowledge = await self.ontology_reasoner.infer_new_knowledge()
        
        for concept in new_knowledge.get("new_concepts", []):
            self.add_belief(f"New operational concept: {concept['name']} - {concept['description']}")
        
        for relationship in new_knowledge.get("new_relationships", []):
            self.add_belief(f"New operational relationship: {relationship['name']} between {relationship['domain']} and {relationship['range']}")

        operational_query = "What are the key factors for efficient operational management in this MAS?"
        operational_factors = await self.ontology_reasoner.answer_query(operational_query)
        self.add_belief(f"Key operational factors: {operational_factors}")

        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        new_desires = await self.reasoning_engine.generate_desires(current_beliefs)
        
        for desire in new_desires:
            self.add_desire(desire["description"], desire["priority"])

        print("Reasoning process for operational management completed")

    async def plan(self):
        print("Starting planning process for operational management")
        for goal in self.goals:
            if goal.description == "Manage task assignments effectively":
                self.create_plan(
                    goal.id,
                    [
                        "Analyze agent capabilities",
                        "Match tasks to suitable agents",
                        "Distribute tasks",
                        "Monitor task progress",
                        "Reallocate tasks if necessary"
                    ]
                )
        
        current_state = self.get_current_state()
        optimized_plan = await self.reasoning_engine.reason_and_plan(self.goals[0].description, current_state)
        
        if optimized_plan.get("plan"):
            self.update_plan(self.goals[0].id, optimized_plan["plan"].steps)
        
        print("Planning process for operational management completed")

    async def execute(self):
        print("Starting execution process for operational management")
        for plan in self.plans:
            for task in plan.steps:
                if task.status == "pending":
                    print(f"Executing task: {task.description}")
                    try:
                        execution_result = await self.reasoning_engine.simulate_action(task.description, self.get_current_state())
                        self.update_task_status(task.id, "completed")
                        
                        for key, value in execution_result.items():
                            self.add_belief(f"Operational task result - {key}: {value}")
                    except Exception as e:
                        print(f"Error executing operational task {task.description}: {str(e)}")
                        self.update_task_status(task.id, "failed")
        print("Execution process for operational management completed")

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
            await asyncio.sleep(1)  # Adjust the sleep time as needed

    async def interpret_tactical_plans(self, tactical_plans: List[Plan]) -> List[Dict[str, Any]]:
        operational_tasks = []
        for plan in tactical_plans:
            for step in plan.steps:
                task = {
                    "description": step.description,
                    "plan_id": plan.id,
                    "status": "pending"
                }
                operational_tasks.append(task)
        return operational_tasks

    async def assign_tasks(self, operational_tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        task_assignments = {}
        available_agents = await self.agent_service.get_available_agents()
        
        for task in operational_tasks:
            suitable_agent = await self.agent_service.find_suitable_agent(task, available_agents)
            if suitable_agent:
                if suitable_agent.id not in task_assignments:
                    task_assignments[suitable_agent.id] = []
                task_assignments[suitable_agent.id].append(task)
                available_agents.remove(suitable_agent)
            else:
                # Handle case when no suitable agent is found
                task_assignments["unassigned"] = task_assignments.get("unassigned", []) + [task]
        
        return task_assignments

    async def monitor_task_execution(self, task_assignments: Dict[str, Any]) -> Dict[str, Any]:
        execution_status = {}
        for agent_id, tasks in task_assignments.items():
            if agent_id != "unassigned":
                agent_status = await self.agent_service.get_agent_status(agent_id)
                for task in tasks:
                    task_status = await self.agent_service.get_task_status(agent_id, task)
                    execution_status[task["description"]] = {
                        "agent_id": agent_id,
                        "agent_status": agent_status,
                        "task_status": task_status
                    }
        return execution_status

    async def handle_exceptions(self, execution_status: Dict[str, Any]) -> Dict[str, Any]:
        exception_handling = {}
        for task, status in execution_status.items():
            if status["task_status"] == "failed" or status["agent_status"] == "offline":
                alternative_agent = await self.agent_service.find_alternative_agent(status["agent_id"])
                exception_handling[task] = {
                    "original_agent": status["agent_id"],
                    "action": "reassign",
                    "new_agent": alternative_agent.id if alternative_agent else None
                }
        return exception_handling

    async def report_operational_status(self) -> Dict[str, Any]:
        return {
            "total_tasks": await self.plan_service.get_total_tasks(),
            "completed_tasks": await self.plan_service.get_completed_tasks(),
            "in_progress_tasks": await self.plan_service.get_in_progress_tasks(),
            "failed_tasks": await self.plan_service.get_failed_tasks(),
            "agent_utilization": await self.agent_service.get_agent_utilization(),
            "overall_progress": await self.plan_service.get_overall_progress(),
            "estimated_completion_time": await self.plan_service.get_estimated_completion_time()
        }
