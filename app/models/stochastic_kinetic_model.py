# app/core/stochastic_kinetic_model.py - 
# models state probabilities for agents using a stochastic kinetic approach
import numpy as np
from typing import List, Union

class StochasticKineticModel:
    """
    A class representing a Stochastic Kinetic Model for modeling state probabilities of agents.

    This model uses a stochastic kinetic approach to update and predict agent states based on observations.
    """

    def __init__(self, num_agents: int, num_states: int):
        """
        Initialize the StochasticKineticModel.

        Args:
            num_agents (int): The number of agents in the model.
            num_states (int): The number of possible states for each agent.

        Raises:
            ValueError: If num_agents or num_states is less than or equal to 0.
        """
        if num_agents <= 0 or num_states <= 0:
            raise ValueError("num_agents and num_states must be positive integers")

        self.num_agents = num_agents
        self.num_states = num_states
        self.state_probabilities = np.ones((num_agents, num_states)) / num_states

    def update(self, observations: List[List[float]]):
        """
        Update state probabilities based on observations.

        Args:
            observations (List[List[float]]): A list of observations for each agent and state.
                Should be a 2D list with dimensions (num_agents, num_states).

        Raises:
            ValueError: If the shape of observations doesn't match (num_agents, num_states).
        """
        if np.array(observations).shape != (self.num_agents, self.num_states):
            raise ValueError(f"Observations shape should be ({self.num_agents}, {self.num_states})")

        for agent_id, agent_obs in enumerate(observations):
            self.state_probabilities[agent_id] *= agent_obs
            
            # Avoid division by zero
            sum_probs = np.sum(self.state_probabilities[agent_id])
            if sum_probs == 0:
                self.state_probabilities[agent_id] = np.ones(self.num_states) / self.num_states
            else:
                # Normalize the probabilities for each agent
                self.state_probabilities[agent_id] /= sum_probs

    def predict_next_state(self) -> Union[int, List[int]]:
        """
        Predict the next state for each agent.

        Returns:
            Union[int, List[int]]: The predicted state(s) for the agent(s).
                Returns a single integer if there's only one agent, otherwise returns a list of integers.
        """
        predictions = np.argmax(self.state_probabilities, axis=1)
        return predictions[0] if self.num_agents == 1 else predictions.tolist()

    def get_state_probabilities(self) -> np.ndarray:
        """
        Get the current state probabilities for all agents.

        Returns:
            np.ndarray: A 2D numpy array of state probabilities with shape (num_agents, num_states).
        """
        return self.state_probabilities.copy()