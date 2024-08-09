from pydantic import BaseModel, Field
from typing import List, Dict, Any

class BusinessModel(BaseModel):
    """
    Represents a business model.

    Attributes:
        id (str): The unique identifier of the business model.
        type (str): The type of the business model (AOM, BMC, BMM, BPMN, UML).
        nodes (List[Dict[str, Any]]): The nodes in the business model.
        edges (List[Dict[str, Any]]): The edges connecting the nodes in the business model.
    """
    id: str = Field(..., description="The unique identifier of the business model")
    type: str = Field(..., description="The type of the business model (AOM, BMC, BMM, BPMN, UML)")
    nodes: List[Dict[str, Any]] = Field(default_factory=list, description="The nodes in the business model")
    edges: List[Dict[str, Any]] = Field(default_factory=list, description="The edges connecting the nodes in the business model")
