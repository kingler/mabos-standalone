from pydantic import BaseModel
from typing import Dict, List, Any

class MABOSServiceSummary(BaseModel):
    name: str
    agent_count: int
    ontology_summary: Dict[str, Any]
    goals: List[str] = []
    beliefs: List[str] = []
    intentions: List[str] = []

class MABOSServiceModel(BaseModel):
    summary: MABOSServiceSummary