from abc import ABC, abstractmethod

from app.core.models.system.multiagent_system import MultiAgentSystem


class ArchitecturalStyle(ABC):
    @abstractmethod
    def apply(self, mas: 'MultiAgentSystem'):
        """
        Apply the architectural style to the given Multi-Agent System.

        This method should be implemented by subclasses to define how
        a specific architectural style is applied to the MAS.

        Args:
            mas (MultiAgentSystem): The Multi-Agent System to apply the style to.

        Returns:
            None
        """
        pass

    @abstractmethod
    def validate(self, mas: 'MultiAgentSystem') -> bool:
        """
        Validate if the Multi-Agent System conforms to the architectural style.

        Args:
            mas (MultiAgentSystem): The Multi-Agent System to validate.

        Returns:
            bool: True if the MAS conforms to the style, False otherwise.
        """
        pass

    @abstractmethod
    def get_style_name(self) -> str:
        """
        Get the name of the architectural style.

        Returns:
            str: The name of the architectural style.
        """
        pass

class HierarchicalStyle(ArchitecturalStyle):
    def apply(self, mas: 'MultiAgentSystem'):
        # Apply hierarchical style to MAS
        agents = mas.get_agents()
        
        # Sort agents by their capabilities or predefined roles
        sorted_agents = sorted(agents, key=lambda a: a.get_capability_level(), reverse=True)
        
        # Create a hierarchical structure
        for i, agent in enumerate(sorted_agents):
            if i == 0:
                # Set the top-level agent
                mas.set_top_level_agent(agent)
            else:
                # Assign each agent to a parent
                parent_index = (i - 1) // 2  # Simple binary tree structure
                parent = sorted_agents[parent_index]
                mas.set_agent_parent(agent, parent)
        
        # Update communication protocols for hierarchical structure
        mas.update_communication_protocol('hierarchical')

class FederatedStyle(ArchitecturalStyle):
    def apply(self, mas: 'MultiAgentSystem'):
        # Apply federated style to MAS
        agents = mas.get_agents()
        
        # Group agents into federations based on their specialties or domains
        federations = {}
        for agent in agents:
            domain = agent.get_domain()
            if domain not in federations:
                federations[domain] = []
            federations[domain].append(agent)
        
        # Assign a facilitator for each federation
        for domain, federation in federations.items():
            facilitator = max(federation, key=lambda a: a.get_capability_level())
            mas.set_federation_facilitator(domain, facilitator)
        
        # Set up inter-federation communication protocols
        mas.setup_inter_federation_protocols(list(federations.keys()))
        
        # Update the overall system structure to reflect federations
        mas.update_system_structure('federated', federations)