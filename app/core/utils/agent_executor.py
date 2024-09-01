from app.core.models.agent.agent import Agent


class AgentExecutor:
    """
    The AgentExecutor class is responsible for executing the perceive-reason-act cycle of an agent.
    It ensures that the agent perceives its environment, reasons about its goals and beliefs, and executes actions accordingly.
    """
    
    def execute_cycle(self, agent: Agent):
        """
        Executes a single cycle of the agent's perceive-reason-act loop.

        Args:
            agent (Agent): The agent to execute the cycle for.

        Raises:
            TypeError: If the provided agent is not an instance of the Agent class.
            Exception: If an error occurs during the execution of the perceive, reason, or execute methods.
        """
        if not isinstance(agent, Agent):
            raise TypeError("The provided agent must be an instance of the Agent class.")

        try:
            agent.perceive()
            agent.reason()
            agent.execute()
        except Exception as e:
            raise Exception(f"An error occurred during the execution of the agent cycle: {str(e)}")
