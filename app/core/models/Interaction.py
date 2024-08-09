from uuid import UUID
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from .message import Message


class Interaction(BaseModel):
    """
    Represents an interaction between participants.

    Attributes:
        id (str): The unique identifier of the interaction.
        participants (List[str]): The list of participant IDs involved in the interaction.
        messages (List[Message]): The list of messages exchanged in the interaction.
        created_at (datetime): The timestamp when the interaction was created.
        updated_at (datetime): The timestamp when the interaction was last updated.
    """
    id: str = Field(default_factory=lambda: str(UUID.uuid()))
    participants: List[str]
    messages: List[Message] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def add_message(self, message: Message):
        """
        Adds a new message to the interaction.

        Args:
            message (Message): The message to be added.
        """
        self.messages.append(message)
        self.updated_at = datetime.utcnow()

    def get_latest_message(self) -> Message:
        """
        Retrieves the latest message in the interaction.

        Returns:
            Message: The latest message, or None if no messages exist.
        """
        if self.messages:
            return self.messages[-1]
        return None
