from typing import Any, Dict, List
from uuid import UUID

from app.core.agents.core_agents.environmental_agent import EnvironmentalAgent
from app.core.models.system.environment import (Environment, EnvironmentCreate,
                                                EnvironmentUpdate)
from app.core.services.agent_service import AgentService


class EnvironmentService:
    def __init__(self):
        self.environments: List[Environment] = []

    def create_environment(self, environment_data: EnvironmentCreate) -> Environment:
        environment = Environment(**environment_data.dict())
        self.environments.append(environment)
        return environment

    def get_environment(self, environment_id: UUID) -> Environment:
        for environment in self.environments:
            if environment.id == environment_id:
                return environment
        return None

    def update_environment(self, environment_id: UUID, environment_data: EnvironmentUpdate) -> Environment:
        environment = self.get_environment(environment_id)
        if environment:
            for field, value in environment_data.dict(exclude_unset=True).items():
                setattr(environment, field, value)
        return environment

    def delete_environment(self, environment_id: UUID) -> bool:
        environment = self.get_environment(environment_id)
        if environment:
            self.environments.remove(environment)
            return True
        return False

    def get_environment_agents(self, environment_id: UUID) -> List[EnvironmentalAgent]:
        environment = self.get_environment(environment_id)
        if environment:
            return environment.agents
        return []

    def update_environment_agent_state(self, environment_id: UUID, agent_id: UUID, new_state: Dict[str, Any]) -> EnvironmentalAgent:
        environment = self.get_environment(environment_id)
        if environment:
            for agent in environment.agents:
                if agent.id == agent_id:
                    agent.update_environment_state(new_state)
                    agent.perceive()
                    return agent
        return None
