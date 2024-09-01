from typing import Any, Dict, List, Tuple

from owlready2 import get_ontology
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS


class OntologyLoader:
    def __init__(self):
        self.graph = Graph()
        self.onto = None
        self.ns = None

    def load_ontology(self, file_path: str):
        self.graph.parse(file_path, format="turtle")
        self.onto = get_ontology(file_path).load()
        self.ns = Namespace(self.onto.base_iri)

    def get_classes(self) -> List[URIRef]:
        return list(self.graph.subjects(RDF.type, OWL.Class))

    def get_properties(self) -> List[URIRef]:
        return list(self.graph.subjects(RDF.type, OWL.ObjectProperty)) + \
               list(self.graph.subjects(RDF.type, OWL.DatatypeProperty))

    def get_property_domain_range(self, property: URIRef) -> Tuple[URIRef, URIRef]:
        domain = list(self.graph.objects(property, RDFS.domain))
        range_ = list(self.graph.objects(property, RDFS.range))
        return (domain[0] if domain else None, range_[0] if range_ else None)

    def get_class_hierarchy(self) -> Dict[URIRef, List[URIRef]]:
        hierarchy = {}
        for cls in self.get_classes():
            subclasses = list(self.graph.subjects(RDFS.subClassOf, cls))
            if subclasses:
                hierarchy[cls] = subclasses
        return hierarchy

    def query_ontology(self, sparql_query: str) -> List[Dict[str, Any]]:
        results = self.graph.query(sparql_query)
        return [dict(zip(result.vars, [str(term) for term in result])) for result in results]

    def get_class_instances(self, class_uri: URIRef) -> List[URIRef]:
        return list(self.graph.subjects(RDF.type, class_uri))

    def get_property_values(self, subject: URIRef, property: URIRef) -> List[URIRef]:
        return list(self.graph.objects(subject, property))

    def get_annotations(self, entity: URIRef) -> Dict[str, str]:
        annotations = {}
        for p, o in self.graph.predicate_objects(entity):
            if p in [RDFS.label, RDFS.comment]:
                annotations[str(p)] = str(o)
        return annotations

    def save_ontology(self, file_path: str, format: str = "turtle"):
        self.graph.serialize(destination=file_path, format=format)
