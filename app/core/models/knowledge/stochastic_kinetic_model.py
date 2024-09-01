# app/core/stochastic_kinetic_model.py - 
# models state probabilities for agents using a stochastic kinetic approach
import numpy as np


class StochasticKineticModel:
    def __init__(self, num_agents, num_states):
        self.num_agents = num_agents
        self.num_states = num_states
        self.state_probabilities = np.ones((num_agents, num_states)) / num_states

    def update(self, observations):
        # Update state probabilities based on observations
        for agent_id, agent_obs in enumerate(observations):
            for state_id, state_obs in enumerate(agent_obs):
                self.state_probabilities[agent_id][state_id] *= state_obs
            
            # Normalize the probabilities for each agent
            self.state_probabilities[agent_id] /= np.sum(self.state_probabilities[agent_id])

    def predict_next_state(self):
        # Predict the next state for each agent
        return np.argmax(self.state_probabilities, axis=1)