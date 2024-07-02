import os
from uuid import UUID
import uuid
from dotenv import load_dotenv
from typing import List, Optional, Dict, Any
from app.models import agent
from app.models.agent import Agent, Belief, Desire, Intention
from app.core.reasoner import Reasoner
from app.models.knowledge_base import KnowledgeBase, KnowledgeItem

# Load environment variables
load_dotenv()

class AgentService:
    def __init__(self):
        self.agents: dict[str, Agent] = {}
        self.knowledge_base = KnowledgeBase(id=str(uuid.uuid4()))
        api_key = os.getenv('OPENAI_API_KEY')  # Get API key from environment variable
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.reasoner = Reasoner(self.knowledge_base, api_key)

    def create_agent(self, name: str) -> Agent:
        agent_id = str(uuid.UUID())
        new_agent = Agent(id=agent_id, name=name)
        self.agents[agent_id] = new_agent
        return new_agent

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        self.agents[agent.id] = agent
        return self.agents.get(agent_id)

    def list_agents(self) -> List[Agent]:
        return list(self.agents.values())
    
    def update_agent(self, agent_id: UUID, update_data: Dict[str, Any]) -> Agent:
        if agent := self.agents.get(agent_id):
            for key, value in update_data.items():
                setattr(agent, key, value)
            return agent
        return None
    
    def delete_agent(self, agent_id: UUID) -> bool:
        if agent_id in self.agents:
            del self.agents[agent_id]
            return True
        return False
    
    def get_all_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def get_agents_by_type(self, agent_type: str) -> List[Agent]:
        return [agent for agent in self.agents.values() if agent.type == agent_type]
    

    def add_belief(self, agent_id: str, belief: Belief) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent.add_belief(belief)
            self._update_desires(agent)
        return agent
    
    def update_agent_beliefs(self, agent_id: UUID, new_beliefs: Dict[str, Any]) -> Agent:
        if agent := self.agents.get(agent_id):
            agent.beliefs.update(new_beliefs)
            return agent
        return None   

    def add_agent_desire(self, agent_id: UUID, desire: str) -> Agent:
        if agent := self.agents.get(agent_id):
            agent.desires.append(desire)
            return agent
        return None

    def add_agent_intention(self, agent_id: UUID, intention: str) -> Agent:
        if agent := self.agents.get(agent_id):
            agent.intentions.append(intention)
            return agent
        return None

    def update_resource(self, agent_id: str, resource_name: str, value: float) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent.update_resource(resource_name, value)
        return agent

    def _update_desires(self, agent: Agent):

        new_desires = self.reasoner.generate_desires(agent.beliefs)
        for desire in new_desires:
            agent.add_desire(desire)

    def _update_intentions(self, agent: Agent):

        new_intentions = self.reasoner.select_intentions(agent.desires, agent.beliefs, agent.resources)
        agent.intentions = new_intentions

    def reason_and_plan(self, agent_id: str) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            self._update_desires(agent)
            self._update_intentions(agent)
            for intention in agent.intentions:
                if plan := self.plan_service.generate_plan(intention, agent.beliefs):
                    agent.plans.append(plan)
                else:
                    agent.intentions.remove(intention)
        return agent

    def perceive_environment(self, agent_id: str, percepts: List[dict]) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            for percept in percepts:
                belief = Belief(id=str(uuid.UUID()), content=percept)
                agent.add_belief(belief)
            self.reason_and_plan(agent_id)
        return agent

    def execute_action(self, agent_id: str, action: str) -> Optional[dict]:
        agent = self.agents.get(agent_id)
        if not agent:
            return None

        action_obj = self.action_service.get_action(action)
        if not action_obj:
            return {"status": "error", "message": f"Unknown action: {action}"}

        if any(capability not in agent.capabilities for capability in action_obj.required_capabilities):
            return {"status": "error", "message": f"Agent {agent_id} lacks required capabilities for action: {action}"}

        effects = action_obj.execute(agent, self.environment)
        
        for effect in effects:
            if effect["type"] == "belief":
                agent.update_belief(effect["belief"])
            elif effect["type"] == "resource":
                agent.update_resource(effect["resource"], effect["value"])

        self.reason_and_plan(agent_id)
        return {"status": "success", "action": action, "effects": effects}

    def add_symbolic_knowledge(self, knowledge_item: KnowledgeItem):
        self.reasoner.knowledge_base.add_symbolic_knowledge(knowledge_item)

    def add_neural_knowledge(self, knowledge_item: KnowledgeItem):
        self.reasoner.knowledge_base.add_neural_knowledge(knowledge_item)

    def query_knowledge_base(self, query: str) -> Dict[str, Any]:
        return self.reasoner.knowledge_base.query(query)