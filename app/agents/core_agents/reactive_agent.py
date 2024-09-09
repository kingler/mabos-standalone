import logging
from typing import Any, Dict, List
from app.agents.core_agents.agent_types import ReactiveAgent as BaseReactiveAgent
from app.models.agent.belief import Belief
from pydantic import Field


logger = logging.getLogger(__name__)


class ReactiveAgent(BaseReactiveAgent):
    """
    A reactive agent that responds to stimuli based on predefined rules.

    Attributes:
        stimulus_response_rules (List[Dict[str, Any]]): List of stimulus-response rules.
    """
    agent_id: str
    name: str
    api_key: str
    llm_service: str
    agent_communication_service: str
    
    class Config:
        arbitrary_types_allowed = True# Allows model creation from ORM objects
        
    def __init__(self, agent_id, name, api_key, llm_service, agent_communication_service):
        # Import Agent within the constructor or methods as needed
        from app.models.agent.agent import Agent
        super().__init__(
            agent_id=agent_id,
            name=name,
            api_key=api_key,
            llm_service=llm_service,
            agent_communication_service=agent_communication_service
        )
        self.base = Agent(agent_id, name, api_key, llm_service, agent_communication_service)
    # Rest of the class remains unchanged
    stimulus_response_rules: List[Dict[str, Any]] = Field(default_factory=list, description="List of stimulus-response rules")

    def add_rule(self, stimulus: str, response: str):
        """Add a new stimulus-response rule."""
        self.stimulus_response_rules.append({"stimulus": stimulus, "response": response})
        logger.info(f"Added new rule: stimulus '{stimulus}', response '{response}'")

    async def perceive(self):
        """Perceive the environment and react based on stimulus-response rules."""
        try:
            for belief in self.beliefs:
                for rule in self.stimulus_response_rules:
                    if rule["stimulus"] in belief.description:
                        if self.can_execute_action(rule["response"]):
                            await self.execute_action(rule["response"])
                            break
                        else:
                            logger.warning(f"Cannot execute action: {rule['response']}. Insufficient resources.")
        except Exception as e:
            logger.error(f"Error during perception: {str(e)}")

    def can_execute_action(self, action: str) -> bool:
        """
        Check if the agent has the necessary resources to execute the action.

        Args:
            action (str): The action to be executed.

        Returns:
            bool: True if the agent has sufficient resources, False otherwise.
        """
        # Check if the agent has the necessary resources to execute the action
        action_requirements = self.get_action_requirements(action)

        # Simplified check for resource sufficiency
        return all(self.resources.get(resource, 0) >= required_amount for resource, required_amount in action_requirements.items())

    def execute_action(self, action: str):
        """
        Execute a reactive action.

        Args:
            action (str): The action to be executed.
        """
        if self.can_execute_action(action):
            print(f"Executing reactive action: {action}")
            self.update_environment(action)
        else:
            print(f"Cannot execute action: {action}. Insufficient resources.")

    def update_environment(self, action: str):
        """
        Update the environment based on the executed action.

        Args:
            action (str): The executed action.
        """
        if action.startswith("Move to"):
            target_location = action.split("Move to ")[1]
            self.move_to(target_location)
        elif action.startswith("Pick up"):
            object_name = action.split("Pick up ")[1]
            self.pick_up(object_name)
        elif action.startswith("Put down"):
            object_name = action.split("Put down ")[1]
            self.put_down(object_name)
        elif action.startswith("Use"):
            tool_name = action.split("Use ")[1]
            self.use_tool(tool_name)
        elif action.startswith("Interact with"):
            entity_name = action.split("Interact with ")[1]
            self.interact_with(entity_name)
        elif action.startswith("Communicate"):
            message = action.split("Communicate ")[1]
            self.communicate(message)
        else:
            print(f"Unknown action: {action}")

    async def act(self) -> None:
        """Perform the agent's main action cycle: perceive and reason."""
        await self.perceive()
        context = self.get_current_state()
        await self.reason(context)

    def get_current_state(self) -> Dict[str, Any]:
        """Get the current state of the agent."""
        return {
            "beliefs": [belief.dict() for belief in self.beliefs],
            "desires": [desire.dict() for desire in self.desires],
            "intentions": [intention.dict() for intention in self.intentions],
            "stimulus_response_rules": self.stimulus_response_rules
        }
