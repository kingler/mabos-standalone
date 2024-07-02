from pydantic import BaseModel
from typing import List

from .role import Role
from .agent import Agent



class Organization(BaseModel):
    name: str
    roles: List[Role]
    agents: List['Agent']
    norms: List[str]