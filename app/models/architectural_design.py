from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List
from app.models.agent import Agent

if TYPE_CHECKING:
    from app.models.multiagent_system import MultiAgentSystem

class ArchitecturalStyle(ABC):
    """
    Abstract base class for architectural styles in a multi-agent system.
    """
    @abstractmethod
    def apply(self, mas: 'MultiAgentSystem') -> None:
        """
        Apply the architectural style to the multi-agent system.

        Args:
            mas (MultiAgentSystem): The multi-agent system to apply the style to.
        """
        pass

class HierarchicalStyle(ArchitecturalStyle):
    """
    Implements a hierarchical architectural style for a multi-agent system.
    """
    def apply(self, mas: 'MultiAgentSystem') -> None:
        """
        Apply the hierarchical style to the multi-agent system.

        Args:
            mas (MultiAgentSystem): The multi-agent system to apply the style to.
        """
        agents = mas.get_agents()
        if not agents:
            return

        # Sort agents by capability score
        sorted_agents = sorted(agents, key=lambda a: a.get_capability_score(), reverse=True)

        # Assign parent-child relationships
        for i in range(1, len(sorted_agents)):
            parent = sorted_agents[i - 1]
            child = sorted_agents[i]
            parent.add_subordinate(child)
            child.set_superior(parent)

        # Set the top-level agent as the root
        mas.set_root_agent(sorted_agents[0])

        # Update communication channels based on hierarchy
        for agent in agents:
            agent.update_communication_channels()

class FederatedStyle(ArchitecturalStyle):
    """
    Implements a federated architectural style for a multi-agent system.
    """
    def apply(self, mas: 'MultiAgentSystem') -> None:
        """
        Apply the federated style to the multi-agent system.

        Args:
            mas (MultiAgentSystem): The multi-agent system to apply the style to.
        """
        agents = mas.get_agents()
        if not agents:
            return

        # Group agents into federations
        federations = self._group_agents_into_federations(agents)

        # Assign a leader to each federation
        for federation in federations:
            leader = max(federation, key=lambda a: a.get_leadership_score())
            for agent in federation:
                if agent != leader:
                    agent.set_federation_leader(leader)
            leader.set_federation_members(federation)

        # Set up inter-federation communication channels
        for i, federation1 in enumerate(federations):
            for federation2 in federations[i+1:]:
                federation1[0].add_inter_federation_link(federation2[0])
                federation2[0].add_inter_federation_link(federation1[0])

        # Update communication channels for all agents
        for agent in agents:
            agent.update_communication_channels()

    def _group_agents_into_federations(self, agents: List[Agent]) -> List[List[Agent]]:
        """
        Group agents into federations based on their capabilities or domain.

        Args:
            agents (List[Agent]): The list of agents to group.

        Returns:
            List[List[Agent]]: A list of federations, where each federation is a list of agents.
        """
        # This is a placeholder implementation. In a real system, you would use
        # more sophisticated criteria to group agents into federations.
        federations = []
        for i in range(0, len(agents), 3):  # Group agents into federations of 3
            federation = agents[i:i+3]
            if federation:
                federations.append(federation)
        return federations