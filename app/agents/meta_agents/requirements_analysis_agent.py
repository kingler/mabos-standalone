from typing import Any, Dict, List

from app.agents.meta_agents.meta_agents import MetaAgent
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.ontology_reasoner import OntologyReasoner
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.llm_manager import LLMManager
from app.models.knowledge.ontology.ontology import Ontology
from pydantic import BaseModel


class RequirementsAnalysisAgent(MetaAgent):
    agent_id: str
    name: str
    api_key: str
    llm_service: str
    agent_communication_service: str
    reasoning_engine: ReasoningEngine
    ontology_reasoner: OntologyReasoner

    def __init__(self, agent_id, name, api_key, llm_service, agent_communication_service):
        super().__init__(
            agent_id=agent_id,
            name=name,
            api_key=api_key,
            llm_service=llm_service,
            agent_communication_service=agent_communication_service
        )
        self.agent_type = "requirements_analysis"
        self.knowledge_base = KnowledgeBase()
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key)
        self.llm_manager = LLMManager()
        self.ontology = Ontology()  # Initialize with your business ontology
        self.ontology_reasoner = OntologyReasoner(self.llm_manager, self.ontology)
        
        self._init_beliefs()
        self._init_desires()
        self._init_goals()
        self._init_plans()

    def _init_beliefs(self):
        self.add_belief("Requirements gathering is crucial for project success")
        self.add_belief("Stakeholder input is essential for accurate requirements")

    def _init_desires(self):
        self.add_desire("Ensure comprehensive requirements gathering", priority=10)
        self.add_desire("Maintain clear communication with stakeholders", priority=9)

    def _init_goals(self):
        self.add_goal("Gather and validate requirements", priority=9)
        self.add_goal("Create detailed use cases", priority=8)

    def _init_plans(self):
        self.create_plan(
            self.goals[0].id,
            [
                "Identify stakeholders",
                "Conduct stakeholder interviews",
                "Analyze existing documentation",
                "Draft initial requirements",
                "Review requirements with stakeholders",
                "Finalize requirements document"
            ]
        )

    async def reason(self):
        print("Starting reasoning process")
        
        # Use the reasoning engine to update beliefs based on current knowledge
        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        updated_beliefs = await self.reasoning_engine.reason({"beliefs": current_beliefs})
        
        # Update agent's beliefs
        for belief in updated_beliefs.get("beliefs", []):
            self.add_belief(belief["content"])

        # Use the ontology reasoner to infer new knowledge
        new_knowledge = await self.ontology_reasoner.infer_new_knowledge()
        
        # Process new concepts and relationships
        for concept in new_knowledge.get("new_concepts", []):
            self.add_belief(f"New concept identified: {concept['name']} - {concept['description']}")
        
        for relationship in new_knowledge.get("new_relationships", []):
            self.add_belief(f"New relationship identified: {relationship['name']} between {relationship['domain']} and {relationship['range']}")

        # Check for specific conditions and update goals
        if any(belief.content == "Stakeholder feedback received" for belief in self.beliefs):
            self.add_goal("Revise requirements based on feedback", priority=8)

        # Use the ontology reasoner to answer specific queries
        project_scope_query = "What is the current scope of the project based on the requirements gathered?"
        scope_answer = await self.ontology_reasoner.answer_query(project_scope_query)
        self.add_belief(f"Project scope analysis: {scope_answer}")

        stakeholder_query = "Who are the key stakeholders for this project?"
        stakeholders_answer = await self.ontology_reasoner.answer_query(stakeholder_query)
        self.add_belief(f"Key stakeholders identified: {stakeholders_answer}")

        # Generate new desires based on updated beliefs
        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        new_desires = await self.reasoning_engine.generate_desires(current_beliefs)
        
        for desire in new_desires:
            self.add_desire(desire["description"], desire["priority"])

        print("Reasoning process completed")

    async def plan(self):
        print("Starting planning process")
        for goal in self.goals:
            if goal.description == "Revise requirements based on feedback":
                self.create_plan(
                    goal.id,
                    [
                        "Review stakeholder feedback",
                        "Identify areas for revision",
                        "Update requirements document",
                        "Validate changes with stakeholders"
                    ]
                )
        
        # Use the reasoning engine to optimize the plan
        current_state = self.get_current_state()
        optimized_plan = await self.reasoning_engine.reason_and_plan(self.goals[0].description, current_state)
        
        if optimized_plan.get("plan"):
            self.update_plan(self.goals[0].id, optimized_plan["plan"].steps)
        
        print("Planning process completed")

    async def execute(self):
        print("Starting execution process")
        for plan in self.plans:
            for task in plan.steps:
                if task.status == "pending":
                    print(f"Executing task: {task.description}")
                    try:
                        # Use the reasoning engine to simulate task execution
                        execution_result = await self.reasoning_engine.simulate_action(task.description, self.get_current_state())
                        self.update_task_status(task.id, "completed")
                        
                        # Update beliefs based on execution result
                        for key, value in execution_result.items():
                            self.add_belief(f"Task result - {key}: {value}")
                    except Exception as e:
                        print(f"Error executing task {task.description}: {str(e)}")
                        self.update_task_status(task.id, "failed")
        print("Execution process completed")

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
