from .ontology import (Concept, Name, Ontology, OperativeRule, Proposition,
                       StructuralRule, Term, VerbConceptWording)

# Move this import to the end of the file
from .domain_ontology_generator import (DomainOntologyGenerator,
                                        SBVRDomainOntologyGenerator)
from .ontology_generator import OntologyGenerator
from .ontology_loader import OntologyLoader

# If needed, you can use __all__ to control what's imported when using "from ... import *"
__all__ = ['Concept', 'Name', 'Ontology', 'OperativeRule', 'Proposition',
           'StructuralRule', 'Term', 'VerbConceptWording', 
           'DomainOntologyGenerator', 'SBVRDomainOntologyGenerator',
           'OntologyGenerator', 'OntologyLoader']
