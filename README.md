# Multi-Agent System (MAS) Framework for Business Development and Operations

## Overview

This Multi-Agent System (MAS) Framework is a sophisticated platform designed for developing complex, goal-oriented, BDI (Belief-Desire-Intention) multi-agent systems. It's specifically tailored for business applications, including business development, operations, intelligence, and performance management.

The framework incorporates advanced features such as:
- Agent Communication Language (ACL) for structured inter-agent communication
- Large Language Model (LLM) integration for natural language processing and human-agent interaction
- Knowledge representation and reasoning capabilities
- Goal management and planning
- Belief revision and update mechanisms
- Environmental, Proactive, and Reactive agent types for comprehensive system behavior

## Key Components

### 1. Agents

Agents are the core entities in the system. Each agent has:
- Beliefs: The agent's understanding of the world
- Desires: The agent's goals
- Intentions: The agent's committed plans to achieve its goals

Our framework supports three main types of agents:

#### a. Environmental Agents
- **Role**: Manage and monitor the environment in which other agents operate.
- **Functions**:
  - Context Provision: Gather and disseminate information about the current state of the environment.
  - State Monitoring: Continuously monitor for changes and update other agents.
  - Facilitating Interaction: Provide a shared context for agent coordination.

#### b. Proactive Agents
- **Role**: Take initiative and act in anticipation of future goals or problems.
- **Functions**:
  - Goal Pursuit: Continuously work towards achieving goals.
  - Opportunity Identification: Identify and exploit opportunities aligned with goals.
  - Long-term Planning: Engage in strategic planning for future objectives.

#### c. Reactive Agents
- **Role**: Respond to changes and events in the environment in real-time.
- **Functions**:
  - Event Handling: Respond to specific events or changes quickly.
  - Short-term Actions: Focus on immediate actions to address current situations.
  - Adaptability: Ensure the system can adapt to unexpected changes.

### 2. Communication

The framework supports two types of communication:
- Agent-to-Agent: Using ACL (Agent Communication Language)
- Agent-to-Human: Using LLMs for natural language interaction

### 3. Knowledge Management

- Knowledge Base: Stores and manages the agent's knowledge
- Ontology: Defines the structure and relationships of concepts in the domain

### 4. Planning and Reasoning

- Goal Management: Handles the creation, prioritization, and achievement of goals
- Plan Library: Stores and retrieves plans for achieving goals
- Reasoning Engine: Performs inference and decision-making based on the agent's knowledge and goals

### 5. Environment

Represents the world in which agents operate, including other agents and external systems.

## API Usage Examples

### 1. Creating Different Types of Agents

```python
from app.services.agent_service import AgentService
from app.models.agent import EnvironmentalAgent, ProactiveAgent, ReactiveAgent

agent_service = AgentService()

# Create an Environmental Agent
env_agent = EnvironmentalAgent(
    name="Market Monitor",
    capabilities=["market_analysis", "data_collection"],
    initial_beliefs={"market_state": "stable"}
)
created_env_agent = agent_service.create_agent(env_agent)

# Create a Proactive Agent
proactive_agent = ProactiveAgent(
    name="Business Strategist",
    capabilities=["trend_analysis", "strategy_formulation"],
    initial_beliefs={"long_term_goal": "market_expansion"}
)
created_proactive_agent = agent_service.create_agent(proactive_agent)

# Create a Reactive Agent
reactive_agent = ReactiveAgent(
    name="Customer Service Rep",
    capabilities=["query_handling", "issue_resolution"],
    initial_beliefs={"response_time_target": "2_minutes"}
)
created_reactive_agent = agent_service.create_agent(reactive_agent)
```

### 2. Environmental Agent Updating System State

```python
from app.services.environment_service import EnvironmentService

env_service = EnvironmentService()

new_market_data = {
    "market_trend": "growing",
    "competitor_activity": "increasing",
    "customer_demand": "high"
}

env_service.update_environment_state(created_env_agent.id, new_market_data)
```

### 3. Proactive Agent Proposing a Strategy

```python
from app.services.strategy_service import StrategyService

strategy_service = StrategyService()

new_strategy = {
    "name": "Market Expansion Initiative",
    "description": "Expand into neighboring markets to capitalize on growing demand",
    "timeline": "12_months",
    "expected_roi": 0.15
}

proposed_strategy = strategy_service.propose_strategy(created_proactive_agent.id, new_strategy)
```

### 4. Reactive Agent Handling a Customer Query

```python
from app.services.customer_service import CustomerServiceHandler

cs_handler = CustomerServiceHandler()

customer_query = {
    "customer_id": "CUST123",
    "query_type": "product_information",
    "product_id": "PROD456"
}

response = cs_handler.handle_customer_query(created_reactive_agent.id, customer_query)
```

### 5. Inter-Agent Communication

```python
from app.services.agent_communication_service import AgentCommunicationService
from app.models.message import Performative

comm_service = AgentCommunicationService()

# Environmental Agent informing Proactive Agent about a market change
market_update = {
    "event": "new_competitor_entry",
    "impact": "moderate",
    "affected_markets": ["Region A", "Region B"]
}

comm_service.send_message(
    sender_id=created_env_agent.id,
    receiver_id=created_proactive_agent.id,
    performative=Performative.INFORM,
    content=market_update
)

# Proactive Agent requesting action from Reactive Agent
action_request = {
    "action": "customer_outreach",
    "target_segment": "high_value_customers",
    "message": "Inform about our competitive advantage"
}

comm_service.send_message(
    sender_id=created_proactive_agent.id,
    receiver_id=created_reactive_agent.id,
    performative=Performative.REQUEST,
    content=action_request
)
```

## Integration of Agent Types

In our BDI Multi-Agent System, the different agent types work together to achieve business objectives:

1. **Environmental Agents** (e.g., Market Monitor) continuously update the system's understanding of the business environment. They provide crucial information to both Proactive and Reactive agents.

2. **Proactive Agents** (e.g., Business Strategist) use the information from Environmental Agents to formulate long-term strategies and identify opportunities. They may issue requests to Reactive Agents for specific actions that align with these strategies.

3. **Reactive Agents** (e.g., Customer Service Rep) handle immediate tasks and respond to real-time events. They may receive strategic guidance from Proactive Agents and use context provided by Environmental Agents to inform their actions.

This integration ensures that the system can balance long-term strategic planning with immediate responsiveness, leveraging the strengths of each agent type to achieve business objectives effectively.

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/mas-framework.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```
   cp .env.example .env
   # Edit .env with your specific configurations
   ```

4. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

5. Access the API documentation:
   Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI with all available endpoints.

## Extending the Framework

To extend the framework for your specific use case:

1. Define your domain-specific ontology in `app/models/ontology.py`
2. Create custom agent types by extending the base `EnvironmentalAgent`, `ProactiveAgent`, or `ReactiveAgent` classes
3. Implement domain-specific reasoning rules in the `ReasoningEngine`
4. Develop custom plans and add them to the `PlanLibrary`
5. Integrate with external systems and data sources as needed

## Contributing

We welcome contributions to improve and extend this MAS framework. Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.