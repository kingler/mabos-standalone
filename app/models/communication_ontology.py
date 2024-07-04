from pydantic import BaseModel, Field
from typing import Dict, Any

class CommunicationOntology(BaseModel):
    """
    Represents a communication ontology for agent interactions.

    Attributes:
        ontology (Dict[str, Dict[str, Any]]): The communication ontology dictionary.
    """
    ontology: Dict[str, Dict[str, Any]] = Field(
        default={
            "request": {"description": "Request for information or action", "parameters": {}},
            "inform": {"description": "Provide information", "parameters": {"content": "Any"}},
            "propose": {"description": "Propose a course of action", "parameters": {"proposal": "str"}},
            "agree": {"description": "Agree to a proposal", "parameters": {"proposal_id": "str"}},
            "refuse": {"description": "Refuse a proposal", "parameters": {"proposal_id": "str", "reason": "str"}},
            "query": {"description": "Ask a question", "parameters": {"question": "str"}},
            "counter-propose": {"description": "Propose an alternative", "parameters": {"original_proposal_id": "str", "counter_proposal": "str"}},
            "broadcast": {"description": "Send message to all agents", "parameters": {"content": "Any"}},
        },
        description="The communication ontology dictionary"
    )

    def get_meaning(self, term: str) -> str:
        """
        Get the meaning (description) of a term in the ontology.

        Args:
            term (str): The term to look up in the ontology.

        Returns:
            str: The description of the term if found, otherwise an empty string.
        """
        return self.ontology.get(term, {}).get("description", "")

    def get_parameters(self, term: str) -> Dict[str, Any]:
        """
        Get the parameters associated with a term in the ontology.

        Args:
            term (str): The term to look up in the ontology.

        Returns:
            Dict[str, Any]: The parameters of the term if found, otherwise an empty dictionary.
        """
        return self.ontology.get(term, {}).get("parameters", {})