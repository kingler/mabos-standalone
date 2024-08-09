from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.models.knowledge import knowledge_base
from app.core.models.system.multiagent_system import MultiAgentSystem
from app.core.models.agent import Agent
from typing import List, Optional
from uuid import UUID
from app.core.models.consistency_checker import ConsistencyChecker
from app.core.models.knowledge.reasoning.temporal_reasoning import TemporalReasoning
from app.core.models.knowledge.distributed_knowledge import DistributedKnowledge
from app.core.models.knowledge.active_knowledge_acquisition import ActiveKnowledgeAcquisition
from app.core.models.knowledge.conflict_resolution import ConflictResolution
from app.core.models.knowledge.explanation_generator import ExplanationGenerator
from app.db.db_integration import DatabaseIntegration
from app.core.models.knowledge.reasoning.reasoning_engine import ReasoningEngine

class MASService:
    def __init__(self, num_agents: int, num_states: int, state_size: int, action_size: int, ontology_path: str):
        self.consistency_checker = ConsistencyChecker(knowledge_base, Ontology)
        self.temporal_reasoning = TemporalReasoning(knowledge_base)
        self.distributed_knowledge = DistributedKnowledge(DatabaseIntegration)
        self.active_knowledge_acquisition = ActiveKnowledgeAcquisition(knowledge_base, Ontology)
        self.conflict_resolution = ConflictResolution(knowledge_base)
        self.explanation_generator = ExplanationGenerator(knowledge_base, ReasoningEngine)

    def add_agent(self, agent: Agent) -> Agent:
        return self.mas.add_agent(agent)

    def get_agent(self, agent_id: UUID) -> Optional[Agent]:
        return self.mas.get_agent(agent_id)

    def remove_agent(self, agent_id: UUID) -> bool:
        return self.mas.remove_agent(agent_id)

    def list_agents(self) -> List[Agent]:
        return self.mas.list_agents()

    def send_message(self, sender_id: UUID, receiver_id: UUID, content: str):
        self.mas.send_message(sender_id, receiver_id, content)

    def step(self):
        self.mas.step()

    def run(self, steps: int):
        self.mas.run(steps)