from typing import Any, Dict, List, Optional
from uuid import UUID

from app.core.models.consistency_checker import ConsistencyChecker
from app.core.models.knowledge.active_knowledge_acquisition import \
    ActiveKnowledgeAcquisition
from app.core.models.knowledge.conflict_resolution import ConflictResolution
from app.core.models.knowledge.distributed_knowledge import \
    DistributedKnowledge
from app.core.models.knowledge.explanation_generator import \
    ExplanationGenerator
from app.core.models.knowledge.reasoning.reasoning_engine import \
    ReasoningEngine
from app.core.models.knowledge.reasoning.temporal_reasoning import \
    TemporalReasoning
from app.core.models.mdd.mdd_mas_model import Agent, Model
from app.core.models.system.multiagent_system import MultiAgentSystem
from app.core.services import knowledge_base_service, ontology_service
from app.core.services.erp_service import ERPService
from app.core.services.mdd_mas_services import ModelingService
from app.db.db_integration import DatabaseIntegration


class MABOSService:
    def __init__(self, erp_service: ERPService, modeling_service: ModelingService, 
                 num_agents: int, num_states: int, state_size: int, action_size: int, 
                 ontology_path: str):
        self.erp_service = erp_service
        self.modeling_service = modeling_service
        self.ontology_service = ontology_service.load_ontology(ontology_path)
        self.consistency_checker = ConsistencyChecker(knowledge_base_service, ontology_service)
        self.temporal_reasoning = TemporalReasoning(knowledge_base_service)
        self.distributed_knowledge = DistributedKnowledge(knowledge_base_service)
        self.active_knowledge_acquisition = ActiveKnowledgeAcquisition(knowledge_base_service, ontology_service)
        self.conflict_resolution = ConflictResolution(knowledge_base_service)
        self.explanation_generator = ExplanationGenerator(knowledge_base_service, ReasoningEngine)
        self.db_integration = DatabaseIntegration(knowledge_base_service, ontology_service)
        
        # Initialize the multi-agent system
        self.mas = MultiAgentSystem(num_agents, num_states, state_size, action_size)

    async def create_agent(self, initial_config: Dict[str, Any], business_domain_ontology: Dict[str, Any]) -> Agent:
        # Create a new MABOS agent
        agent = Agent(name=initial_config['name'], type=initial_config['type'])
        created_agent = self.mas.add_agent(agent)

        # Create a model for the agent
        model = Model(name=f"{initial_config['name']} Model", type="Agent Model")
        created_model = await self.modeling_service.create_model(model)

        # Associate the model with the agent
        await self.associate_model(created_agent.id, created_model.id)

        # Create an ERP system for the agent
        erp_system = await self.erp_service.create_erp_system(initial_config['name'])

        # Generate a domain-specific ontology based on the business domain ontology
        domain_ontology = self.modeling_service.generate_domain_ontology(business_domain_ontology)
        
        # Associate the domain ontology with the agent's model
        await self.modeling_service.associate_ontology(created_model.id, domain_ontology)
        
        # Load the domain ontology into the agent's knowledge base
        await self.load_ontology(created_agent.id, domain_ontology)

        return created_agent

    def get_agent(self, agent_id: UUID) -> Optional[Agent]:
        return self.mas.get_agent(agent_id)

    async def update_agent(self, agent_id: UUID, updates: Dict[str, Any]) -> Agent:
        agent = self.mas.get_agent(agent_id)
        if agent:
            for key, value in updates.items():
                setattr(agent, key, value)
            return agent
        raise ValueError("Agent not found")

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

    # Add more methods as needed for MABOS functionality