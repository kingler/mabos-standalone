from abc import ABC, abstractmethod

class ArchitecturalStyle(ABC):
    @abstractmethod
    def apply(self, mas: 'MultiAgentSystem'):
        pass

class HierarchicalStyle(ArchitecturalStyle):
    def apply(self, mas: 'MultiAgentSystem'):
        # Apply hierarchical style to MAS
        pass

class FederatedStyle(ArchitecturalStyle):
    def apply(self, mas: 'MultiAgentSystem'):
        # Apply federated style to MAS
        pass