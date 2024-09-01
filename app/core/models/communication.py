import logging
from typing import Any

from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.knowledge_graph import KnowledgeGraph

logger = logging.getLogger(__name__)

class AgentCommunication:
    """
    Handles communication for an agent, including sending and receiving messages,
    and updating the agent's knowledge base and graph based on communications.

    Attributes:
        agent (Any): The agent using this communication module.
        knowledge_base (KnowledgeBase): The agent's knowledge base.
        knowledge_graph (KnowledgeGraph): The agent's knowledge graph.
    """

    def __init__(self, agent: Any, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph):
        self.agent = agent
        self.knowledge_base = knowledge_base
        self.knowledge_graph = knowledge_graph

    def send_message(self, recipient: Any, message: str) -> bool:
        """
        Sends a message to the specified recipient.

        Args:
            recipient (Any): The recipient of the message.
            message (str): The content of the message.

        Returns:
            bool: True if the message was sent successfully, False otherwise.
        """
        try:
            # In a real implementation, this would use some messaging system
            logger.info(f"Sending message to {recipient}: {message}")
            # Update knowledge base and graph
            self.knowledge_base.add_communication_record(self.agent, recipient, message)
            self.knowledge_graph.add_communication_link(self.agent, recipient)
            return True
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            return False

    def receive_message(self, sender: Any, message: str) -> None:
        """
        Processes a received message from a sender.

        Args:
            sender (Any): The sender of the message.
            message (str): The content of the message.
        """
        logger.info(f"Received message from {sender}: {message}")
        # Update knowledge base and graph
        self.knowledge_base.add_communication_record(sender, self.agent, message)
        self.knowledge_graph.add_communication_link(sender, self.agent)
        # Process the message (this would depend on the specific agent's logic)
        self.agent.process_message(sender, message)

    def broadcast_message(self, message: str, recipients: list) -> None:
        """
        Broadcasts a message to multiple recipients.

        Args:
            message (str): The content of the message.
            recipients (list): A list of recipients to send the message to.
        """
        for recipient in recipients:
            self.send_message(recipient, message)
