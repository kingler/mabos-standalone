from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.core.agents.core_agents.environmental_agent import EnvironmentalAgent


class EnvironmentError(Exception):
    """
    Exception class for environment-related errors.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class Environment(BaseModel):
    name: str
    description: str
    state: dict
    agents: List[EnvironmentalAgent] = []

class EnvironmentCreate(Environment):
    pass

class EnvironmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    state: Optional[dict] = None
    agents: Optional[List[EnvironmentalAgent]] = None

class Environment(Environment):
    id: UUID

