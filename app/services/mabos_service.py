from typing import Dict, Any
from uuid import UUID
from app.services.erp_service import ERPService
from app.models.erp_models import ERPSystem
from app.services.mdd_mas_services import ModelingService, AgentService
from app.core.mdd_mas.mdd_mas_model import Model, Agent

class MABOSService:
    def __init__(self, erp_service: ERPService, modeling_service: ModelingService, agent_service: AgentService):
        self.erp_service = erp_service
        self.modeling_service = modeling_service
        self.agent_service = agent_service

    async def create_agent(self, initial_config: Dict[str, Any], business_domain_ontology: Dict[str, Any]) -> Agent:
        # Create a new MABOS agent using the agent service
        agent = Agent(name=initial_config['name'], type=initial_config['type'])
        created_agent = await self.agent_service.create_agent(agent)

        # Create a model for the agent
        model = Model(name=f"{initial_config['name']} Model", type="Agent Model")
        created_model = await self.modeling_service.create_model(model)

        # Associate the model with the agent (assuming there's a method to do this)
        await self.agent_service.associate_model(created_agent.id, created_model.id)

        # Create an ERP system for the agent
        erp_system = await self.erp_service.create_erp_system(initial_config['name'])

        # Generate a domain-specific ontology based on the business domain ontology
        domain_ontology = self.modeling_service.generate_domain_ontology(business_domain_ontology)
        
        # Associate the domain ontology with the agent's model
        await self.modeling_service.associate_ontology(created_model.id, domain_ontology)
        
        # Load the domain ontology into the agent's knowledge base
        await self.agent_service.load_ontology(created_agent.id, domain_ontology)

        return created_agent

    async def get_agent(self, agent_id: UUID) -> Agent:
        return await self.agent_service.get_agent(agent_id)

    async def update_agent(self, agent_id: UUID, updates: Dict[str, Any]) -> Agent:
        return await self.agent_service.update_agent(agent_id, updates)

    async def delete_agent(self, agent_id: UUID) -> None:
        await self.agent_service.delete_agent(agent_id)

    # Add more methods as needed for MABOS functionality