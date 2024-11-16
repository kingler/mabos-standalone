"""
Specialized knowledge model implementations for knowledge representation and reasoning.
"""
from typing import Any, Dict, List, Optional, Set
from uuid import UUID

from pydantic import Field, field_validator
from rdflib import Graph, URIRef

from .base_models import BaseModel


class KnowledgeItem(BaseModel):
    """
    Base class for knowledge items in the system.
    """
    id: UUID
    type: str
    content: Any
    source: str
    confidence: float = Field(ge=0.0, le=1.0)
    timestamp: float
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @field_validator('confidence')
    def validate_confidence(cls, v):
        if not 0.0 <= v <= 1.0:
            raise ValueError('Confidence must be between 0.0 and 1.0')
        return v


class Ontology(BaseModel):
    """
    Model representing an ontology.
    """
    id: UUID
    name: str
    namespace: str
    version: str
    graph: Graph
    concepts: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    relations: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    axioms: List[Dict[str, Any]] = Field(default_factory=list)
    imports: List[str] = Field(default_factory=list)

    def add_concept(self, concept: Dict[str, Any]) -> None:
        """Add a new concept to the ontology."""
        uri = URIRef(f"{self.namespace}{concept['name']}")
        self.concepts[concept['name']] = {
            'uri': str(uri),
            'properties': concept.get('properties', {}),
            'relations': concept.get('relations', [])
        }
        # Add to RDF graph
        self.graph.add((uri, URIRef('rdf:type'), URIRef('owl:Class')))

    def add_relation(self, relation: Dict[str, Any]) -> None:
        """Add a new relation to the ontology."""
        uri = URIRef(f"{self.namespace}{relation['name']}")
        self.relations[relation['name']] = {
            'uri': str(uri),
            'domain': relation.get('domain', []),
            'range': relation.get('range', [])
        }
        # Add to RDF graph
        self.graph.add((uri, URIRef('rdf:type'), URIRef('owl:ObjectProperty')))


class KnowledgeBase(BaseModel):
    """
    Model representing a knowledge base.
    """
    id: UUID
    name: str
    ontology: Optional[UUID]
    items: Dict[UUID, KnowledgeItem] = Field(default_factory=dict)
    indices: Dict[str, Dict[str, Set[UUID]]] = Field(default_factory=dict)
    rules: List[Dict[str, Any]] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def add_item(self, item: KnowledgeItem) -> None:
        """Add a knowledge item to the knowledge base."""
        self.items[item.id] = item
        # Update indices
        for key, value in item.metadata.items():
            if key not in self.indices:
                self.indices[key] = {}
            if str(value) not in self.indices[key]:
                self.indices[key][str(value)] = set()
            self.indices[key][str(value)].add(item.id)

    def query(self, criteria: Dict[str, Any]) -> List[KnowledgeItem]:
        """Query knowledge items based on criteria."""
        results = set()
        first = True
        
        for key, value in criteria.items():
            if key in self.indices and str(value) in self.indices[key]:
                if first:
                    results = self.indices[key][str(value)].copy()
                    first = False
                else:
                    results &= self.indices[key][str(value)]
        
        return [self.items[item_id] for item_id in results]


class ReasoningRule(BaseModel):
    """
    Model representing a reasoning rule.
    """
    id: UUID
    name: str
    description: str
    condition: str
    action: str
    priority: int = Field(default=0)
    enabled: bool = Field(default=True)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def evaluate(self, context: Dict[str, Any]) -> bool:
        """Evaluate the rule's condition in the given context."""
        try:
            return eval(self.condition, context)
        except Exception as e:
            print(f"Error evaluating rule {self.name}: {str(e)}")
            return False


class InferenceEngine(BaseModel):
    """
    Model representing an inference engine.
    """
    id: UUID
    name: str
    knowledge_base: UUID
    rules: List[ReasoningRule] = Field(default_factory=list)
    strategies: List[str] = Field(default_factory=list)
    cache: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def infer(self, facts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Perform inference based on facts and rules."""
        context = {"facts": facts}
        conclusions = []
        
        for rule in sorted(self.rules, key=lambda x: x.priority, reverse=True):
            if rule.enabled and rule.evaluate(context):
                try:
                    result = eval(rule.action, context)
                    conclusions.append({
                        "rule": rule.name,
                        "result": result
                    })
                except Exception as e:
                    print(f"Error executing rule {rule.name}: {str(e)}")
        
        return conclusions


class KnowledgeGraph(BaseModel):
    """
    Model representing a knowledge graph.
    """
    id: UUID
    name: str
    nodes: Dict[UUID, Dict[str, Any]] = Field(default_factory=dict)
    edges: Dict[UUID, Dict[str, Any]] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def add_node(self, node_id: UUID, data: Dict[str, Any]) -> None:
        """Add a node to the graph."""
        self.nodes[node_id] = data

    def add_edge(self, edge_id: UUID, source: UUID, target: UUID, data: Dict[str, Any]) -> None:
        """Add an edge to the graph."""
        self.edges[edge_id] = {
            "source": source,
            "target": target,
            **data
        }

    def get_neighbors(self, node_id: UUID) -> List[UUID]:
        """Get neighboring nodes."""
        neighbors = []
        for edge in self.edges.values():
            if edge["source"] == node_id:
                neighbors.append(edge["target"])
            elif edge["target"] == node_id:
                neighbors.append(edge["source"])
        return neighbors


class KnowledgeFactory:
    """
    Factory class for creating knowledge-related components.
    """
    @staticmethod
    def create_component(component_type: str, **kwargs) -> BaseModel:
        """
        Create a knowledge component of the specified type.
        
        Args:
            component_type: Type of knowledge component to create
            **kwargs: Additional arguments for component initialization
        
        Returns:
            Instance of the specified knowledge component type
        """
        component_classes = {
            "knowledge_item": KnowledgeItem,
            "ontology": Ontology,
            "knowledge_base": KnowledgeBase,
            "reasoning_rule": ReasoningRule,
            "inference_engine": InferenceEngine,
            "knowledge_graph": KnowledgeGraph
        }
        
        if component_class := component_classes.get(component_type):
            return component_class(**kwargs)
        
        raise ValueError(f"Unsupported knowledge component type: {component_type}")
