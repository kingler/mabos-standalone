import uuid
from typing import Any, Dict, List, Optional
from uuid import UUID

from app.models.agent import Agent, Belief, Intention
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.reasoner import Reasoner
from app.services.planning_service import PlanningService
from app.tools.llm_manager import LLMManager


class AgentService:
    def __init__(self, world_model, llm_manager: LLMManager):
        self.id = str(uuid.uuid4())
        self.agents: Dict[str, Agent] = {}
        self.knowledge_base = KnowledgeBase(id=str(uuid.uuid4()))
        self.planning_service = PlanningService(KnowledgeBase)
        self.llm_manager = llm_manager
        self.reasoner = Reasoner(self.knowledge_base, api_key=self.llm_manager.api_keys['openai'])
        self.world_model = world_model

    def create_agent(self, name: str) -> Agent:
        agent_id = str(uuid.uuid4())
        new_agent = Agent(id=agent_id, name=name)
        self.agents[agent_id] = new_agent
        self.world_model.add_agent(UUID(agent_id), new_agent.dict())
        return new_agent

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        return self.agents.get(agent_id)

    def update_agent(self, agent_id: UUID, update_data: Dict[str, Any]) -> Agent:
        if agent := self.agents.get(str(agent_id)):
            for key, value in update_data.items():
                setattr(agent, key, value)
            self.world_model.update_agent(agent_id, update_data)
            return agent
        return None

    def perceive_environment(self, agent_id: str) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent_view = self.world_model.get_agent_view(UUID(agent_id))
            percepts = self._extract_percepts(agent_view)
            for percept in percepts:
                belief = Belief(id=str(uuid.UUID()), content=percept)
                agent.add_belief(belief)
            self.reason_and_plan(agent_id)
        return agent

    def _extract_percepts(self, agent_view: Dict[str, Any]) -> List[Dict[str, Any]]:
        percepts = []
        percepts.append({"type": "state", "content": agent_view["state"]})
        percepts.append({"type": "self", "content": agent_view["agent"]})
        for obj_id, obj_data in agent_view["visible_objects"].items():
            percepts.append({"type": "object", "id": obj_id, "content": obj_data})
        for relationship in agent_view["relationships"]:
            percepts.append({"type": "relationship", "content": relationship})
        
        # Add ontology-based percepts
        for ontology_info in agent_view["ontology_info"]:
            percepts.append({"type": "ontology", "content": ontology_info})
        
        return percepts

    def execute_action(self, agent_id: str, action: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        agent = self.agents.get(agent_id)
        if not agent:
            return None

        # Execute the action and update the world model
        if action["type"] == "move":
            self.world_model.update_agent(UUID(agent_id), {"position": action["target"]})
        elif action["type"] == "interact":
            # Handle interaction with objects or other agents
            pass
        elif action["type"] == "query_ontology":
            # Allow agents to query the ontology directly
            query_result = self.world_model.query_world_knowledge(action["query"])
            return {"status": "success", "action": action, "result": query_result}

        # Update the agent's beliefs based on the action's effects
        self.perceive_environment(agent_id)

        return {"status": "success", "action": action}

    def reason_and_plan(self, agent_id: str) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            # Use the reasoner to update desires and intentions based on new beliefs
            new_desires = self.reasoner.generate_desires(agent.beliefs)
            for desire in new_desires:
                agent.add_desire(desire)
            
            new_intentions = self.reasoner.select_intentions(agent.desires, agent.beliefs, agent.resources)
            agent.intentions = new_intentions
            
            # Generate plans for new intentions
            for intention in new_intentions:
                if plan := self.generate_plan(intention, agent.beliefs):
                    agent.plans.append(plan)
                else:
                    agent.intentions.remove(intention)
        return agent

    def generate_plan(self, intention: Intention, beliefs: List[Belief]) -> Optional[Dict[str, Any]]:
        # Implement planning logic here
        # This could involve querying the ontology for action possibilities
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
        
        # Process the query results to create a plan
        plan = {
            "intention_id": intention.id,
            "steps": [{"action": step[0], "precondition": step[1], "effect": step[2]} for step in plan_steps]
        }
        return plan if plan["steps"] else None