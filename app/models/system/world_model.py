"""
Compatibility module for world model.
Redirects to new core model implementation while maintaining backward compatibility.
"""
import warnings
from typing import Any, Dict, Optional
from uuid import UUID

from ..core import BaseModel


class WorldModel(BaseModel):
    """
    World model implementation.
    Maintains backward compatibility while using new core model structure.
    """
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "Importing WorldModel from app.models.system.world_model is deprecated. "
            "Use 'from app.models.core import WorldModel' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        super().__init__(*args, **kwargs)

    @classmethod
    async def create(cls) -> 'WorldModel':
        """Create a new world model instance."""
        return cls(
            id=UUID(int=0),  # Default ID for singleton instance
            name="World Model",
            type="world_model",
            content={}
        )

    def add_agent(self, agent_id: UUID, agent_data: Dict[str, Any]) -> None:
        """Add an agent to the world model."""
        if "agents" not in self.content:
            self.content["agents"] = {}
        self.content["agents"][str(agent_id)] = agent_data

    def update_agent(self, agent_id: UUID, updates: Dict[str, Any]) -> None:
        """Update an agent in the world model."""
        if "agents" in self.content and str(agent_id) in self.content["agents"]:
            self.content["agents"][str(agent_id)].update(updates)

    def get_agent_view(self, agent_id: UUID) -> Dict[str, Any]:
        """Get an agent's view of the world."""
        agent_data = self.content.get("agents", {}).get(str(agent_id), {})
        return {
            "state": self.content.get("state", {}),
            "agent": agent_data,
            "visible_objects": self.content.get("objects", {}),
            "relationships": self.content.get("relationships", []),
            "ontology_info": self.content.get("ontology_info", [])
        }

    def query_world_knowledge(self, query: str) -> Any:
        """Query knowledge in the world model."""
        # Implement query logic here
        return []

    async def cleanup(self):
        """Cleanup resources."""
        pass
