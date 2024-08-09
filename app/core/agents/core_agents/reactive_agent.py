from typing import List, Dict, Any
from pydantic import Field
from app.core.models.agent.agent import Agent

class ReactiveAgent(Agent):
    """
    A reactive agent that responds to stimuli based on predefined rules.

    Attributes:
        stimulus_response_rules (List[Dict[str, Any]]): List of stimulus-response rules.
    """
    stimulus_response_rules: List[Dict[str, Any]] = Field(default_factory=list, description="List of stimulus-response rules")

    def add_rule(self, stimulus: str, response: str):
        """
        Add a new stimulus-response rule.

        Args:
            stimulus (str): The stimulus that triggers the rule.
            response (str): The response action to be executed.
        """
        self.stimulus_response_rules.append({"stimulus": stimulus, "response": response})

    def perceive(self):
        """
        Perceive the environment and react based on stimulus-response rules.
        """
        for belief in self.beliefs:
            for rule in self.stimulus_response_rules:
                if rule["stimulus"] in belief.description:
                    if self.can_execute_action(rule["response"]):
                        self.execute_action(rule["response"])
                        break  # Stop after executing the highest priority matching rule
                    else:
                        print(f"Cannot execute action: {rule['response']}. Insufficient resources.")

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
        for resource, required_amount in action_requirements.items():
            if resource not in self.resources or self.resources[resource] < required_amount:
                return False
        return True

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
