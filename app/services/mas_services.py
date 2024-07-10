from app.models.multiagent_system import MultiAgentSystem
from app.models.agent import Agent
from typing import List, Optional
from uuid import UUID
from app.core.consistency_checker import ConsistencyChecker
from app.core.temporal_reasoning import TemporalReasoning
from app.core.distributed_knowledge import DistributedKnowledge
from app.core.active_knowledge_acquisition import ActiveKnowledgeAcquisition
from app.core.conflict_resolution import ConflictResolution
from app.core.explanation_generator import ExplanationGenerator

class MASService:
    def __init__(self, num_agents: int, num_states: int, state_size: int, action_size: int, ontology_path: str):
        self.consistency_checker = ConsistencyChecker(knowledge_base, ontology)
        self.temporal_reasoning = TemporalReasoning(knowledge_base)
        self.distributed_knowledge = DistributedKnowledge(db_integration)
        self.active_knowledge_acquisition = ActiveKnowledgeAcquisition(knowledge_base, ontology)
        self.conflict_resolution = ConflictResolution(knowledge_base)
        self.explanation_generator = ExplanationGenerator(knowledge_base, reasoning_engine)

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