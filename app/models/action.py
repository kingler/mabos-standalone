from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from .agent import Agent

class Action(BaseModel):
    """
    Represents an action that can be executed by an agent.

    Attributes:
        action_id (str): The unique identifier of the action.
        description (str): A description of the action.
        preconditions (Dict[str, Any]): Conditions that must be met before the action can be executed.
        effects (Dict[str, Any]): The expected outcomes of the action.
        required_capabilities (List[str]): Capabilities required by an agent to perform this action.
    """

    action_id: str = Field(..., description="The unique identifier of the action")
    description: str = Field(..., description="A description of the action")
    preconditions: Dict[str, Any] = Field(default_factory=dict, description="Conditions that must be met before the action can be executed")
    effects: Dict[str, Any] = Field(default_factory=dict, description="The expected outcomes of the action")
    required_capabilities: list[str] = Field(default_factory=list, description="Capabilities required by an agent to perform this action")
    status: str = Field(default="pending", description="The current status of the action")
    dify_tool_id: Optional[str] = Field(default=None, description="Optional mapping to Dify tool ID")
    dify_tool: Optional[Any] = Field(default=None, description="Optional reference to the actual Dify Tool object")

    def execute(self, agent: Agent) -> bool:
        """
        Executes the action based on the agent's beliefs and knowledge.

        Args:
            agent (Agent): The agent executing the action.

        Returns:
            bool: True if the action was executed successfully, False otherwise.
        """
        if not self._check_preconditions(agent):
            print(f"Action {self.action_id} cannot be executed due to unmet preconditions")
            return False

        if not self._check_capabilities(agent):
            print(f"Agent {agent.agent_id} lacks the required capabilities for action {self.action_id}")
            return False

        # Perform the action
        print(f"Executing action {self.action_id} for agent {agent.agent_id}")
        
        # Update agent's state or environment as needed
        self._apply_effects(agent)
        
        self.status = "completed"
        return True

    def _check_preconditions(self, agent: Agent) -> bool:
        """
        Checks if the preconditions for the action are met.

        Args:
            agent (Agent): The agent executing the action.

        Returns:
            bool: True if all preconditions are met, False otherwise.
        """
        for condition, value in self.preconditions.items():
            if not agent.check_belief(condition, value):
                return False
        return True

    def _check_capabilities(self, agent: Agent) -> bool:
        """
        Checks if the agent has the required capabilities for the action.

        Args:
            agent (Agent): The agent executing the action.

        Returns:
            bool: True if the agent has all required capabilities, False otherwise.
        """
        return all(capability in agent.capabilities for capability in self.required_capabilities)

    def _apply_effects(self, agent: Agent) -> None:
        """
        Applies the effects of the action to the agent's state.

        Args:
            agent (Agent): The agent executing the action.
        """
        for effect, value in self.effects.items():
            agent.update_belief(effect, value)

    def get_failure_reason(self) -> str:
        """
        Returns the reason for action failure if the action failed.

        Returns:
            str: The reason for action failure, or None if the action didn't fail.
        """
        if self.status != "completed":
            return f"Action {self.action_id} failed or was not executed"
        return None