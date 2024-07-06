import uuid
from pydantic import BaseModel, Field
from typing import Dict, Any, List
from uuid import UUID
from app.core.ontology_manager import OntologyManager

class WorldModel(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    state: Dict[str, Any] = Field(default_factory=dict)
    agents: Dict[UUID, Dict[str, Any]] = Field(default_factory=dict)
    objects: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    relationships: List[Dict[str, Any]] = Field(default_factory=list)
    ontology_manager: OntologyManager = None

    class Config:
        arbitrary_types_allowed = True
        
    def __init__(self, **data):
        super().__init__(**data)
        ontology_path = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/core/ontologies/mabos.owl"
        self.ontology_manager = OntologyManager(ontology_path)

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
            "relationships": self.relationships
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