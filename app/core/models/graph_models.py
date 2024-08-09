from pydantic import BaseModel
from typing import Dict

class GraphSummary(BaseModel):
    num_triples: int
    num_subjects: int
    num_predicates: int
    num_objects: int
    subject_types: Dict[str, int]
    predicate_types: Dict[str, int]
    object_types: Dict[str, int]

class GraphModel(BaseModel):
    summary: GraphSummary