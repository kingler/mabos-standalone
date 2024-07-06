from uuid import UUID
from fastapi import FastAPI, Depends, HTTPException
from app.models.belief import Belief
from app.models.desire import Desire
from app.models.intention import Intention
from app.models.agent import Agent as ExistingAgent
from app.core.world_model import WorldModel
from app.services.agent_service import AgentService as ExistingAgentService
from app.routers import agents as existing_agent_router
from core.mdd_mas.mdd_mas_model import Model, Agent as MDDAgent, Goal
from app.services.mdd_mas_services import ModelingService, AgentService as MDDAgentService, GoalService
from app.routers.mdd_mas import router as mdd_router
from functools import lru_cache
from pydantic import Field
from typing import Dict, Any

app = FastAPI()

# Existing components
app.include_router(existing_agent_router.router, prefix="/api/v1/agents", tags=["agents"])

# MDD components
app.include_router(mdd_router, prefix="/api/v1/mdd", tags=["mdd"])

# Integration service
class IntegrationService:
    def __init__(self, existing_agent_service: ExistingAgentService, mdd_agent_service: MDDAgentService, modeling_service: ModelingService):
        self.existing_agent_service = existing_agent_service
        self.mdd_agent_service = mdd_agent_service
        self.modeling_service = modeling_service

    async def create_agent_from_model(self, model_id: UUID) -> ExistingAgent:
        # Retrieve the MDD model
        model = await self.modeling_service.get_model(model_id)
        
        # Validate the model
        if not model:
            raise HTTPException(status_code=404, detail="Model not found")
        if model.type != "BDI":
            raise HTTPException(status_code=400, detail="Invalid model type for agent creation")
        
        # Generate code from the MDD model
        code = await self.modeling_service.generate_code(model_id)
        
        # Create an MDD agent from the generated code
        mdd_agent = await self.mdd_agent_service.create_agent_from_code(code)
        
        # Convert MDD agent to existing agent format
        existing_agent = self.convert_mdd_to_existing_agent(mdd_agent)
        
        # Create the agent in the existing system
        created_agent = await self.existing_agent_service.create_agent(existing_agent)
        
        # Store the mapping between MDD model and existing agent
        await self.modeling_service.map_model_to_agent(model_id, created_agent.id)
        
        return created_agent

    def convert_mdd_to_existing_agent(self, mdd_agent: MDDAgent) -> ExistingAgent:
        return ExistingAgent(
            id=mdd_agent.id,
            name=mdd_agent.name,
            beliefs=[Belief(description=k, certainty=v) for k, v in mdd_agent.beliefs.items()],
            desires=[Desire(description=d) for d in mdd_agent.desires],
            intentions=[Intention(description=i) for i in mdd_agent.intentions]
        )

    async def update_model_from_agent(self, agent_id: UUID, model_id: UUID) -> Model:
        # Retrieve the existing agent
        existing_agent = await self.existing_agent_service.get_agent(agent_id)
        
        # Retrieve the MDD model
        model = await self.modeling_service.get_model(model_id)
        
        # Validate the agent and model
        if not existing_agent:
            raise HTTPException(status_code=404, detail="Agent not found")
        if not model:
            raise HTTPException(status_code=404, detail="Model not found")
        if model.type != "BDI":
            raise HTTPException(status_code=400, detail="Invalid model type for agent update")
        
        # Convert existing agent to MDD agent format
        mdd_agent = self.convert_existing_to_mdd_agent(existing_agent)
        
        # Update the MDD model based on the agent's current state
        updated_model = await self.modeling_service.update_model_from_agent(model_id, mdd_agent)
        
        # Validate the updated model
        await self.validate_model_consistency(updated_model, existing_agent)
        
        return updated_model

    def convert_existing_to_mdd_agent(self, existing_agent: ExistingAgent) -> MDDAgent:
        return MDDAgent(
            id=existing_agent.id,
            name=existing_agent.name,
            beliefs={b.description: b.certainty for b in existing_agent.beliefs},
            desires=[d.description for d in existing_agent.desires],
            intentions=[i.description for i in existing_agent.intentions]
        )
        
    async def validate_model_consistency(self, model: Model, agent: ExistingAgent):
        # Validate that the model and agent are consistent
        mdd_agent = self.convert_existing_to_mdd_agent(agent)
        if model.content != mdd_agent.dict(exclude_unset=True):
            raise HTTPException(status_code=400, detail="Model and agent are inconsistent")

# Dependency injection
def get_integration_service(
    existing_agent_service: ExistingAgentService = Depends(existing_agent_router.get_agent_service),
    mdd_agent_service: MDDAgentService = Depends(mdd_router.get_agent_service),
    modeling_service: ModelingService = Depends(mdd_router.get_modeling_service)
):
    return IntegrationService(existing_agent_service, mdd_agent_service, modeling_service)

# Integration routes
@app.post("/api/v1/integration/agents", response_model=ExistingAgent)
async def create_agent_from_model(model_id: UUID, service: IntegrationService = Depends(get_integration_service)):
    return await service.create_agent_from_model(model_id)

@app.put("/api/v1/integration/models/{model_id}/agents/{agent_id}", response_model=Model)
async def update_model_from_agent(model_id: UUID, agent_id: UUID, service: IntegrationService = Depends(get_integration_service)):
    return await service.update_model_from_agent(agent_id, model_id)

# Update WorldModel to include MDD models
class EnhancedWorldModel(WorldModel):
    mdd_models: Dict[UUID, Model] = Field(default_factory=dict)

    def add_mdd_model(self, model: Model):
        self.mdd_models[model.id] = model

    def update_mdd_model(self, model_id: UUID, updates: Dict[str, Any]):
        if model_id in self.mdd_models:
            updated_model = Model(**{**self.mdd_models[model_id].dict(), **updates})
            self.mdd_models[model_id] = updated_model
            
    def get_mdd_model(self, model_id: UUID) -> Model:
        return self.mdd_models.get(model_id)
        
    def delete_mdd_model(self, model_id: UUID):
        if model_id in self.mdd_models:
            del self.mdd_models[model_id]

# Update the world model provider
@lru_cache()
def get_enhanced_world_model() -> EnhancedWorldModel:
    return EnhancedWorldModel()

# Update existing services to use the enhanced world model
class EnhancedAgentService(ExistingAgentService):
    def __init__(self, world_model: EnhancedWorldModel):
        super().__init__(world_model)

    async def create_agent_with_model(self, agent: ExistingAgent, model: Model):
        created_agent = await self.create_agent(agent)
        self.world_model.add_mdd_model(model)
        return created_agent
        
    async def update_agent_from_model(self, agent_id: UUID, model: Model):
        agent = await self.get_agent(agent_id)
        if not agent:
            raise HTTPException(status_code=404, detail="Agent not found")
        
        updated_agent = ExistingAgent(
            **agent.dict(exclude_unset=True),
            beliefs=[Belief(description=k, certainty=v) for k, v in model.content["beliefs"].items()],
            desires=[Desire(description=d) for d in model.content["desires"]],
            intentions=[Intention(description=i) for i in model.content["intentions"]]
        )
        
        await self.update_agent(agent_id, updated_agent)
        self.world_model.update_mdd_model(model.id, model.dict(exclude_unset=True))
        
        return updated_agent
        
    async def delete_agent_with_model(self, agent_id: UUID, model_id: UUID):
        await self.delete_agent(agent_id)
        self.world_model.delete_mdd_model(model_id)

# Update the agent service provider
def get_enhanced_agent_service(world_model: EnhancedWorldModel = Depends(get_enhanced_world_model)):
    return EnhancedAgentService(world_model)

# Update existing routes to use the enhanced agent service
existing_agent_router.get_agent_service = get_enhanced_agent_service