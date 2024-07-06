from typing import Dict, List, Optional, Any
from uuid import UUID, uuid4
from app.models.agent import Agent
from app.models.message import Message
from app.core.world_model import WorldModel

class MultiAgentSystem:
    def __init__(self, num_agents: int, num_states: int, state_size: int, action_size: int, ontology_path: str):
        self.agents: Dict[UUID, Agent] = {}
        self.message_queue: List[Message] = []
        self.world_model: WorldModel = WorldModel(
            num_agents=num_agents,
            num_states=num_states,
            state_size=state_size,
            action_size=action_size,
            ontology_path=ontology_path
        )

    def add_agent(self, agent: Agent) -> Agent:
        agent_id = uuid4()
        agent.agent_id = str(agent_id)
        self.agents[agent_id] = agent
        self.world_model.add_agent(agent_id, agent.dict())
        return agent

    def get_agent(self, agent_id: UUID) -> Optional[Agent]:
        return self.agents.get(agent_id)

    def remove_agent(self, agent_id: UUID) -> bool:
        if agent_id in self.agents:
            del self.agents[agent_id]
            del self.world_model.agents[agent_id]
            return True
        return False

    def list_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def send_message(self, sender_id: UUID, receiver_id: UUID, content: str):
        message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
        self.message_queue.append(message)

    def process_messages(self):
        for message in self.message_queue:
            receiver = self.agents.get(message.receiver_id)
            if receiver:
                receiver.receive_message(message)
        self.message_queue.clear()

    def update_world_model(self, updates: Dict[str, Any]):
        self.world_model.update_state(updates)

    def get_agent_world_view(self, agent_id: UUID) -> Dict[str, Any]:
        return self.world_model.get_agent_view(agent_id)

    def step(self):
        for agent in self.agents.values():
            agent_view = self.get_agent_world_view(agent.agent_id)
            agent.perceive(agent_view)
            agent.deliberate()
            agent.plan()
            actions = agent.execute()
            self.process_agent_actions(agent.agent_id, actions)
        self.process_messages()

    def process_agent_actions(self, agent_id: UUID, actions: List[Dict[str, Any]]):
        for action in actions:
            # Process each action and update the world model accordingly
            # This is a simplified example and should be expanded based on your specific action types
            if action['type'] == 'move':
                self.world_model.update_agent(agent_id, {'position': action['target']})
            elif action['type'] == 'interact':
                # Handle interaction with objects or other agents
                pass
            # Add more action types as needed

    def run(self, steps: int):
        for _ in range(steps):
            self.step()