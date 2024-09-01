from typing import Any, Dict, List

from pydantic import BaseModel


class MABOSServiceSummary(BaseModel):
    name: str
    agent_count: int
    ontology_summary: Dict[str, Any]
    goals: List[str] = []
    beliefs: List[str] = []
    intentions: List[str] = []

class MABOSServiceModel(BaseModel):
    summary: MABOSServiceSummary