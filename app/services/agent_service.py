import os
import uuid
from dotenv import load_dotenv
from typing import List, Optional, Dict, Any
from app.models import knowledge_base
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
        agent_id = str(uuid.uuid4())
        new_agent = Agent(id=agent_id, name=name)
        self.agents[agent_id] = new_agent
        return new_agent

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        return self.agents.get(agent_id)

    def list_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def add_belief(self, agent_id: str, belief: Belief) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent.add_belief(belief)
            self._update_desires(agent)
        return agent

    def add_desire(self, agent_id: str, desire: Desire) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent.add_desire(desire)
            self._update_intentions(agent)
        return agent

    def add_intention(self, agent_id: str, intention: Intention) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent.add_intention(intention)
        return agent

    def update_resource(self, agent_id: str, resource_name: str, value: float) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            agent.update_resource(resource_name, value)
        return agent

    def _update_desires(self, agent: Agent):
        # Use the hybrid reasoner to update desires based on new beliefs
        new_desires = self.reasoner.generate_desires(agent.beliefs)
        for desire in new_desires:
            agent.add_desire(desire)

    def _update_intentions(self, agent: Agent):
        # Use the hybrid reasoner to select intentions based on desires and current context
        new_intentions = self.reasoner.select_intentions(agent.desires, agent.beliefs, agent.resources)
        agent.intentions = new_intentions

    def reason_and_plan(self, agent_id: str) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            self._update_desires(agent)
            self._update_intentions(agent)
            # Here you might want to trigger plan generation for new intentions
            # This could involve interaction with a PlanService
        return agent

    def perceive_environment(self, agent_id: str, percepts: List[dict]) -> Optional[Agent]:
        agent = self.agents.get(agent_id)
        if agent:
            for percept in percepts:
                belief = Belief(id=str(uuid.uuid4()), content=percept)
                agent.add_belief(belief)
            self.reason_and_plan(agent_id)
        return agent

    def execute_action(self, agent_id: str, action: str) -> Optional[dict]:
        agent = self.agents.get(agent_id)
        if agent:
            # Here you would implement the logic for executing an action
            # This might involve updating the agent's state, interacting with the environment, etc.
            result = {"status": "success", "action": action, "effects": []}
            # After executing the action, you might want to update the agent's beliefs and re-plan
            self.reason_and_plan(agent_id)
            return result
        return None

    def add_symbolic_knowledge(self, knowledge_item: KnowledgeItem):
        self.reasoner.knowledge_base.add_symbolic_knowledge(knowledge_item)

    def add_neural_knowledge(self, knowledge_item: KnowledgeItem):
        self.reasoner.knowledge_base.add_neural_knowledge(knowledge_item)

    def query_knowledge_base(self, query: str) -> Dict[str, Any]:
        return self.reasoner.knowledge_base.query(query)