from typing import Dict, Any, List
from uuid import UUID
from app.core.models.system.world_model import WorldModel

class WorldModelService:
    def __init__(self, world_model: WorldModel):
        self.world_model = world_model

    def get_state(self) -> Dict[str, Any]:
        return self.world_model.state

    def update_state(self, updates: Dict[str, Any]) -> Dict[str, Any]:
        self.world_model.update_state(updates)
        return self.world_model.state

    def get_agents(self) -> Dict[UUID, Dict[str, Any]]:
        return self.world_model.agents

    def add_agent(self, agent_id: UUID, agent_data: Dict[str, Any]) -> Dict[str, Any]:
        self.world_model.add_agent(agent_id, agent_data)
        return self.world_model.agents[agent_id]

    def update_agent(self, agent_id: UUID, updates: Dict[str, Any]) -> Dict[str, Any]:
        self.world_model.update_agent(agent_id, updates)
        return self.world_model.agents[agent_id]

    def get_objects(self) -> Dict[str, Dict[str, Any]]:
        return self.world_model.objects

    def add_object(self, object_id: str, object_data: Dict[str, Any]) -> Dict[str, Any]:
        self.world_model.add_object(object_id, object_data)
        return self.world_model.objects[object_id]

    def update_object(self, object_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        self.world_model.update_object(object_id, updates)
        return self.world_model.objects[object_id]

    def get_relationships(self) -> List[Dict[str, Any]]:
        return self.world_model.relationships

    def add_relationship(self, relationship: Dict[str, Any]) -> Dict[str, Any]:
        self.world_model.add_relationship(relationship)
        return relationship

    def query_ontology(self, query: str) -> List[Any]:
        return self.world_model.query_world_knowledge(query)

    def update_ontology(self, new_information: str) -> Dict[str, Any]:
        self.world_model.update_ontology(new_information)
        return {
            "classes": self.world_model.ontology_manager.get_class_hierarchy(),
            "properties": self.world_model.ontology_manager.get_properties()
        }

    def get_agent_view(self, agent_id: UUID) -> Dict[str, Any]:
        return self.world_model.get_agent_view(agent_id)