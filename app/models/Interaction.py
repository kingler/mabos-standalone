from pydantic import BaseModel
from typing import List
from.message import Message


class Interaction(BaseModel):
    participants: List[str]
    messages: List[Message]