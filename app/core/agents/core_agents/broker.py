from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class Broker:
    """
    A message broker that facilitates communication between agents.

    This broker keeps track of registered agents and their locations,
    and routes messages between them.

    Attributes:
        agents (Dict[str, str]): A dictionary mapping agent names to their locations.
    """

    def __init__(self):
        self.agents: Dict[str, str] = {}

    def register_agent(self, agent_name: str, location: str) -> None:
        """
        Registers an agent with the broker.

        Args:
            agent_name (str): The name of the agent.
            location (str): The location of the agent.
        """
        self.agents[agent_name] = location
        logger.info(f"Agent {agent_name} registered at location {location}")

    def unregister_agent(self, agent_name: str) -> None:
        """
        Unregisters an agent from the broker.

        Args:
            agent_name (str): The name of the agent to unregister.
        """
        if agent_name in self.agents:
            del self.agents[agent_name]
            logger.info(f"Agent {agent_name} unregistered")
        else:
            logger.warning(f"Attempted to unregister non-existent agent {agent_name}")

    def route_message(self, sender: Any, recipient: str, message: str) -> bool:
        """
        Routes a message from the sender to the recipient.

        Args:
            sender (Any): The sending agent.
            recipient (str): The name of the recipient agent.
            message (str): The message to be sent.

        Returns:
            bool: True if the message was successfully routed, False otherwise.
        """
        if recipient in self.agents:
            recipient_location = self.agents[recipient]
            logger.info(f"Routing message from {sender} to {recipient} at {recipient_location}")
            # In a real implementation, this would actually send the message
            # For now, we'll just log it
            logger.info(f"Message content: {message}")
            return True
        else:
            logger.warning(f"Recipient {recipient} not found")
            return False

    def get_agent_location(self, agent_name: str) -> str:
        """
        Gets the location of a registered agent.

        Args:
            agent_name (str): The name of the agent.

        Returns:
            str: The location of the agent, or None if the agent is not registered.
        """
        return self.agents.get(agent_name)

    def list_agents(self) -> Dict[str, str]:
        """
        Returns a dictionary of all registered agents and their locations.

        Returns:
            Dict[str, str]: A dictionary mapping agent names to their locations.
        """
        return self.agents.copy()
