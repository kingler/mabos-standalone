"""
This module provides different types of agents for the MABOS system, following the BDI (Belief-Desire-Intention) architecture.

Agents:
    - Agent: Base class for all agents.
    - EnvironmentalAgent: An agent that interacts with the environment.
    - ProactiveAgent: An agent that proactively pursues its goals.
    - ReactiveAgent: An agent that reacts to changes in the environment.
"""

from typing import List, Dict, Any
from pydantic import BaseModel, Field
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.llm_manager import LLMManager
from app.models.agent.belief import Belief
from app.models.agent.desire import Desire
from app.models.agent.intention import Intention

class Agent(BaseModel):
    """
    Base class for all agents in the system, incorporating BDI components.

    Attributes:
        agent_id (str): Unique identifier for the agent.
        name (str): Name of the agent.
        beliefs (List[Belief]): Current beliefs of the agent.
        desires (List[Desire]): Current desires of the agent.
        intentions (List[Intention]): Current intentions of the agent.
        reasoning_engine (ReasoningEngine): Engine for performing reasoning tasks.
        llm_manager (LLMManager): Manager for interacting with language models.
    """
    agent_id: str = Field(..., description="Unique identifier for the agent")
    name: str = Field(..., description="Name of the agent")
    beliefs: List[Belief] = Field(default_factory=list, description="Current beliefs of the agent")
    desires: List[Desire] = Field(default_factory=list, description="Current desires of the agent")
    intentions: List[Intention] = Field(default_factory=list, description="Current intentions of the agent")
    reasoning_engine: ReasoningEngine = Field(default_factory=ReasoningEngine)
    llm_manager: LLMManager = Field(default_factory=LLMManager)

    def act(self) -> None:
        """
        Perform the agent's main action. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'act' method")

    async def reason(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform reasoning based on the given context.

        Args:
            context (Dict[str, Any]): The context for reasoning.

        Returns:
            Dict[str, Any]: The result of the reasoning process.
        """
        return await self.reasoning_engine.reason(context)

    async def generate_text(self, prompt: str) -> str:
        """
        Generate text using the LLM manager.

        Args:
            prompt (str): The prompt for text generation.

        Returns:
            str: The generated text.
        """
        return await self.llm_manager.generate_text(prompt)

    def update_beliefs(self, new_beliefs: List[Belief]):
        """
        Update the agent's beliefs.

        Args:
            new_beliefs (List[Belief]): New beliefs to be added or updated.
        """
        for new_belief in new_beliefs:
            existing_belief = next((b for b in self.beliefs if b.key == new_belief.key), None)
            if existing_belief:
                existing_belief.value = new_belief.value
                existing_belief.certainty = new_belief.certainty
            else:
                self.beliefs.append(new_belief)

    def update_desires(self, new_desires: List[Desire]):
        """
        Update the agent's desires.

        Args:
            new_desires (List[Desire]): New desires to be added or updated.
        """
        for new_desire in new_desires:
            existing_desire = next((d for d in self.desires if d.id == new_desire.id), None)
            if existing_desire:
                existing_desire.priority = new_desire.priority
            else:
                self.desires.append(new_desire)

    def update_intentions(self, new_intentions: List[Intention]):
        """
        Update the agent's intentions.

        Args:
            new_intentions (List[Intention]): New intentions to be added or updated.
        """
        for new_intention in new_intentions:
            existing_intention = next((i for i in self.intentions if i.id == new_intention.id), None)
            if existing_intention:
                existing_intention.status = new_intention.status
            else:
                self.intentions.append(new_intention)

class EnvironmentalAgent(Agent):
    """
    An agent that interacts with and perceives the environment.

    Attributes:
        environment_state (Dict[str, Any]): The current state of the environment as perceived by the agent.
    """
    environment_state: Dict[str, Any] = Field(default_factory=dict, description="Current state of the environment")

    def perceive(self) -> None:
        """
        Update the agent's perception of the environment and beliefs.
        """
        raise NotImplementedError("Subclass must implement the 'perceive' method")

class ProactiveAgent(Agent):
    """
    A goal-oriented agent capable of planning and executing actions to achieve its goals.

    Attributes:
        goals (List[str]): List of the agent's current goals.
        plans (List[Dict[str, Any]]): List of the agent's current plans.
    """
    goals: List[str] = Field(default_factory=list, description="List of agent's current goals")
    plans: List[Dict[str, Any]] = Field(default_factory=list, description="List of agent's current plans")

    def plan(self) -> None:
        """
        Generate plans to achieve the agent's goals based on beliefs, desires, and intentions.
        """
        raise NotImplementedError("Subclass must implement the 'plan' method")

    def deliberate(self) -> None:
        """
        Deliberate on current beliefs and desires to form intentions.
        """
        raise NotImplementedError("Subclass must implement the 'deliberate' method")

class ReactiveAgent(Agent):
    """
    An agent that responds to stimuli based on predefined rules.

    Attributes:
        rules (Dict[str, str]): Dictionary of stimulus-response rules.
    """
    rules: Dict[str, str] = Field(default_factory=dict, description="Dictionary of stimulus-response rules")

    def react(self, stimulus: str) -> str:
        """
        React to a given stimulus based on the agent's rules and current beliefs.

        Args:
            stimulus (str): The incoming stimulus.

        Returns:
            str: The agent's response to the stimulus.
        """
        return self.rules.get(stimulus, "No reaction")

class AgentType(BaseModel):
    """
    Represents a type of agent with its characteristics.

    Attributes:
        name (str): Name of the agent type.
        description (str): Description of the agent type.
        use_cases (List[str]): List of use cases for this agent type.
    """
    name: str = Field(..., description="Name of the agent type")
    description: str = Field(..., description="Description of the agent type")
    use_cases: List[str] = Field(default_factory=list, description="List of use cases for this agent type")

__all__ = ['Agent', 'EnvironmentalAgent', 'ProactiveAgent', 'ReactiveAgent', 'AgentType']
