from typing import Optional

from pydantic import BaseModel, Field


class Desire(BaseModel):
    """
    Represents a desire held by an agent.

    Attributes:
        desire_id (str): The unique identifier of the desire.
        description (str): Description of the desire.
        priority (float): Priority level of the desire.
        status (str): Current status of the desire (active, suspended, completed).
    """
    desire_id: str = Field(..., description="The unique identifier of the desire")
    description: str = Field(..., description="Description of the desire")
    priority: float = Field(..., description="Priority level of the desire")
    status: str = Field(default="active", description="Current status of the desire (active, suspended, completed)")

    def activate(self):
        """
        Activate the desire.
        """
        self.status = "active"

    def suspend(self):
        """
        Suspend the desire.
        """
        self.status = "suspended"

    def complete(self):
        """
        Mark the desire as completed.
        """
        self.status = "completed"

    def update_status(self, new_status: str):
        """
        Update the status of the desire.

        Args:
            new_status (str): The new status to set (active, suspended, completed).
        """
        if new_status in ["active", "suspended", "completed"]:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Status must be one of 'active', 'suspended', or 'completed'.")
