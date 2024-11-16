"""
Unified Agent Service
Combines functionality from agent_service.py, mas_services.py, and mdd_mas_services.py
"""
import json
import uuid
from typing import Any, Dict, List, Optional
from uuid import UUID

from app.models.agent import Agent, Belief, Intention
from app.models.consistency_checker import ConsistencyChecker
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.knowledge.active_knowledge_acquisition import ActiveKnowledgeAcquisition
from app.models.knowledge.conflict_resolution import ConflictResolution
from app.models.knowledge.distributed_knowledge import DistributedKnowledge
from app.models.knowledge.explanation_generator import ExplanationGenerator
from app.models.knowledge.ontology.ontology import Ontology
from app.models.knowledge.reasoning.temporal_reasoning import TemporalReasoning
from app.models.system.multiagent_system import MultiAgentSystem
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.llm_manager import LLMManager
from app.db.db_integration import DatabaseIntegration


class UnifiedAgentService:
    """
    Unified service for managing agents within the Multi-Agent System.
    Combines functionality from multiple agent services into a single, cohesive interface.
    """
    def __init__(self, world_model, llm_manager: LLMManager, ontology_path: str):
        # Core components
        self.id = str(uuid.uuid4())
        self.agents: Dict[str, Agent] = {}
        self.world_model = world_model
        self.llm_manager = llm_manager
        
        # Knowledge and reasoning components
        self.knowledge_base = KnowledgeBase(id=str(uuid.uuid4()))
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key=self.llm_manager.api_keys['openai'])
        
        # MAS components
        self.consistency_checker = ConsistencyChecker(self.knowledge_base, Ontology)
        self.temporal_reasoning = TemporalReasoning(self.knowledge_base)
        self.distributed_knowledge = DistributedKnowledge(DatabaseIntegration)
        self.active_knowledge_acquisition = ActiveKnowledgeAcquisition(self.knowledge_base, Ontology)
        self.conflict_resolution = ConflictResolution(self.knowledge_base)
        self.explanation_generator = ExplanationGenerator(self.knowledge_base, self.reasoning_engine)

    async def create_agent(self, name: str, agent_type: str = None, beliefs: Dict[str, Any] = None) -> Agent:
        """Create a new agent with specified characteristics."""
        agent_id = str(uuid.uuid4())
        new_agent = Agent(
            id=agent_id,
            name=name,
            type=agent_type,
            beliefs=beliefs or {}
        )
        
        # Store agent in memory
        self.agents[agent_id] = new_agent
        
        # Update world model
        self.world_model.add_agent(UUID(agent_id), new_agent.dict())
        
        # Initialize agent's knowledge base
        agent_kb = KnowledgeBase(agent_id=agent_id)
        for belief, value in new_agent.beliefs.items():
            agent_kb.add_belief(belief, value)
        
        # Store agent in database
        db = DatabaseIntegration()
        query = """
        INSERT INTO agents (id, name, type, beliefs)
        VALUES (:id, :name, :type, :beliefs)
        """
        params = {
            "id": agent_id,
            "name": name,
            "type": agent_type,
            "beliefs": json.dumps(beliefs or {})
        }
        await db.execute_sql_query(query, params)
        
        return new_agent

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        """Retrieve an agent by ID."""
        return self.agents.get(agent_id)

    def list_agents(self) -> List[Agent]:
        """List all agents in the system."""
        return list(self.agents.values())

    async def update_agent(self, agent_id: UUID, update_data: Dict[str, Any]) -> Optional[Agent]:
        """Update an agent's attributes."""
        if agent := self.agents.get(str(agent_id)):
            for key, value in update_data.items():
                setattr(agent, key, value)
            
            # Update world model
            self.world_model.update_agent(agent_id, update_data)
            
            # Update database
            await self._update_agent_in_db(agent)
            
            return agent
        return None

    async def remove_agent(self, agent_id: UUID) -> bool:
        """Remove an agent from the system."""
        if str(agent_id) in self.agents:
            del self.agents[str(agent_id)]
            # Remove from database
            db = DatabaseIntegration()
            query = "DELETE FROM agents WHERE id = :id"
            await db.execute_sql_query(query, {"id": str(agent_id)})
            return True
        return False

    def perceive_environment(self, agent_id: str) -> Optional[Agent]:
        """Update agent's beliefs based on environment perception."""
        agent = self.agents.get(agent_id)
        if agent:
            agent_view = self.world_model.get_agent_view(UUID(agent_id))
            percepts = self._extract_percepts(agent_view)
            for percept in percepts:
                belief = Belief(id=str(uuid.uuid4()), content=percept)
                agent.add_belief(belief)
            self.reason_and_plan(agent_id)
        return agent

    def _extract_percepts(self, agent_view: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract percepts from agent's view of the environment."""
        percepts = []
        percepts.append({"type": "state", "content": agent_view["state"]})
        percepts.append({"type": "self", "content": agent_view["agent"]})
        
        for obj_id, obj_data in agent_view["visible_objects"].items():
            percepts.append({"type": "object", "id": obj_id, "content": obj_data})
        
        for relationship in agent_view["relationships"]:
            percepts.append({"type": "relationship", "content": relationship})
        
        for ontology_info in agent_view["ontology_info"]:
            percepts.append({"type": "ontology", "content": ontology_info})
        
        return percepts

    async def execute_action(self, agent_id: str, action: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Execute an action on behalf of an agent."""
        agent = self.agents.get(agent_id)
        if not agent:
            return None

        # Execute action and update world model
        if action["type"] == "move":
            self.world_model.update_agent(UUID(agent_id), {"position": action["target"]})
        elif action["type"] == "interact":
            # Handle interaction with objects or other agents
            pass
        elif action["type"] == "query_ontology":
            query_result = self.world_model.query_world_knowledge(action["query"])
            return {"status": "success", "action": action, "result": query_result}

        # Update agent's beliefs based on action effects
        self.perceive_environment(agent_id)

        return {"status": "success", "action": action}

    def reason_and_plan(self, agent_id: str) -> Optional[Agent]:
        """Perform reasoning and planning for an agent."""
        agent = self.agents.get(agent_id)
        if agent:
            # Generate new desires based on beliefs
            new_desires = self.reasoning_engine.generate_desires(agent.beliefs)
            for desire in new_desires:
                agent.add_desire(desire)
            
            # Select intentions based on desires and beliefs
            new_intentions = self.reasoning_engine.select_intentions(
                agent.desires,
                agent.beliefs,
                agent.resources
            )
            agent.intentions = new_intentions
            
            # Generate plans for new intentions
            for intention in new_intentions:
                if plan := self.generate_plan(intention, agent.beliefs):
                    agent.plans.append(plan)
                else:
                    agent.intentions.remove(intention)
        return agent

    def generate_plan(self, intention: Intention, beliefs: List[Belief]) -> Optional[Dict[str, Any]]:
        """Generate a plan to achieve an intention."""
        plan_query = f"""
        SELECT ?action ?precondition ?effect
        WHERE {{
            ?action rdf:type :Action .
            ?action :hasPrecondition ?precondition .
            ?action :hasEffect ?effect .
            ?effect :achieves "{intention.goal_id}" .
        }}
        """
        plan_steps = self.world_model.query_world_knowledge(plan_query)
        
        plan = {
            "intention_id": intention.id,
            "steps": [
                {
                    "action": step[0],
                    "precondition": step[1],
                    "effect": step[2]
                }
                for step in plan_steps
            ]
        }
        return plan if plan["steps"] else None

    async def _update_agent_in_db(self, agent: Agent):
        """Update agent information in the database."""
        db = DatabaseIntegration()
        query = """
        UPDATE agents
        SET name = :name,
            type = :type,
            beliefs = :beliefs,
            goals = :goals,
            intentions = :intentions
        WHERE id = :id
        """
        params = {
            "id": str(agent.id),
            "name": agent.name,
            "type": agent.type,
            "beliefs": json.dumps(agent.beliefs),
            "goals": json.dumps(agent.goals),
            "intentions": json.dumps([i.dict() for i in agent.intentions])
        }
        await db.execute_sql_query(query, params)

    def step(self):
        """Execute one step of the multi-agent system."""
        for agent in self.agents.values():
            self.perceive_environment(str(agent.id))
            self.reason_and_plan(str(agent.id))
            # Execute any pending actions
            if agent.current_plan:
                next_action = agent.current_plan.get_next_action()
                if next_action:
                    self.execute_action(str(agent.id), next_action)

    def run(self, steps: int):
        """Run the multi-agent system for a specified number of steps."""
        for _ in range(steps):
            self.step()
