# Codebase Summary

## Project Structure Overview

MABOS (Multi-Agent Business Operating System) is organized into several key components:

### Core Components

1. **Multi-Agent System Core** (`app/agents/`)
   - Base agent architecture
   - Core agent types (OnboardingAgent, LLMAgent)
   - Agent communication protocols

2. **Services Layer** (`app/services/`)
   - Agent Services
     - `agent_service.py` - Core agent management
     - `agent_communication_service.py` - Inter-agent communication
     - `agent_role_service.py` - Agent role management
   
   - Business Modeling
     - `business_model_service.py` - Business model generation
     - `business_onboarding.py` - Business onboarding process
     - `business_plan_service.py` - Business planning
   
   - Enterprise Architecture
     - `togaf_mdd_services.py` - TOGAF methodology integration
     - `archimate_service.py` - ArchiMate modeling
     - `tropos_mdd_services.py` - Tropos goal modeling
   
   - Knowledge Management
     - `knowledge_base_service.py` - Knowledge base operations
     - `ontology_service.py` - Ontology management
     - `topic_map_service.py` - Topic mapping
   
   - Planning & Execution
     - `planning_service.py` - Plan generation
     - `intention_service.py` - Intention management
     - `task_manager.py` - Task execution
   
   - Integration Services
     - `mdd_mas_integration.py` - Model-driven development integration
     - `erp_service.py` - ERP system integration

3. **Database Layer** (`app/db/`)
   - ArangoDB integration
   - Database schema management
   - Data persistence

### Key Interactions

1. **Business Onboarding Flow**
   - OnboardingAgent coordinates with LLMAgent
   - Question-based information gathering
   - Model generation and validation
   - Enterprise architecture alignment

2. **Model Generation Pipeline**
   - Business model creation
   - TOGAF methodology application
   - ArchiMate model generation
   - Tropos goal modeling
   - BPMN process modeling

3. **Agent Coordination**
   - Inter-agent communication protocols
   - Role-based task distribution
   - Knowledge sharing mechanisms
   - Goal-driven collaboration

## Data Flow

1. **Input Processing**
   - Business requirements gathering
   - Natural language processing
   - Knowledge extraction

2. **Model Generation**
   - Business model creation
   - Enterprise architecture modeling
   - Process modeling
   - Goal modeling

3. **System Integration**
   - ERP system integration
   - External system connectivity
   - Data synchronization

## Recent Changes

1. **Core Framework**
   - Enhanced agent communication
   - Improved model generation
   - Extended ontology support

2. **Integration Layer**
   - Added ERP integration capabilities
   - Enhanced external system connectivity
   - Improved data synchronization

3. **Knowledge Management**
   - Enhanced ontology management
   - Improved topic mapping
   - Extended knowledge base capabilities

## External Dependencies

1. **Core Dependencies**
   - FastAPI & Flask for API development
   - ArangoDB for data storage
   - OpenAI & Anthropic for LLM capabilities
   - PyTorch & Transformers for NLP

2. **Modeling Tools**
   - owlready2 for ontology management
   - rdflib for RDF graph manipulation
   - networkx for graph operations
   - plantuml for UML diagrams

3. **Business Logic**
   - business-rule-engine
   - durable-rules
   - z3-solver for constraints

## Development Guidelines

1. **Code Organization**
   - Modular service architecture
   - Clear separation of concerns
   - Dependency injection pattern
   - Event-driven communication

2. **Testing Strategy**
   - Unit tests for services
   - Integration tests for workflows
   - End-to-end testing for critical paths

3. **Documentation**
   - Inline code documentation
   - API documentation
   - Architecture documentation
   - User guides

## Future Development

1. **Planned Enhancements**
   - Advanced agent coordination
   - Enhanced model validation
   - Improved performance monitoring
   - Extended integration capabilities

2. **Technical Debt**
   - Service layer optimization
   - Test coverage improvement
   - Documentation updates
   - Code refactoring opportunities

3. **Integration Points**
   - External system APIs
   - Enterprise software connectivity
   - Cloud service integration
   - Data import/export capabilities
