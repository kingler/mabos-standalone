from app.core.models.agent.agent_role import AgentRole
from typing import List

class AgentRolesService:
    def __init__(self):
        self.roles: List[AgentRole] = []

    def get_all_roles(self) -> List[AgentRole]:
        """
        Retrieve all agent roles.

        Returns:
            List[AgentRole]: A list of all agent roles.
        """
        return self.roles

    def get_role_by_id(self, role_id: int) -> AgentRole:
        """
        Retrieve a specific agent role by ID.

        Args:
            role_id (int): The ID of the agent role to retrieve.

        Returns:
            AgentRole: The agent role with the specified ID, or None if not found.
        """
        for role in self.roles:
            if role.id == role_id:
                return role
        return None

    def create_role(self, role: AgentRole) -> AgentRole:
        """
        Create a new agent role.

        Args:
            role (AgentRole): The agent role to create.

        Returns:
            AgentRole: The created agent role.
        """
        self.roles.append(role)
        return role

    def update_role(self, role_id: int, updated_role: AgentRole) -> AgentRole:
        """
        Update an existing agent role.

        Args:
            role_id (int): The ID of the agent role to update.
            updated_role (AgentRole): The updated agent role data.

        Returns:
            AgentRole: The updated agent role, or None if the role was not found.
        """
        for i, role in enumerate(self.roles):
            if role.id == role_id:
                self.roles[i] = updated_role
                return updated_role
        return None

    def delete_role(self, role_id: int) -> bool:
        """
        Delete an agent role.

        Args:
            role_id (int): The ID of the agent role to delete.

        Returns:
            bool: True if the role was deleted successfully, False otherwise.
        """
        for i, role in enumerate(self.roles):
            if role.id == role_id:
                del self.roles[i]
                return True
        return False
