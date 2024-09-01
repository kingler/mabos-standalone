from __future__ import annotations

from app.core.models.knowledge.base import KnowledgeGraphInterface

import json
from typing import Any, Dict, List, Optional

import networkx as nx
from pydantic import BaseModel, Field, ConfigDict
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF

from app.core.models.agent.action import Action
from app.core.models.agent.agent import Agent
from app.core.models.database.database_schema_generator import DatabaseSchemaGenerator
from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.services.database_service import DatabaseService
from app.core.tools.llm_manager import LLMManager

class KnowledgeGraph(KnowledgeGraphInterface):
    graph: nx.MultiDiGraph = Field(default_factory=nx.MultiDiGraph)
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def build_graph(self, rdf_graph: Graph, ontology: Ontology):
        for s, p, o in rdf_graph:
            s_id, o_id = str(s), str(o)
            self.graph.add_node(s_id, type=self.get_node_type(s, rdf_graph, ontology))
            self.graph.add_node(o_id, type=self.get_node_type(o, rdf_graph, ontology))
            self.graph.add_edge(s_id, o_id, predicate=str(p))
            
            if isinstance(o, Literal):
                self.graph.nodes[s_id][str(p)] = str(o)

    def get_node_type(self, node: URIRef, rdf_graph: Graph, ontology: Ontology) -> Optional[str]:
        return next((str(o) for s, p, o in rdf_graph 
                     if s == node and p == RDF.type and str(o) in ontology.get_classes()), None)

    def add_node(self, node_id: str, node_data: Dict[str, Any]):
        self.graph.add_node(node_id, **node_data)
        
    def add_edge(self, source_id: str, target_id: str, edge_data: Dict[str, Any]):
        self.graph.add_edge(source_id, target_id, **edge_data)
        
    def get_node(self, node_id: str) -> Dict[str, Any]:
        return dict(self.graph.nodes[node_id])
    
    def get_neighbors(self, node_id: str) -> List[str]:
        return list(self.graph.neighbors(node_id))

class KnowledgeGraphIntegrator:
    def __init__(self, graph_database):
        self.graph_db = graph_database

    def ontology_to_graph(self, ontology: Ontology):
        # Convert ontology to knowledge graph format and store in database
        db_service = DatabaseService()
        schema_generator = DatabaseSchemaGenerator()
        
        # Generate database schema from ontology
        schema = schema_generator.generate_schema(ontology)
        
        # Create tables in the database
        schema_generator.create_tables(schema)
        
        # Generate ORM classes
        orm_classes = schema_generator.generate_orm_classes(schema)
        
        # Create nodes for each concept in the ontology
        for concept in ontology.concepts.values():
            node_data = {
                'name': concept.name,
                'type': 'Concept'
            }
            db_service.create_agent(Agent(**node_data))  # Using Agent as a generic node type
        
        # Create edges for relationships between concepts
        for relationship in ontology.relationships:
            edge_data = {
                'source': relationship.source,
                'target': relationship.target,
                'type': relationship.type
            }
            db_service.create_action(Action(**edge_data))  # Using Action to represent edges
        
        # Store properties as attributes of concept nodes
        for concept in ontology.concepts.values():
            for prop in ontology.get_properties_for_concept(concept.name):
                if node := db_service.get_agent(concept.name):
                    node.metadata[prop.name] = prop.range
                    db_service.update_agent(node)
        
        # Return the generated ORM classes for further use
        return orm_classes

    def update_graph_from_ontology(self, ontology: Ontology):
        # Update existing knowledge graph with new ontology information
        pass

    def query_graph(self, query: str) -> List[Dict[str, Any]]:
        # Execute queries against the knowledge graph
        pass

class OntologyAligner:
    def __init__(self, llm_manager: LLMManager):
        self.llm_manager = llm_manager

    async def align_ontologies(self, ontology1: Ontology, ontology2: Ontology) -> Dict[str, Any]:
        prompt = f"""
        Align the following two ontologies:

        Ontology 1:
        {ontology1.to_json()}

        Ontology 2:
        {ontology2.to_json()}

        Provide an alignment report in JSON format with the following structure:
        {{
            "aligned_concepts": [
                {{
                    "ontology1_concept": "concept_name",
                    "ontology2_concept": "concept_name",
                    "similarity_score": float
                }},
                ...
            ],
            "unaligned_concepts": {{
                "ontology1": ["concept1", "concept2", ...],
                "ontology2": ["concept1", "concept2", ...]
            }}
        }}
        """
        
        selected_model = self.llm_manager.select_model("Align ontologies", required_capabilities=["multilingual"])
        response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
        return json.loads(response)

    async def merge_ontologies(self, ontology1: Ontology, ontology2: Ontology, alignment: Dict[str, Any]) -> Ontology:
        merged_ontology = Ontology()

        # Merge aligned concepts
        for aligned_concept in alignment['aligned_concepts']:
            concept1 = aligned_concept['ontology1_concept']
            concept2 = aligned_concept['ontology2_concept']
            merged_description = f"{ontology1.get_concept_description(concept1)} | {ontology2.get_concept_description(concept2)}"
            merged_ontology.add_concept(concept1, merged_description)

            # Merge properties of aligned concepts
            properties1 = ontology1.get_properties(concept1)
            properties2 = ontology2.get_properties(concept2)
            merged_properties = list(set(properties1 + properties2))
            for property in merged_properties:
                merged_ontology.add_property(concept1, property)

        # Add unaligned concepts from ontology1
        for concept in alignment['unaligned_concepts']['ontology1']:
            merged_ontology.add_concept(concept, ontology1.get_concept_description(concept))
            for property in ontology1.get_properties(concept):
                merged_ontology.add_property(concept, property)

        # Add unaligned concepts from ontology2
        for concept in alignment['unaligned_concepts']['ontology2']:
            merged_ontology.add_concept(concept, ontology2.get_concept_description(concept))
            for property in ontology2.get_properties(concept):
                merged_ontology.add_property(concept, property)

        # Merge relationships
        for relationship in ontology1.get_relationships() + ontology2.get_relationships():
            domain = relationship['domain']
            range = relationship['range']
            if merged_ontology.has_concept(domain) and merged_ontology.has_concept(range):
                merged_ontology.add_relationship(relationship['name'], domain, range)

        return merged_ontology