# app/core/fnrl.py -- Federated Neural Reinforcement Learning model 
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from typing import List, Union

class FNRL:
    """
    Federated Neural Reinforcement Learning model.
    
    This class implements a federated learning approach for reinforcement learning
    using pre-trained language models.
    """

    def __init__(self, num_agents: int, model_name: str = "distilbert-base-uncased"):
        """
        Initialize the FNRL model.

        Args:
            num_agents (int): Number of agents in the federated learning setup.
            model_name (str): Name of the pre-trained model to use. Defaults to "distilbert-base-uncased".
        """
        self.num_agents = num_agents
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.models = [AutoModelForSequenceClassification.from_pretrained(model_name) for _ in range(num_agents)]
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        for model in self.models:
            model.to(self.device)

    def train(self, agent_id: int, states: List[str], actions: List[int]):
        """
        Train the model for a specific agent.

        Args:
            agent_id (int): ID of the agent to train.
            states (List[str]): List of state descriptions.
            actions (List[int]): List of corresponding actions.

        Raises:
            ValueError: If agent_id is out of range or if states and actions have different lengths.
        """
        if agent_id < 0 or agent_id >= self.num_agents:
            raise ValueError(f"Invalid agent_id. Must be between 0 and {self.num_agents - 1}")
        
        if len(states) != len(actions):
            raise ValueError("The number of states must match the number of actions")

        model = self.models[agent_id]
        model.train()
        
        inputs = self.tokenizer(states, return_tensors="pt", padding=True, truncation=True).to(self.device)
        labels = torch.tensor(actions).to(self.device)
        
        optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
        
        outputs = model(**inputs, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    def predict(self, agent_id: int, state: Union[str, List[str]]) -> np.ndarray:
        """
        Predict action probabilities for a given state.

        Args:
            agent_id (int): ID of the agent to use for prediction.
            state (Union[str, List[str]]): State description(s) to predict for.

        Returns:
            np.ndarray: Predicted action probabilities.

        Raises:
            ValueError: If agent_id is out of range.
        """
        if agent_id < 0 or agent_id >= self.num_agents:
            raise ValueError(f"Invalid agent_id. Must be between 0 and {self.num_agents - 1}")

        model = self.models[agent_id]
        model.eval()
        
        inputs = self.tokenizer(state, return_tensors="pt", padding=True, truncation=True).to(self.device)
        
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
        
        return torch.softmax(logits, dim=-1).cpu().numpy()

    def aggregate_models(self):
        """
        Aggregate the models from all agents using federated averaging.

        This method should be called periodically to perform federated learning.
        """
        # Initialize a dictionary to store the averaged state_dict
        averaged_state_dict = {}

        # Iterate through all model parameters
        for key in self.models[0].state_dict().keys():
            # Stack the same parameter from all models
            stacked_params = torch.stack([model.state_dict()[key].float() for model in self.models])
            # Compute the average
            averaged_state_dict[key] = torch.mean(stacked_params, dim=0).to(self.models[0].state_dict()[key].dtype)

        # Update all models with the averaged parameters
        for model in self.models:
            model.load_state_dict(averaged_state_dict)

        print("Models aggregated successfully.")
