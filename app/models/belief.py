from typing import Any
from pydantic import BaseModel, Field

class Belief(BaseModel):
    """
    Represents a belief held by an agent.

    Attributes:
        description (str): Description of the belief.
        certainty (float): Certainty level of the belief (0-1).
        value (Any): The value associated with the belief.
    """
    description: str = Field(..., description="Description of the belief")
    certainty: float = Field(..., ge=0, le=1, description="Certainty level of the belief (0-1)")
    value: Any = Field(..., description="The value associated with the belief")
    
    def update_certainty(self, new_certainty: float):
        """
        Updates the certainty level of the belief.

        Args:
            new_certainty (float): The new certainty level (0-1).
        """
        self.certainty = max(0, min(new_certainty, 1))  # Ensure certainty stays between 0 and 1
        
    def update_value(self, new_value: Any):
        """
        Updates the value associated with the belief.
        
        Args:
            new_value (Any): The new value to associate with the belief.
        """
        self.value = new_value