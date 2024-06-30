from pydantic import BaseModel, Field
from typing import Dict

class CommunicationOntology(BaseModel):
    ontology: Dict[str, Dict[str, str]] = Field(
        default={
            "request": {"description": "Request for information or action"},
            "inform": {"description": "Provide information"},
            "propose": {"description": "Propose a course of action"},
            "agree": {"description": "Agree to a proposal"},
            "refuse": {"description": "Refuse a proposal"},
            "query": {"description": "Ask a question"},
            "counter-propose": {"description": "Propose an alternative"},
            "broadcast": {"description": "Send message to all agents"},
        }
    )

    def get_meaning(self, term: str) -> str:
        return self.ontology.get(term, {}).get("description", "")