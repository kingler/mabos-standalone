# Multi-Agent System (MAS) Framework for Business Development and Operations

## Table of Contents
1. [Overview](#overview)
2. [Key Components](#key-components)
   - [Agents](#agents)
   - [Communication](#communication)
   - [Knowledge Management](#knowledge-management)
   - [Planning and Reasoning](#planning-and-reasoning)
   - [Environment](#environment)
3. [API Usage Examples](#api-usage-examples)
   - [Creating Different Types of Agents](#creating-different-types-of-agents)
   - [Environmental Agent Updating System State](#environmental-agent-updating-system-state)
   - [Proactive Agent Proposing a Strategy](#proactive-agent-proposing-a-strategy)
   - [Reactive Agent Handling a Customer Query](#reactive-agent-handling-a-customer-query)
   - [Inter-Agent Communication](#inter-agent-communication)
   - [Model-Driven Development (MDD)](#model-driven-development-mdd)
   - [TOGAF Integration](#togaf-integration)
   - [Tropos Framework](#tropos-framework)
   - [Creating a TOGAF Enterprise Architecture](#creating-a-togaf-enterprise-architecture)
   - [Creating a Tropos Model](#creating-a-tropos-model)
   - [Generating MAS from Tropos Model](#generating-mas-from-tropos-model)
4. [Integration of Agent Types](#integration-of-agent-types)
5. [Integration of MDD, TOGAF, and Tropos](#integration-of-mdd-togaf-and-tropos)
6. [Getting Started](#getting-started)
7. [Extending the Framework](#extending-the-framework)
8. [Contributing](#contributing)
9. [License](#license)

## Overview

This Multi-Agent System (MAS) Framework is a sophisticated platform designed for developing complex, goal-oriented, BDI (Belief-Desire-Intention) multi-agent systems. It's specifically tailored for business applications, including business development, operations, intelligence, and performance management.

The framework incorporates advanced features such as:
- Agent Communication Language (ACL) for structured inter-agent communication
- Large Language Model (LLM) integration for natural language processing and human-agent interaction
- Knowledge representation and reasoning capabilities
- Goal management and planning
- Belief revision and update mechanisms
- Environmental, Proactive, and Reactive agent types for comprehensive system behavior
- Model-Driven Development (MDD) approach for system design and implementation
- Integration with TOGAF (The Open Group Architecture Framework) for enterprise architecture alignment
- Incorporation of Tropos framework for agent-oriented software development

___

### Generating Business Domain-Specific MASs
The MABOS API provides a powerful set of endpoints that can be leveraged by a conversational LLM-based BDI (Belief-Desire-Intention) agent to generate business domain-specific Multi-Agent Systems. This process involves several steps, utilizing various endpoints to create a comprehensive MAS tailored to the specific business needs. Here's an overview of how this process works:

1. Business Description Analysis
    The LLM-based agent starts by analyzing the business description provided by the user. It uses its natural language understanding capabilities to extract key information about the business domain, objectives, and requirements.

2. Domain Modeling
    Endpoint: POST /mdd/models
    The agent creates an initial domain model based on the analyzed business description.

3. TOGAF Enterprise Architecture Creation
    Endpoint: POST /togaf/enterprise-architectures
    The agent establishes a high-level enterprise architecture aligned with the business description.

4. Tropos Goal Modeling
    Endpoint: POST /tropos/models
    The agent creates a Tropos model to capture the strategic goals and actor dependencies of the business.

5. Agent Type Identification and Creation
    Endpoints:
    POST /agents/ (for each identified agent type)
    POST /agents/environmental/{agent_id}/update_state
    POST /agents/proactive/{agent_id}/propose_strategy
    POST /agents/reactive/{agent_id}/handle_event

Based on the business needs, the agent identifies and creates appropriate agent types (Environmental, Proactive, Reactive).

6. Knowledge Base Setup
    Endpoint: POST /knowledge_bases/
    The agent creates knowledge bases for each agent, populating them with domain-specific knowledge.

7. Goal Definition
    Endpoint: POST /goals/
    The agent defines specific goals for each agent based on the Tropos model and business objectives.


8. Plan Generation

    Endpoint: POST /planning/plan
    For each goal, the agent generates plans that agents can follow to achieve their objectives.


9. Action and Task Definition
    Endpoints:
    POST /actions/
    POST /tasks/

The agent defines specific actions and tasks that agents need to perform as part of their plans.

10. Communication Protocol Setup
    Endpoints:
    POST /communication/agent/subscribe
    POST /communication/agent/publish

The agent sets up appropriate communication channels and protocols between agents.

11. World Model Integration

    Endpoints:
    PUT /world/state
    POST /world/agents/{agent_id}
    POST /world/objects/{object_id}
    POST /world/relationships

    The agent integrates all components into a cohesive world model.


12. MAS Integration

    Endpoint: POST /integration/tropos-to-mas/{tropos_model_id}
    The agent generates a complete Multi-Agent System based on the Tropos model and all defined components.


13. Alignment and Validation

    Endpoints:
    POST /integration/align-tropos-togaf/{tropos_model_id}/{ea_id}
    POST /integration/align-agents/{ea_id}

    The agent ensures alignment between the generated MAS, the Tropos model, and the TOGAF enterprise architecture.


14. Code Generation

    Endpoint: POST /mdd/models/{model_id}/generate
    Finally, the agent generates executable code for the MAS based on the integrated model.


Throughout this process, the LLM-based agent uses its reasoning capabilities to make decisions about the best way to structure the MAS based on the business description. It can engage in a dialogue with the user, asking for clarifications or additional information when needed, and explaining its decisions.

The agent can also use endpoints like GET /knowledge_bases/{kb_id} to retrieve information, POST /knowledge_bases/{kb_id}/reason to perform reasoning tasks, and POST /knowledge_bases/{kb_id}/query to answer specific questions about the domain or the generated MAS.
This approach allows for the creation of highly customized, business-specific Multi-Agent Systems that are well-aligned with the organization's goals and architecture, all driven by the intelligent decision-making of the LLM-based BDI agent.

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

### 6. Model-Driven Development (MDD)

The framework now supports a comprehensive MDD approach, allowing for:
- High-level modeling of the multi-agent system
- Automatic code generation from models
- Model transformation between different abstraction levels
- Validation and verification of models

### 7. TOGAF Integration

The framework incorporates TOGAF concepts for enterprise architecture:
- Business Architecture: Aligning agent goals with business objectives
- Data Architecture: Modeling knowledge bases and information flow
- Application Architecture: Designing agent interactions and system components
- Technology Architecture: Specifying the technical environment for the MAS

### 8. Tropos Framework

Tropos concepts are integrated for agent-oriented software development:
- Actor modeling: Representing stakeholders and system actors
- Goal modeling: Capturing and analyzing system goals
- Dependency modeling: Expressing relationships between actors
- Plan modeling: Detailing how goals are achieved

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


### 6. Creating a TOGAF Enterprise Architecture

```python
from app.services.togaf_service import TOGAFService
from app.models.togaf_models import EnterpriseArchitecture, BusinessService, TechnologyService

togaf_service = TOGAFService()

# Create an Enterprise Architecture
ea = EnterpriseArchitecture(
    name="Global Expansion Architecture",
    description="Architecture for international market expansion"
)
created_ea = togaf_service.create_enterprise_architecture(ea)

# Add a Business Service
business_service = BusinessService(
    name="Market Entry Service",
    processes=["market analysis", "regulatory compliance", "local partnership establishment"],
    stakeholders=["Business Development", "Legal", "Finance"]
)
updated_ea = togaf_service.add_business_service(created_ea.id, business_service)

# Add a Technology Service
technology_service = TechnologyService(
    name="Cross-Border Transaction Platform",
    infrastructure_components=["payment gateway", "currency conversion", "fraud detection"],
    platforms=["cloud-based", "mobile-friendly"]
)
updated_ea = togaf_service.add_technology_service(created_ea.id, technology_service)
```
### 7. Creating a Tropos Model

```python
from app.services.tropos_service import TroposService
from app.models.tropos_models import TroposModel, Actor, Dependency

tropos_service = TroposService()

# Create a Tropos Model
tropos_model = TroposModel(
    name="Market Expansion Model",
    description="Agent-oriented model for market expansion strategy"
)
created_model = tropos_service.create_tropos_model(tropos_model)

# Add an Actor
business_strategist = Actor(
    name="Business Strategist",
    type="Agent",
    goals=["identify new markets", "develop entry strategies"],
    softgoals=["minimize risk", "maximize ROI"]
)
updated_model = tropos_service.add_actor(created_model.id, business_strategist)

# Add a Dependency
market_data_dependency = Dependency(
    name="Accurate Market Data",
    type="Resource",
    depender=business_strategist.id,
    dependee=market_analyst.id  # Assuming market_analyst is another actor
)
updated_model = tropos_service.add_dependency(created_model.id, market_data_dependency)
```

### 8. Generating MAS from Tropos Model

```python
from app.services.tropos_mas_integration_service import TroposMASIntegrationService

integration_service = TroposMASIntegrationService()

# Generate MAS from Tropos Model
mas = integration_service.generate_mas_from_tropos(created_model.id)
```

## Integration of MDD, TOGAF, and Tropos

The framework now provides a seamless integration between MDD, TOGAF, and Tropos:

1. **TOGAF Enterprise Architecture** provides the overall business and technology context.
2. **Tropos Models** define the agent-oriented aspects of the system within this context.
3. **MDD Approach** is used to transform high-level Tropos and TOGAF models into implementable MAS designs.
4. **Multi-Agent System** is generated and aligned with both the enterprise architecture and agent-oriented models.

This integration ensures that the resulting MAS is:
- Aligned with business goals and enterprise architecture (TOGAF)
- Designed with a focus on agent interactions and goals (Tropos)
- Consistently implemented through model transformations (MDD)

## Getting Started

. Clone the repository:
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
6. Create TOGAF models to align your MAS with enterprise architecture
7. Develop Tropos models to capture agent-oriented aspects of your system
8. Implement custom model transformations for your specific domain

___
## System Architecture Diagrams
System architecture diagrams to represent the MABOS architecture based on TOGAF, state machines, data class models, activity diagrams, sequence diagrams, and use case diagrams. I'll also highlight the knowledge management, reasoning, and inference capabilities of the MAS, illustrating the use of ontologies and knowledge graphs for knowledge representation in MAS agents.

Here's an updated section for the README with these diagrams:

## System Architecture Diagrams

### TOGAF-based Enterprise Architecture

```plantuml
@startuml MABOS Enterprise Architecture
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

title MABOS Enterprise Architecture (TOGAF-based)

Enterprise_Boundary(eb, "MABOS Enterprise") {
    System_Boundary(sb, "MABOS Platform") {
        System(mas, "Multi-Agent System", "Core system for goal-oriented agents")
        System(kb, "Knowledge Base", "Ontology and knowledge graph storage")
        System(re, "Reasoning Engine", "Inference and decision-making component")
        System(mdd, "Model-Driven Development", "Automated code generation and model transformation")
        System(togaf, "TOGAF Integration", "Enterprise architecture alignment")
        System(tropos, "Tropos Framework", "Goal-oriented requirement analysis")
    }
    
    System_Ext(ext_sys, "External Systems", "Business systems and data sources")
    Person(business_user, "Business User", "Defines goals and interacts with the system")
    
    Rel(business_user, mas, "Interacts with")
    Rel(mas, kb, "Utilizes")
    Rel(mas, re, "Uses for decision-making")
    Rel(mas, mdd, "Generates code and models")
    Rel(mas, togaf, "Aligns with")
    Rel(mas, tropos, "Defines goals using")
    Rel(mas, ext_sys, "Integrates with")
}
@enduml
```
---

### MAS State Machine

```plantuml
@startuml MAS State Machine
[*] --> Initializing
Initializing --> Ready : System initialized
Ready --> ProcessingGoal : New goal received
ProcessingGoal --> PlanningAction : Goal analyzed
PlanningAction --> ExecutingAction : Plan created
ExecutingAction --> EvaluatingResult : Action completed
EvaluatingResult --> Ready : Goal achieved
EvaluatingResult --> ProcessingGoal : Goal not achieved
Ready --> [*] : System shutdown
@enduml
```
---

### Data Class Model

```plantuml
@startuml Data Class Model
class Agent {
  +id: UUID
  +name: String
  +type: AgentType
  +beliefs: List<Belief>
  +desires: List<Desire>
  +intentions: List<Intention>
}

class Belief {
  +id: UUID
  +content: String
  +confidence: Float
}

class Desire {
  +id: UUID
  +description: String
  +priority: Int
}

class Intention {
  +id: UUID
  +goal: Goal
  +plan: Plan
}

class Goal {
  +id: UUID
  +description: String
  +status: GoalStatus
}

class Plan {
  +id: UUID
  +steps: List<Action>
}

class Action {
  +id: UUID
  +description: String
  +preconditions: List<Condition>
  +effects: List<Effect>
}

class KnowledgeBase {
  +id: UUID
  +ontology: Ontology
  +knowledgeGraph: Graph
}

Agent "1" *-- "many" Belief
Agent "1" *-- "many" Desire
Agent "1" *-- "many" Intention
Intention "1" *-- "1" Goal
Intention "1" *-- "1" Plan
Plan "1" *-- "many" Action
Agent "1" -- "1" KnowledgeBase
@enduml
```
---

### Activity Diagram: Goal Processing

```plantuml
@startuml Goal Processing Activity
start
:Receive new goal;
:Analyze goal;
if (Goal already exists?) then (yes)
  :Update existing goal;
else (no)
  :Create new goal;
endif
:Determine required actions;
:Create plan;
while (Actions remaining?)
  :Execute next action;
  :Update world state;
endwhile
:Evaluate goal achievement;
if (Goal achieved?) then (yes)
  :Mark goal as completed;
else (no)
  :Replan or adjust goal;
endif
stop
@enduml
```
---

### Sequence Diagram: Inter-Agent Communication

```plantuml
@startuml Inter-Agent Communication
actor User
participant "Agent A" as AgentA
participant "Agent B" as AgentB
participant "Knowledge Base" as KB

User -> AgentA: Submit task
activate AgentA
AgentA -> KB: Query knowledge
activate KB
KB --> AgentA: Return relevant information
deactivate KB
AgentA -> AgentA: Process information
AgentA -> AgentB: Request assistance
activate AgentB
AgentB -> KB: Query knowledge
activate KB
KB --> AgentB: Return relevant information
deactivate KB
AgentB -> AgentB: Process information
AgentB --> AgentA: Provide assistance
deactivate AgentB
AgentA -> AgentA: Complete task
AgentA --> User: Return result
deactivate AgentA
@enduml
```
---

### Use Case Diagram

```plantuml
@startuml MABOS Use Cases
left to right direction
actor "Business User" as BU
actor "Developer" as Dev
actor "System Administrator" as Admin

rectangle MABOS {
  usecase "Define Business Goals" as UC1
  usecase "Create Agents" as UC2
  usecase "Monitor System Performance" as UC3
  usecase "Manage Knowledge Base" as UC4
  usecase "Generate Code" as UC5
  usecase "Deploy Agents" as UC6
  usecase "Configure System" as UC7
}

BU --> UC1
BU --> UC3
Dev --> UC2
Dev --> UC4
Dev --> UC5
Admin --> UC6
Admin --> UC7
@enduml
