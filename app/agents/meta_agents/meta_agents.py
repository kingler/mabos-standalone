from typing import Any, Dict, List
from app.models.agent.agent import Agent
from app.models.agent.belief import Belief
from app.models.agent.desire import Desire
from app.models.agent.goal import Goal
from app.models.agent.plan import Plan
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.ontology_reasoner import OntologyReasoner
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.llm_manager import LLMManager
from app.models.knowledge.ontology.ontology import Ontology
import asyncio

class MetaAgent(Agent):
    def __init__(self, agent_id: str, name: str, api_key: str, llm_service: Any, agent_communication_service: Any):
        super().__init__(agent_id, name)
        self.api_key = api_key
        self.llm_service = llm_service
        self.agent_communication_service = agent_communication_service
        self.knowledge_base = KnowledgeBase()
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key)
        self.llm_manager = LLMManager()
        self.ontology = Ontology()
        self.ontology_reasoner = OntologyReasoner(self.llm_manager, self.ontology)

    async def reason(self):
        raise NotImplementedError("Subclasses must implement the reason method")

    async def plan(self):
        raise NotImplementedError("Subclasses must implement the plan method")

    async def execute(self):
        raise NotImplementedError("Subclasses must implement the execute method")

    async def run(self):
        while True:
            await self.reason()
            await self.plan()
            await self.execute()
            await asyncio.sleep(1)  # Adjust sleep time as needed

    def get_current_state(self) -> Dict[str, Any]:
        return {
            "beliefs": [belief.to_dict() for belief in self.beliefs],
            "desires": [desire.to_dict() for desire in self.desires],
            "goals": [goal.to_dict() for goal in self.goals],
            "plans": [plan.to_dict() for plan in self.plans],
        }

    def add_belief(self, content: str):
        self.beliefs.append(Belief(content=content))

    def add_desire(self, description: str, priority: int):
        self.desires.append(Desire(description=description, priority=priority))

    def add_goal(self, description: str, priority: int):
        self.goals.append(Goal(description=description, priority=priority))

    def create_plan(self, goal_id: str, steps: List[str]):
        plan = Plan(goal_id=goal_id)
        for step in steps:
            plan.add_step(step)
        self.plans.append(plan)

    def update_plan(self, goal_id: str, new_steps: List[str]):
        for plan in self.plans:
            if plan.goal_id == goal_id:
                plan.steps = []
                for step in new_steps:
                    plan.add_step(step)
                break

    def update_task_status(self, task_id: str, status: str):
        for plan in self.plans:
            for step in plan.steps:
                if step.id == task_id:
                    step.status = status
                    break