from fastapi import FastAPI
from app.routers import agents, goals, plans, knowledge_bases, actions, tasks, planning, communication, mas_router, version_control, world_model_router
from app.core.world_model_provider import get_world_model
from app.core.world_model import WorldModel
from app.services.agent_service import AgentService
from app.services.world_model_service import WorldModelService

app = FastAPI()

# Initialize WorldModel
world_model = WorldModel()

# Initialize services
agent_service = AgentService(world_model)
world_model_service = WorldModelService(world_model)

# Include routers
app.include_router(agents.router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(goals.router, prefix="/api/v1/goals", tags=["goals"])
app.include_router(plans.router, prefix="/api/v1/plans", tags=["plans"])
app.include_router(knowledge_bases.router, prefix="/api/v1/knowledge_bases", tags=["knowledge_bases"])
app.include_router(actions.router, prefix="/api/v1", tags=["actions"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(planning.router, prefix="/api/v1/planning", tags=["planning"])
app.include_router(communication.router, prefix="/api/v1/communication", tags=["communication"])
app.include_router(mas_router.router, prefix="/api/v1", tags=["multi-agent system"])
app.include_router(version_control.router, prefix="/api/v1/vc", tags=["version control"])
app.include_router(world_model_router.router, prefix="/api/v1/world", tags=["world model"])

# Dependency to get the WorldModel
def get_world_model_dependency():
    return get_world_model()

# Dependency to get the AgentService
def get_agent_service():
    return agent_service

# Dependency to get the WorldModelService
def get_world_model_service():
    return world_model_service

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)