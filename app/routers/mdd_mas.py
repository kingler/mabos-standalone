from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
from uuid import UUID
from app.core.mdd_mas.mdd_mas_model import Model, Agent, Goal, BusinessProcess, Communication, PerformanceMetrics, ModelRepository, DomainSpecificLanguage, BusinessSystemIntegration, ReusableComponent
from app.services.mdd_mas_services import ModelingService, AgentService, GoalService, BusinessProcessService, CommunicationService, PerformanceService, RepositoryService, DSLService, IntegrationService, ComponentService

router = APIRouter()

# Dependency injection
def get_modeling_service():
    return ModelingService()

def get_agent_service():
    return AgentService()

def get_goal_service():
    return GoalService()

def get_process_service():
    return BusinessProcessService()

def get_communication_service():
    return CommunicationService()

def get_performance_service():
    return PerformanceService()

def get_repository_service():
    return RepositoryService()

def get_dsl_service():
    return DSLService()

def get_integration_service():
    return IntegrationService()

def get_component_service():
    return ComponentService()

# Modeling routes
@router.post("/models", response_model=Model)
async def create_model(model: Model, service: ModelingService = Depends(get_modeling_service)):
    return await service.create_model(model)

@router.post("/models/{model_id}/generate", response_model=str)
async def generate_code(model_id: UUID, service: ModelingService = Depends(get_modeling_service)):
    return await service.generate_code(model_id)

@router.post("/models/{source_model_id}/transform/{target_type}", response_model=Model)
async def transform_model(source_model_id: UUID, target_type: str, service: ModelingService = Depends(get_modeling_service)):
    return await service.transform_model(source_model_id, target_type)

# Agent routes
@router.post("/agents", response_model=Agent)
async def create_agent(agent: Agent, service: AgentService = Depends(get_agent_service)):
    return await service.create_agent(agent)

@router.put("/agents/{agent_id}/beliefs", response_model=Agent)
async def update_agent_beliefs(agent_id: UUID, beliefs: Dict[str, Any], service: AgentService = Depends(get_agent_service)):
    return await service.update_agent_beliefs(agent_id, beliefs)

# Goal routes
@router.post("/goals", response_model=Goal)
async def create_goal(goal: Goal, service: GoalService = Depends(get_goal_service)):
    return await service.create_goal(goal)

@router.get("/goals/{goal_id}/decompose", response_model=List[Goal])
async def decompose_goal(goal_id: UUID, service: GoalService = Depends(get_goal_service)):
    return await service.decompose_goal(goal_id)

# Business Process routes
@router.post("/processes", response_model=BusinessProcess)
async def create_process(process: BusinessProcess, service: BusinessProcessService = Depends(get_process_service)):
    return await service.create_process(process)

# Communication routes
@router.post("/communications", status_code=204)
async def send_message(communication: Communication, service: CommunicationService = Depends(get_communication_service)):
    await service.send_message(communication)

# Performance routes
@router.get("/performance", response_model=PerformanceMetrics)
async def get_performance_metrics(service: PerformanceService = Depends(get_performance_service)):
    return await service.collect_metrics()

# Repository routes
@router.post("/repositories/{repository_id}/models", response_model=ModelRepository)
async def store_model(repository_id: UUID, model: Model, service: RepositoryService = Depends(get_repository_service)):
    return await service.store_model(repository_id, model)

# DSL routes
@router.post("/dsl/parse", response_model=Dict[str, Any])
async def parse_dsl(dsl: DomainSpecificLanguage, content: str, service: DSLService = Depends(get_dsl_service)):
    return await service.parse_dsl(dsl, content)

# Integration routes
@router.post("/integrations", response_model=BusinessSystemIntegration)
async def create_integration(integration: BusinessSystemIntegration, service: IntegrationService = Depends(get_integration_service)):
    return await service.create_integration(integration)

# Component routes
@router.post("/components", response_model=ReusableComponent)
async def create_component(component: ReusableComponent, service: ComponentService = Depends(get_component_service)):
    return await service.create_component(component)

@router.post("/components/{component_id}/apply/{model_id}", response_model=Model)
async def apply_component(component_id: UUID, model_id: UUID, service: ComponentService = Depends(get_component_service)):
    return await service.apply_component(component_id, model_id)