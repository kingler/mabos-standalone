from __future__ import annotations
from typing import List, Dict, Any, Optional, TYPE_CHECKING, ForwardRef
import networkx as nx
from pydantic import BaseModel, Field, SkipValidation
from rdflib import Literal, URIRef
from rdflib.namespace import RDF

if TYPE_CHECKING:
    from app.models.knowledge_base import KnowledgeBase

KnowledgeBaseRef = ForwardRef('KnowledgeBase')
KnowledgeGraphRef = ForwardRef('KnowledgeGraph')

class KnowledgeGraph(BaseModel):
    knowledge_base: KnowledgeBaseRef = None
    graph: SkipValidation[nx.MultiDiGraph] = Field(default_factory=nx.MultiDiGraph)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, knowledge_base: KnowledgeBaseRef, **data):
        super().__init__(knowledge_base=knowledge_base, **data)
        self.build_graph()

    def build_graph(self) -> None:
        """
        Builds the knowledge graph from the knowledge base.
        """
        for s, p, o in self.knowledge_base.graph:
            s_id, o_id = str(s), str(o)
            self.add_node(s_id, {"type": self.get_node_type(s)})
            self.add_node(o_id, {"type": self.get_node_type(o)})
            self.add_edge(s_id, o_id, {"predicate": str(p)})
            
            if isinstance(o, Literal):
                self.graph.nodes[s_id][str(p)] = str(o)

    def get_node_type(self, node: URIRef) -> Optional[str]:
        """
        Gets the type of a node.

        Args:
            node (URIRef): The node to get the type for.

        Returns:
            Optional[str]: The type of the node, or None if not found.
        """
        return next(
            (str(node_class) for node_class in self.knowledge_base.ontology.get_classes()
             if (node, RDF.type, URIRef(node_class)) in self.knowledge_base.graph),
            None
        )
    def add_node(self, node_id: str, node_data: Dict[str, Any]) -> None:
        """
        Adds a node to the graph.

        Args:
            node_id (str): The ID of the node.
            node_data (Dict[str, Any]): The data associated with the node.
        """
        self.graph.add_node(node_id, **node_data)
        
    def add_edge(self, source_id: str, target_id: str, edge_data: Dict[str, Any]) -> None:
        """
        Adds an edge to the graph.

        Args:
            source_id (str): The ID of the source node.
            target_id (str): The ID of the target node.
            edge_data (Dict[str, Any]): The data associated with the edge.
        """
        self.graph.add_edge(source_id, target_id, **edge_data)
        
    def get_node(self, node_id: str) -> Dict[str, Any]:
        """
        Gets the data associated with a node.

        Args:
            node_id (str): The ID of the node.

        Returns:
            Dict[str, Any]: The data associated with the node.

        Raises:
            KeyError: If the node is not found in the graph.
        """
        if node_id not in self.graph:
            raise KeyError(f"Node {node_id} not found in the graph.")
        return dict(self.graph.nodes[node_id])
    
    def get_neighbors(self, node_id: str) -> List[str]:
        """
        Gets the neighbors of a node.

        Args:
            node_id (str): The ID of the node.

        Returns:
            List[str]: The IDs of the neighboring nodes.

        Raises:
            KeyError: If the node is not found in the graph.
        """
        if node_id not in self.graph:
            raise KeyError(f"Node {node_id} not found in the graph.")
        return list(self.graph.neighbors(node_id))
    