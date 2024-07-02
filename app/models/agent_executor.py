from app.models.agent import Agent

class AgentExecutor:
    def execute_cycle(self, agent: 'Agent'):
        agent.perceive()
        agent.reason()
        agent.execute()