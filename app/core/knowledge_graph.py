from __future__ import annotations
from typing import List, Dict, Any, TYPE_CHECKING
import networkx as nx
from pydantic import BaseModel
from rdflib import Literal, URIRef
from rdflib.namespace import RDF

if TYPE_CHECKING:
    from app.models.knowledge_base import KnowledgeBase

class KnowledgeGraph(BaseModel):
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base
        self.graph = nx.MultiDiGraph()
        self.build_graph()

    def build_graph(self):
        for s, p, o in self.knowledge_base.graph:
            s_id, o_id = str(s), str(o)
            self.graph.add_node(s_id, type=self.get_node_type(s))
            self.graph.add_node(o_id, type=self.get_node_type(o))
            self.graph.add_edge(s_id, o_id, predicate=str(p))
            
            if isinstance(o, Literal):
                self.graph.nodes[s_id][str(p)] = str(o)

    def get_node_type(self, node: URIRef) -> str:
        for node_class in self.knowledge_base.ontology.get_classes():
            if (node, RDF.type, URIRef(node_class)) in self.knowledge_base.graph:
                return node_class
        return None

    def add_node(self, node_id: str, node_data: Dict[str, Any]):
        self.graph.add_node(node_id, **node_data)
        
    def add_edge(self, source_id: str, target_id: str, edge_data: Dict[str, Any]):
        self.graph.add_edge(source_id, target_id, **edge_data)
        
    def get_node(self, node_id: str) -> Dict[str, Any]:
        return dict(self.graph.nodes[node_id])
    
    def get_neighbors(self, node_id: str) -> List[str]:
        return list(self.graph.neighbors(node_id))