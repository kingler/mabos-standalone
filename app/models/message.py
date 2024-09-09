from datetime import datetime
from enum import Enum
from typing import Any, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Performative(str, Enum):
    """
    Represents the performative of a message in the agent communication language.
    """
    INFORM = "inform"
    REQUEST = "request"
    AGREE = "agree"
    REFUSE = "refuse"
    QUERY = "query"
    PROPOSE = "propose"
    ACCEPT_PROPOSAL = "accept-proposal"
    REJECT_PROPOSAL = "reject-proposal"

class Message(BaseModel):
    """
    Represents a message exchanged between agents.
    """
    id: UUID = Field(default_factory=uuid4)
    sender_id: UUID
    recipient_id: UUID
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    conversation_id: Optional[UUID] = None
    reply_to: Optional[UUID] = None
    language: str = "english"
    ontology: Optional[str] = None
    protocol: Optional[str] = None
    performative: Performative

    def __str__(self):
        return f"Message from {self.sender_id} to {self.recipient_id}: {self.content}"

class ACLMessage(BaseModel):
    """
    Represents a message in the agent communication language (ACL).
    """
    id: UUID = Field(default_factory=uuid4)
    sender_id: UUID
    receiver_id: UUID
    performative: Performative
    content: Any
    conversation_id: Optional[UUID] = None
    reply_with: Optional[str] = None
    in_reply_to: Optional[str] = None
    reply_by: Optional[datetime] = None
    language: str = "English"
    ontology: Optional[str] = None
    protocol: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        """
        Converts the ACLMessage object to a dictionary representation.
        
        Returns:
            dict: The dictionary representation of the ACLMessage object.
        """
        return {
            "id": str(self.id),
            "sender_id": str(self.sender_id),
            "receiver_id": str(self.receiver_id),
            "performative": self.performative.value,
            "content": self.content,
            "conversation_id": str(self.conversation_id) if self.conversation_id else None,
            "reply_with": self.reply_with,
            "in_reply_to": self.in_reply_to,
            "reply_by": self.reply_by.isoformat() if self.reply_by else None,
            "language": self.language,
            "ontology": self.ontology,
            "protocol": self.protocol,
            "timestamp": self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'ACLMessage':
        """
        Creates an ACLMessage object from a dictionary representation.
        
        Args:
            data (dict): The dictionary representation of the ACLMessage object.
        
        Returns:
            ACLMessage: The ACLMessage object created from the dictionary.
        """
        data['performative'] = Performative(data['performative'])
        if data.get('conversation_id'):
            data['conversation_id'] = UUID(data['conversation_id'])
        if data.get('reply_by'):
            data['reply_by'] = datetime.fromisoformat(data['reply_by'])
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)

    def to_message(self) -> Message:
        """
        Converts the ACLMessage object to a Message object.
        
        Returns:
            Message: The Message object created from the ACLMessage object.
        """
        return Message(
            id=self.id,
            sender_id=self.sender_id,
            recipient_id=self.receiver_id,
            content=str(self.content),
            timestamp=self.timestamp,
            conversation_id=self.conversation_id,
            reply_to=UUID(self.in_reply_to) if self.in_reply_to else None,
            language=self.language,
            ontology=self.ontology,
            protocol=self.protocol,
            performative=self.performative
        )

    @classmethod
    def from_message(cls, message: Message) -> 'ACLMessage':
        """
        Creates an ACLMessage object from a Message object.
        
        Args:
            message (Message): The Message object to convert.
        
        Returns:
            ACLMessage: The ACLMessage object created from the Message object.
        """
        return cls(
            id=message.id,
            sender_id=message.sender_id,
            receiver_id=message.recipient_id,
            performative=message.performative,
            content=message.content,
            timestamp=message.timestamp,
            conversation_id=message.conversation_id,
            in_reply_to=str(message.reply_to) if message.reply_to else None,
            language=message.language,
            ontology=message.ontology,
            protocol=message.protocol
        )