from typing import List, Optional
from app.models.action import Action
from app.models.agent import Agent

class ActionService:
    def __init__(self):
        self.actions: dict[str, Action] = {}

    def create_action(self, action_data: dict) -> Action:
        """
        Creates a new action with the given data.

        Args:
            action_data (dict): The data for creating the action.

        Returns:
            Action: The created action.
        """
        action = Action(**action_data)
        self.actions[action.action_id] = action
        return action

    def get_action(self, action_id: str) -> Optional[Action]:
        """
        Retrieves the action with the given action ID.

        Args:
            action_id (str): The unique identifier of the action.

        Returns:
            Optional[Action]: The action with the given ID, or None if not found.
        """
        return self.actions.get(action_id)

    def update_action(self, action_id: str, action_data: dict) -> Optional[Action]:
        """
        Updates the action with the given action ID.

        Args:
            action_id (str): The unique identifier of the action.
            action_data (dict): The updated data for the action.

        Returns:
            Optional[Action]: The updated action, or None if not found.
        """
        if action := self.get_action(action_id):
            updated_action = Action(**{**action.dict(), **action_data})
            self.actions[action_id] = updated_action
            return updated_action
        return None

    def delete_action(self, action_id: str) -> bool:
        """
        Deletes the action with the given action ID.

        Args:
            action_id (str): The unique identifier of the action.

        Returns:
            bool: True if the action was deleted, False otherwise.
        """
        if action_id in self.actions:
            del self.actions[action_id]
            return True
        return False

    def execute_action(self, action_id: str, agent: Agent) -> bool:
        """
        Executes the action with the given action ID using the specified agent.

        Args:
            action_id (str): The unique identifier of the action.
            agent (Agent): The agent executing the action.

        Returns:
            bool: True if the action was executed successfully, False otherwise.
        """
        if action := self.get_action(action_id):
            return action.execute(agent)
        return False

    def get_available_actions(self, agent: Agent) -> List[Action]:
        """
        Retrieves all actions that the given agent is capable of executing.

        Args:
            agent (Agent): The agent to check actions for.

        Returns:
            List[Action]: A list of actions the agent can execute.
        """
        return [
            action for action in self.actions.values()
            if all(capability in agent.capabilities for capability in action.required_capabilities)
        ]