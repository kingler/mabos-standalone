from pydantic import BaseModel

class AgentNotFoundError(Exception):
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.message = f"Agent with id {agent_id} not found"
        super().__init__(self.message)

class AgentNotFoundErrorResponse(BaseModel):
    error: str
    agent_id: str

def handle_agent_not_found_error(agent_id: str) -> AgentNotFoundErrorResponse:
    error = AgentNotFoundError(agent_id)
    return AgentNotFoundErrorResponse(error=error.message, agent_id=agent_id)
