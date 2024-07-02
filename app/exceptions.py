class AgentNotFoundError(Exception):
    def __init__(self, agent_id):
        self.message = f"Agent with id {agent_id} not found"
        super().__init__(self.message)
