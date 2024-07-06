from pydantic import BaseModel
from typing import List, Optional

from .agent_role import AgentRole
from .agent import Agent

class OrganizationBase(BaseModel):
    name: str
    norms: List[str]
    goals: List[str] = []
    policies: List[str] = []
    communication_channels: List[str] = []

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(OrganizationBase):
    name: Optional[str] = None
    norms: Optional[List[str]] = None
    goals: Optional[List[str]] = None
    policies: Optional[List[str]] = None
    communication_channels: Optional[List[str]] = None

class Organization(OrganizationBase):
    """
    Represents an organization in the Multi-Agent System (MAS).

    Attributes:
        name (str): The name of the organization.
        roles (List[Role]): The list of roles within the organization.
        agents (List[Agent]): The list of agents associated with the organization.
        norms (List[str]): The list of norms governing the organization.
        goals (List[str]): The list of goals of the organization.
        policies (List[str]): The list of policies of the organization.
        communication_channels (List[str]): The list of communication channels used within the organization.
    """
    roles: List[AgentRole]
    agents: List[Agent]
    
    def __init__(self):
        self.roles = {}

    def assign_role(self, agent_id, role):
        if role not in self.roles:
            self.roles[role] = []
        self.roles[role].append(agent_id)

    def get_agents_with_role(self, role):
        return self.roles.get(role, [])
