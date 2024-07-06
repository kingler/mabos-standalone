from durable.lang import *
from .agent import Agent

class BusinessAgent(Agent):
    def __init__(self):
        self.beliefs = {}
        self.desires = []
        self.intentions = []

    def update_belief(self, key, value):
        self.beliefs[key] = value

    def add_desire(self, desire):
        self.desires.append(desire)

    def set_intention(self, intention):
        self.intentions.append(intention)

    def act(self):
        for intention in self.intentions:
            if intention == 'process_orders':
                for order_id in self.beliefs.get('pending_orders', []):
                    post('business', {'subject': 'order', 'action': 'process', 'order_id': order_id})

# Define the ruleset
with ruleset('business'):
    # Rule for processing an order
    @when_all(m.subject == 'order' & m.action == 'process')
    def process_order(c):
        print(f"Processing order {c.m.order_id}")
        c.assert_fact({'subject': 'order', 'action': 'complete', 'order_id': c.m.order_id})

    # Rule for completing an order
    @when_all(m.subject == 'order' & m.action == 'complete')
    def complete_order(c):
        print(f"Order {c.m.order_id} has been completed")

# Function to simulate an agent's action
def agent_action(action, order_id):
    post('business', {'subject': 'order', 'action': action, 'order_id': order_id})

# Create an agent
agent = BusinessAgent()

# Update agent's beliefs
agent.update_belief('pending_orders', [1, 2, 3])

# Set agent's desires and intentions
agent.add_desire('process_all_orders')
agent.set_intention('process_orders')

# Agent acts based on its intentions
agent.act()

# Wait for a moment to allow rules to be processed
import time
time.sleep(1)