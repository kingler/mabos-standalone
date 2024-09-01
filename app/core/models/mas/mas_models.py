from typing import Any, Dict, List

from pydantic import BaseModel


class Inconsistency(BaseModel):
    type: str
    description: str

class KnowledgeGap(BaseModel):
    concept: str
    description: str

class Conflict(BaseModel):
    entities: List[str]
    description: str

class Explanation(BaseModel):
    decision: Dict[str, Any]
    reasoning: str
    evidence: Dict[str, Any]