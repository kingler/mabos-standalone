
from pydantic import BaseModel


class InferenceResult(BaseModel):
    conclusion: str
    confidence: float
    explanation: str