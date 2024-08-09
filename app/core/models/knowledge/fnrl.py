# app/core/fnrl.py -- Federated Neural Reinforcement Learning model 
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

class FNRL:
    def __init__(self, num_agents, model_name="distilbert-base-uncased"):
        self.num_agents = num_agents
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.models = [AutoModelForSequenceClassification.from_pretrained(model_name) for _ in range(num_agents)]

    def train(self, agent_id, states, actions):
        model = self.models[agent_id]
        inputs = self.tokenizer(states, return_tensors="pt", padding=True, truncation=True)
        labels = torch.tensor(actions)
        
        optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
        loss = model(**inputs, labels=labels).loss
        loss.backward()
        optimizer.step()

    def predict(self, agent_id, state):
        model = self.models[agent_id]
        inputs = self.tokenizer(state, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        return torch.softmax(logits, dim=-1).numpy()
