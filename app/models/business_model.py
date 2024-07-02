from pydantic import BaseModel
from typing import List, Dict, Any

class BusinessModel(BaseModel):
    id: str
    type: str  # AOM, BMC, BMM, BPMN, UML
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]
