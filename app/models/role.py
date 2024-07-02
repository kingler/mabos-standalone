from pydantic import BaseModel
from typing import List


class Role(BaseModel):
    name: str
    responsibilities: List[str]