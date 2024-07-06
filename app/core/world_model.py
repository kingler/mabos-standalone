import uuid
from pydantic import BaseModel, Field
from typing import Dict, Any, List
from uuid import UUID
from app.core.ontology_manager import OntologyManager
from app.models.organization import Organization
from app.services.organization_service import OrganizationService
from app.core.stochastic_kinetic_model import StochasticKineticModel
from app.core.fnrl import FNRL
from app.core.mdd_mas.togaf_mdd_models import EnterpriseArchitecture
from app.core.mdd_mas.tropos_mdd_model import TroposModel

class WorldModel(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    state: Dict[str, Any] = Field(default_factory=dict)
    agents: Dict[UUID, Dict[str, Any]] = Field(default_factory=dict)
    objects: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    relationships: List[Dict[str, Any]] = Field(default_factory=list)
    ontology_manager: OntologyManager = None
    organization_service: OrganizationService = Field(default_factory=OrganizationService)
    stochastic_kinetic_model: StochasticKineticModel = None
    fnrl_model: FNRL = None
    enterprise_architectures: Dict[UUID, EnterpriseArchitecture] = Field(default_factory=dict)
    
    # Tropos models
    tropos_models: Dict[UUID, TroposModel] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True
        
    def __init__(self, **data):
        super().__init__(**data)
        ontology_path = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/core/ontologies/mabos.owl"
        self.ontology_manager = OntologyManager(ontology_path)
        
        # Initialize StochasticKineticModel and FNRL
        num_agents = len(self.agents)
        num_states = 10  # You may want to adjust this based on your specific use case
        state_size = 10  # Adjust based on your state representation
        action_size = 5  # Adjust based on your action space
        
        self.stochastic_kinetic_model = StochasticKineticModel(num_agents, num_states)
        self.fnrl_model = FNRL(num_agents, state_size, action_size)

    def update_state(self, updates: Dict[str, Any]):
        self.state.update(updates)
        for key, value in updates.items():
            self.ontology_manager.update_property("WorldState", key, value)

    def add_agent(self, agent_id: UUID, agent_data: Dict[str, Any]):
        self.agents[agent_id] = agent_data
        self.ontology_manager.add_individual(f"Agent_{agent_id}", "Agent")
        for key, value in agent_data.items():
            self.ontology_manager.update_property(f"Agent_{agent_id}", key, value)

    def update_agent(self, agent_id: UUID, updates: Dict[str, Any]):
        if agent_id in self.agents:
            self.agents[agent_id].update(updates)
            for key, value in updates.items():
                self.ontology_manager.update_property(f"Agent_{agent_id}", key, value)
        
        # Update StochasticKineticModel
        observations = [self.agents[agent_id].get('observation', [0] * self.stochastic_kinetic_model.num_states)]
        self.update_stochastic_kinetic_model(observations)
        
        # Train FNRL model
        states = [self.agents[agent_id].get('state', [0] * self.fnrl_model.models[0].input_shape[2])]
        actions = [self.agents[agent_id].get('action', [0] * self.fnrl_model.models[0].output_shape[1])]
        self.train_fnrl_model(list(self.agents.keys()).index(agent_id), states, actions)

    def add_object(self, object_id: str, object_data: Dict[str, Any]):
        self.objects[object_id] = object_data
        self.ontology_manager.add_individual(f"Object_{object_id}", "Object")
        for key, value in object_data.items():
            self.ontology_manager.update_property(f"Object_{object_id}", key, value)

    def update_object(self, object_id: str, updates: Dict[str, Any]):
        if object_id in self.objects:
            self.objects[object_id].update(updates)
            for key, value in updates.items():
                self.ontology_manager.update_property(f"Object_{object_id}", key, value)

    def add_relationship(self, relationship: Dict[str, Any]):
        self.relationships.append(relationship)
        subject = relationship["subject"]
        predicate = relationship["predicate"]
        object = relationship["object"]
        self.ontology_manager.update_property(subject, predicate, object)

    def get_agent_view(self, agent_id: UUID) -> Dict[str, Any]:
        agent_view = {
        "state": self.state,
        "agent": self.agents.get(agent_id, {}),
        "visible_objects": self.objects,
        "relationships": self.relationships,
        "predicted_next_state": self.predict_next_state()[list(self.agents.keys()).index(agent_id)],
        "predicted_action": self.predict_action(list(self.agents.keys()).index(agent_id), self.agents[agent_id].get('state', [0] * self.fnrl_model.models[0].input_shape[2])).tolist()
    }
    
        # Query the ontology for additional information
        agent_query = f"""
        SELECT ?property ?value
        WHERE {{
            Agent_{agent_id} ?property ?value .
        }}
        """
        agent_info = self.ontology_manager.query_ontology(agent_query)
        agent_view["ontology_info"] = agent_info
        
        return agent_view

    def query_world_knowledge(self, query: str) -> List[Any]:
        return self.ontology_manager.query_ontology(query)
        
    def create_organization(self, organization_data: Dict[str, Any]) -> Organization:
        return self.organization_service.create_organization(organization_data)

    def get_organization(self, name: str) -> Organization:
        return self.organization_service.get_organization(name)

    def update_organization(self, name: str, organization_data: Dict[str, Any]) -> Organization:
        return self.organization_service.update_organization(name, organization_data)

    def delete_organization(self, name: str) -> bool:
        return self.organization_service.delete_organization(name)

    def assign_agent_to_role(self, organization_name: str, agent_id: UUID, role: str):
        agent = self.agents.get(agent_id)
        if agent:
            self.organization_service.assign_agent_to_role(organization_name, agent, role)

    def get_agents_with_role(self, organization_name: str, role: str) -> List[Dict[str, Any]]:
        agents = self.organization_service.get_agents_with_role(organization_name, role)
        return [self.agents[agent.id] for agent in agents]
    
    def update_stochastic_kinetic_model(self, observations):
        self.stochastic_kinetic_model.update(observations)

    def predict_next_state(self):
        return self.stochastic_kinetic_model.predict_next_state()

    def train_fnrl_model(self, agent_id, states, actions):
        self.fnrl_model.train(agent_id, states, actions)

    def predict_action(self, agent_id, state):
        return self.fnrl_model.predict(agent_id, state)
    
    def add_enterprise_architecture(self, ea: EnterpriseArchitecture):
        self.enterprise_architectures[ea.id] = ea

    def update_enterprise_architecture(self, ea_id: UUID, updates: Dict[str, Any]):
        if ea_id in self.enterprise_architectures:
            self.enterprise_architectures[ea_id].update(updates)