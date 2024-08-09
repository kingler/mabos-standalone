# app/models/question_models.py
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

class Question(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    category: str
    framework: str  # TOGAF, CMMI, or BMC
    text: str
    sub_category: Optional[str] = None

class Answer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    question_id: UUID
    text: str
    business_id: UUID  # To associate answers with specific businesses