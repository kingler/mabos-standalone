from typing import Any, Dict, List, Optional
from uuid import UUID

from app.models.consistency_checker import ConsistencyChecker
from app.models.knowledge.active_knowledge_acquisition import ActiveKnowledgeAcquisition
from app.models.knowledge.conflict_resolution import ConflictResolution
from app.models.knowledge.distributed_knowledge import DistributedKnowledge
from app.models.knowledge.explanation_generator import ExplanationGenerator
from app.tools.reasoning_engine import ReasoningEngine
from app.models.knowledge.reasoning.temporal_reasoning import TemporalReasoning
from app.models.mdd.mdd_mas_model import Agent, Model
from app.models.system.multiagent_system import MultiAgentSystem
from app.services import knowledge_base_service
from app.services.ontology_service import OntologyService
from app.services.erp_service import ERPService
from app.services.mdd_mas_services import ModelingService
from app.db.arango_db_client import ArangoDBClient
from app.models.rules.rules import Rules
from app.tools.reasoner import Reasoner
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.config.config import CONFIG
from app.models.business.business_profile import BusinessProfile
from app.models.system.world_model import WorldModel


class MABOSService:
    @classmethod
    async def create(cls, erp_service: ERPService, modeling_service: ModelingService, 
             num_agents: int, num_states: int, state_size: int, action_size: int, 
             ontology_path: str) -> 'MABOSService':
        """Create a new MABOSService instance.
        
        Args:
            erp_service: ERP service instance
            modeling_service: Modeling service instance
            num_agents: Number of agents in the system
            num_states: Number of states in the system
            state_size: Size of each state
            action_size: Size of each action
            ontology_path: Path to the ontology file
            
        Returns:
            A new MABOSService instance
        """
        instance = cls()
        instance.erp_service = erp_service
        instance.modeling_service = modeling_service
        
        # Create an instance of OntologyService and load the ontology
        instance.ontology_service = OntologyService()
        instance.ontology = instance.ontology_service.load_ontology(ontology_path)
        
        # Create domain rules
        instance.domain_rules = Rules()
        # Add any default rules here if needed
        # instance.domain_rules.add_rule("condition", "action")
        
        # Create knowledge base
        instance.knowledge_base = KnowledgeBase()
        
        # Create reasoner
        instance.reasoner = Reasoner(knowledge_base=instance.knowledge_base)
        
        instance.consistency_checker = ConsistencyChecker(
            knowledge_base_service, 
            instance.ontology_service,
            instance.domain_rules
        )
        
        instance.temporal_reasoning = TemporalReasoning(
            knowledge_base=instance.knowledge_base,
            reasoner=instance.reasoner
        )
        
        instance.distributed_knowledge = DistributedKnowledge(knowledge_base_service)
        instance.active_knowledge_acquisition = ActiveKnowledgeAcquisition(knowledge_base_service, instance.ontology_service)
        instance.conflict_resolution = ConflictResolution(knowledge_base_service)
        instance.explanation_generator = ExplanationGenerator(knowledge_base_service, ReasoningEngine)
        
        # Initialize database client
        instance.db_client = ArangoDBClient(
            host=CONFIG.ARANGO_HOST,
            port=CONFIG.ARANGO_PORT,
            username=CONFIG.ARANGO_USER,
            password=CONFIG.ARANGO_PASSWORD,
            database=CONFIG.ARANGO_DATABASE
        )
        
        # Create a default business profile for initialization
        business_profile = await BusinessProfile.get_current()
        
        # Create world model
        world_model = WorldModel.create(
            num_agents=num_agents,
            num_states=num_states,
            state_size=state_size,
            action_size=action_size,
            ontology_path=ontology_path,
            business_profile=business_profile
        )
        
        # Initialize the multi-agent system with world model
        instance.mas = MultiAgentSystem.create(
            num_agents=num_agents,
            num_states=num_states,
            state_size=state_size,
            action_size=action_size,
            ontology_path=ontology_path
        )
        
        return instance

    async def initialize(self):
        """Initialize the service asynchronously."""
        await self.mas.initialize()

    async def create_agent(self, initial_config: Dict[str, Any], business_domain_ontology: Dict[str, Any] = None) -> Agent:
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

        if business_domain_ontology:
            # Generate a domain-specific ontology based on the business domain ontology
            domain_ontology = self.modeling_service.generate_domain_ontology(business_domain_ontology)
            
            # Associate the domain ontology with the agent's model
            await self.modeling_service.associate_ontology(created_model.id, domain_ontology)
            
            # Load the domain ontology into the agent's knowledge base
            await self.load_ontology(created_agent.id, domain_ontology)

        # Store agent data in database
        agent_data = {
            'id': str(created_agent.id),
            'name': initial_config['name'],
            'type': initial_config['type'],
            'industry': initial_config.get('industry'),
            'employee_count': initial_config.get('employee_count'),
            'model_id': str(created_model.id),
            'erp_system_id': erp_system.id if erp_system else None
        }
        self.db_client.create_document('agents', agent_data)

        return created_agent

    def get_agent(self, agent_id: UUID) -> Optional[Agent]:
        return self.mas.get_agent(agent_id)

    async def update_agent(self, agent_id: UUID, updates: Dict[str, Any]) -> Agent:
        agent = self.mas.get_agent(agent_id)
        if agent:
            for key, value in updates.items():
                setattr(agent, key, value)
            # Update agent data in database
            self.db_client.update_document('agents', str(agent_id), updates)
            return agent
        raise ValueError("Agent not found")

    def remove_agent(self, agent_id: UUID) -> bool:
        success = self.mas.remove_agent(agent_id)
        if success:
            # Remove agent data from database
            self.db_client.delete_document('agents', str(agent_id))
        return success

    def list_agents(self) -> List[Agent]:
        return self.mas.list_agents()

    def send_message(self, sender_id: UUID, receiver_id: UUID, content: str):
        self.mas.send_message(sender_id, receiver_id, content)

    def step(self):
        self.mas.step()

    def run(self, steps: int):
        self.mas.run(steps)

    async def associate_model(self, agent_id: UUID, model_id: UUID):
        """Associate a model with an agent."""
        try:
            self.db_client.create_document('model_associations', {
                'agent_id': str(agent_id),
                'model_id': str(model_id)
            })
        except Exception as e:
            raise Exception(f"Failed to associate model with agent: {str(e)}")

    async def load_ontology(self, agent_id: UUID, ontology: Dict[str, Any]):
        """Load an ontology into an agent's knowledge base."""
        try:
            self.db_client.create_document('agent_ontologies', {
                'agent_id': str(agent_id),
                'ontology': ontology
            })
        except Exception as e:
            raise Exception(f"Failed to load ontology for agent: {str(e)}")
