from typing import Any, Dict, List
from pydantic import BaseModel
from app.agents.meta_agents.meta_agents import MetaAgent
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.ontology_reasoner import OntologyReasoner
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.llm_manager import LLMManager
from app.models.knowledge.ontology.ontology import Ontology
from openai import OpenAI

class AgentType(BaseModel):
    name: str
    description: str
    use_cases: List[str]

class AgentGBI(BaseModel):
    goals: List[str]
    beliefs: List[str]
    intentions: List[str]

class AgentBehavior(BaseModel):
    name: str
    description: str
    decision_process: str

class TroposModel(BaseModel):
    actor: str
    goals: List[str]
    dependencies: List[str]

class AgentDesignAgent(MetaAgent):
    """
    Specializes in designing individual agents for the domain-specific MAS.
    
    Key functions:
    - Define agent types (e.g., reactive, proactive, hybrid)
    - Specify agent goals, beliefs, and intentions
    - Design agent behaviors and decision-making processes
    - Implement Tropos-based agent modeling
    """
    def __init__(self, agent_id, name, api_key, llm_service, agent_communication_service):
        super().__init__(
            agent_id=agent_id,
            name=name,
            api_key=api_key,
            llm_service=llm_service,
            agent_communication_service=agent_communication_service
        )
        self.agent_type = "agent_design"
        self.knowledge_base = KnowledgeBase()
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key)
        self.llm_manager = LLMManager()
        self.ontology = Ontology()  # Initialize with your agent design ontology
        self.ontology_reasoner = OntologyReasoner(self.llm_manager, self.ontology)
        self.client = OpenAI()

        self._init_beliefs()
        self._init_desires()
        self._init_goals()
        self._init_plans()

    def _init_beliefs(self):
        self.add_belief("Agent design is crucial for MAS effectiveness")
        self.add_belief("Different agent types suit different problem domains")

    def _init_desires(self):
        self.add_desire("Design optimal agents for the MAS", priority=10)
        self.add_desire("Ensure agent designs align with system requirements", priority=9)

    def _init_goals(self):
        self.add_goal("Define appropriate agent types", priority=9)
        self.add_goal("Specify agent GBIs", priority=8)
        self.add_goal("Design agent behaviors", priority=8)
        self.add_goal("Create Tropos models", priority=7)

    def _init_plans(self):
        self.create_plan(
            self.goals[0].id,
            [
                "Analyze domain requirements",
                "Identify suitable agent types",
                "Define agent type characteristics"
            ]
        )

    async def reason(self):
        print("Starting reasoning process for agent design")
        
        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        updated_beliefs = await self.reasoning_engine.reason({"beliefs": current_beliefs})
        
        for belief in updated_beliefs.get("beliefs", []):
            self.add_belief(belief["content"])

        new_knowledge = await self.ontology_reasoner.infer_new_knowledge()
        
        for concept in new_knowledge.get("new_concepts", []):
            self.add_belief(f"New agent design concept: {concept['name']} - {concept['description']}")
        
        for relationship in new_knowledge.get("new_relationships", []):
            self.add_belief(f"New agent design relationship: {relationship['name']} between {relationship['domain']} and {relationship['range']}")

        agent_type_query = "What are the most suitable agent types for the current problem domain?"
        agent_types_answer = await self.ontology_reasoner.answer_query(agent_type_query)
        self.add_belief(f"Suitable agent types: {agent_types_answer}")

        current_beliefs = [belief.to_dict() for belief in self.beliefs]
        new_desires = await self.reasoning_engine.generate_desires(current_beliefs)
        
        for desire in new_desires:
            self.add_desire(desire["description"], desire["priority"])

        print("Reasoning process for agent design completed")

    async def plan(self):
        print("Starting planning process for agent design")
        current_state = self.get_current_state()
        optimized_plan = await self.reasoning_engine.reason_and_plan(self.goals[0].description, current_state)
        
        if optimized_plan.get("plan"):
            self.update_plan(self.goals[0].id, optimized_plan["plan"].steps)
        
        print("Planning process for agent design completed")

    async def execute(self):
        print("Starting execution process for agent design")
        for plan in self.plans:
            for task in plan.steps:
                if task.status == "pending":
                    print(f"Executing task: {task.description}")
                    try:
                        execution_result = await self.reasoning_engine.simulate_action(task.description, self.get_current_state())
                        self.update_task_status(task.id, "completed")
                        
                        for key, value in execution_result.items():
                            self.add_belief(f"Agent design task result - {key}: {value}")
                    except Exception as e:
                        print(f"Error executing agent design task {task.description}: {str(e)}")
                        self.update_task_status(task.id, "failed")
        print("Execution process for agent design completed")

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

    async def design_agents(self, domain_requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Design agents based on the domain requirements.

        Args:
            domain_requirements (Dict[str, Any]): The requirements of the domain-specific MAS.

        Returns:
            Dict[str, Any]: A dictionary containing the designed agent types, GBIs, behaviors, and Tropos models.
        """
        await self.reason()  # Update beliefs and goals based on domain requirements
        await self.plan()    # Create or update plans for agent design

        agent_types = await self._define_agent_types(domain_requirements)
        agent_gbis = await self._specify_agent_gbis(domain_requirements, agent_types)
        agent_behaviors = await self._design_agent_behaviors(agent_gbis)
        tropos_models = await self._implement_tropos_modeling(agent_types, agent_gbis, agent_behaviors)
        
        return {
            "agent_types": agent_types,
            "agent_gbis": agent_gbis,
            "agent_behaviors": agent_behaviors,
            "tropos_models": tropos_models
        }

    async def _define_agent_types(self, domain_requirements: Dict[str, Any]) -> List[AgentType]:
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are an AI expert specializing in multi-agent systems."},
                {"role": "user", "content": f"Based on these domain requirements: {domain_requirements}, suggest appropriate agent types for a multi-agent system."}
            ],
            response_format=List[AgentType]
        )
        return self._handle_completion(completion) or []

    async def _specify_agent_gbis(self, domain_requirements: Dict[str, Any], agent_types: List[AgentType]) -> Dict[str, AgentGBI]:
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are an AI expert specializing in multi-agent systems."},
                {"role": "user", "content": f"Based on these domain requirements: {domain_requirements} and agent types: {agent_types}, specify the goals, beliefs, and intentions for each agent type."}
            ],
            response_format=Dict[str, AgentGBI]
        )
        return self._handle_completion(completion) or {}

    async def _design_agent_behaviors(self, agent_gbis: Dict[str, AgentGBI]) -> Dict[str, List[AgentBehavior]]:
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are an AI expert specializing in multi-agent systems."},
                {"role": "user", "content": f"Based on these agent GBIs: {agent_gbis}, design appropriate behaviors and decision-making processes for each agent type."}
            ],
            response_format=Dict[str, List[AgentBehavior]]
        )
        return self._handle_completion(completion) or {}

    async def _implement_tropos_modeling(self, agent_types: List[AgentType], agent_gbis: Dict[str, AgentGBI], agent_behaviors: Dict[str, List[AgentBehavior]]) -> Dict[str, TroposModel]:
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are an AI expert specializing in multi-agent systems and Tropos modeling."},
                {"role": "user", "content": f"Based on these agent types: {agent_types}, GBIs: {agent_gbis}, and behaviors: {agent_behaviors}, create Tropos models for each agent type."}
            ],
            response_format=Dict[str, TroposModel]
        )
        return self._handle_completion(completion) or {}

    def _handle_completion(self, completion):
        if not hasattr(completion.choices[0].message, 'refusal'):
            return completion.choices[0].message.parsed
        
        print(completion.choices[0].message.refusal)
        return None
