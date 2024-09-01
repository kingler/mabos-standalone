import sys
import os
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI

from app.api.routes import (actions, agents, communication, goals,
                            knowledge_bases, mas_router, planning, plans,
                            tasks, version_control, world_model_router)
from app.api.routes.mdd_mas import router as mdd_router
from app.api.routes.togaf_mdd import router as togaf_router
from app.api.routes.tropos_mdd import router as tropos_router
from app.core.models.system.world_model import WorldModel
from app.core.models.system.world_model_provider import get_world_model
from app.core.services.agent_service import AgentService
from app.core.services.world_model_service import WorldModelService

app = FastAPI()

# Initialize WorldModel asynchronously
async def initialize_world_model():
    return await WorldModel()

# Initialize services
async def initialize_services():
    world_model = await initialize_world_model()
    agent_service = AgentService(world_model)
    world_model_service = WorldModelService(world_model)
    return agent_service, world_model_service

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
# MDD router
app.include_router(mdd_router, prefix="/api/v1/mdd", tags=["MDD"])
# TOGAF router
app.include_router(togaf_router, prefix="/api/v1/togaf", tags=["TOGAF"])
# Tropos router
app.include_router(tropos_router, prefix="/api/v1/tropos", tags=["Tropos"])
# Dependency to get the WorldModel
def get_world_model_dependency():
    return get_world_model()

# Dependency to get the AgentService
def get_agent_service():
    return AgentService

# Dependency to get the WorldModelService
def get_world_model_service():
    return WorldModelService

async def main():
    AgentService, WorldModelService = await initialize_services()
    # Continue with the rest of your code

if __name__ == "__main__":
    import uvicorn
    asyncio.run(main())
    uvicorn.run(app, host="0.0.0.0", port=8000)