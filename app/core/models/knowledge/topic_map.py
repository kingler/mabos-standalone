# app/models/topic_map.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from rdflib import RDF, RDFS, Graph, URIRef
import hypergraphx as hgx

class Topic(BaseModel):
    id: str
    name: str
    occurrences: List[str] = []
    associations: List[str] = []

class Association(BaseModel):
    id: str
    type: str
    members: List[str]

class TopicMap(BaseModel):
    id: str
    topics: Dict[str, Topic] = {}
    associations: Dict[str, Association] = {}
    graph: Graph = Field(default_factory=Graph)
    hypergraph: hgx.Hypergraph = Field(default_factory=hgx.Hypergraph)

    class Config:
        arbitrary_types_allowed = True

    def add_topic(self, topic: Topic):
        self.topics[topic.id] = topic
        self.hypergraph.add_node(topic.id, name=topic.name)

    def add_association(self, association: Association):
        self.associations[association.id] = association
        self.hypergraph.add_edge(association.members, type=association.type)

    def get_topic(self, topic_id: str) -> Optional[Topic]:
        return self.topics.get(topic_id)

    def get_association(self, association_id: str) -> Optional[Association]:
        return self.associations.get(association_id)

    def to_rdf(self):
        # Convert the topic map to RDF
        for topic_id, topic in self.topics.items():
            topic_uri = self.graph.URIRef(f"http://example.org/topic/{topic_id}")
            self.graph.add((topic_uri, RDF.type, self.graph.URIRef("http://example.org/Topic")))
            self.graph.add((topic_uri, RDFS.label, self.graph.Literal(topic.name)))
            
            for occurrence in topic.occurrences:
                self.graph.add((topic_uri, self.graph.URIRef("http://example.org/hasOccurrence"), self.graph.Literal(occurrence)))
            
            for association_id in topic.associations:
                association_uri = self.graph.URIRef(f"http://example.org/association/{association_id}")
                self.graph.add((topic_uri, self.graph.URIRef("http://example.org/hasAssociation"), association_uri))
        
        for association_id, association in self.associations.items():
            association_uri = self.graph.URIRef(f"http://example.org/association/{association_id}")
            self.graph.add((association_uri, RDF.type, self.graph.URIRef("http://example.org/Association")))
            self.graph.add((association_uri, self.graph.URIRef("http://example.org/associationType"), self.graph.Literal(association.type)))
            
            for member in association.members:
                member_uri = self.graph.URIRef(f"http://example.org/topic/{member}")
                self.graph.add((association_uri, self.graph.URIRef("http://example.org/hasMember"), member_uri))
        
        return self.graph

    def from_rdf(self, rdf_graph: Graph):
        # Create a topic map from an RDF graph
        for subject in rdf_graph.subjects(RDF.type, URIRef("http://example.org/Topic")):
            topic_id = str(subject).split("/")[-1]
            topic_name = rdf_graph.value(subject, RDFS.label)
            topic = Topic(id=topic_id, name=str(topic_name))
            
            # Add occurrences
            for occurrence in rdf_graph.objects(subject, URIRef("http://example.org/hasOccurrence")):
                topic.occurrences.append(str(occurrence))
            
            self.add_topic(topic)
        
        for subject in rdf_graph.subjects(RDF.type, URIRef("http://example.org/Association")):
            association_id = str(subject).split("/")[-1]
            association_type = rdf_graph.value(subject, URIRef("http://example.org/associationType"))
            members = [str(member).split("/")[-1] for member in rdf_graph.objects(subject, URIRef("http://example.org/hasMember"))]
            
            association = Association(id=association_id, type=str(association_type), members=members)
            self.add_association(association)
        
        # Update topic associations
        for topic in self.topics.values():
            topic.associations = [assoc.id for assoc in self.associations.values() if topic.id in assoc.members]