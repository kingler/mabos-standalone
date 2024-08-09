from typing import List
from app.core.models.system.organization import Organization, OrganizationCreate, OrganizationUpdate
from app.core.models.agent import Agent
from app.core.models.agent.agent_role import AgentRole

class OrganizationService:
    """
    Service class for managing organizations in the Multi-Agent System (MAS).
    """

    def __init__(self):
        self.organizations: List[Organization] = []

    def create_organization(self, organization_data: OrganizationCreate) -> Organization:
        """
        Create a new organization.

        Args:
            organization_data (OrganizationCreate): The data for creating the organization.

        Returns:
            Organization: The created organization.
        """
        organization = Organization(**organization_data.dict())
        self.organizations.append(organization)
        return organization

    def get_organization(self, name: str) -> Organization:
        """
        Get an organization by its name.

        Args:
            name (str): The name of the organization.

        Returns:
            Organization: The organization with the specified name.
        """
        for organization in self.organizations:
            if organization.name == name:
                return organization
        return None

    def update_organization(self, name: str, organization_data: OrganizationUpdate) -> Organization:
        """
        Update an existing organization.

        Args:
            name (str): The name of the organization to update.
            organization_data (OrganizationUpdate): The updated data for the organization.

        Returns:
            Organization: The updated organization.
        """
        organization = self.get_organization(name)
        if organization:
            for field, value in organization_data.dict(exclude_unset=True).items():
                setattr(organization, field, value)
        return organization

    def delete_organization(self, name: str) -> bool:
        """
        Delete an organization.

        Args:
            name (str): The name of the organization to delete.

        Returns:
            bool: True if the organization was deleted, False otherwise.
        """
        organization = self.get_organization(name)
        if organization:
            self.organizations.remove(organization)
            return True
        return False

    def assign_agent_to_role(self, organization_name: str, agent: Agent, role: AgentRole):
        """
        Assign an agent to a role within an organization.

        Args:
            organization_name (str): The name of the organization.
            agent (Agent): The agent to assign to the role.
            role (AgentRole): The role to assign the agent to.
        """
        organization = self.get_organization(organization_name)
        if organization:
            organization.assign_role(agent.id, role)

    def get_agents_with_role(self, organization_name: str, role: AgentRole) -> List[Agent]:
        """
        Get the agents assigned to a specific role within an organization.

        Args:
            organization_name (str): The name of the organization.
            role (AgentRole): The role to retrieve agents for.

        Returns:
            List[Agent]: The list of agents assigned to the specified role.
        """
        organization = self.get_organization(organization_name)
        if organization:
            return organization.get_agents_with_role(role)
        return []
