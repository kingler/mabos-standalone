from app.models.agent import Agent

class AgentExecutor(Agent):
    def execute_cycle(self, agent: 'Agent'):
        """
        Executes a single cycle of the agent's perceive-reason-act loop.

        Args:
            agent (Agent): The agent to execute the cycle for.
        """
        agent.perceive()
        agent.reason()
        agent.execute()