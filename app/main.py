import sys
import os
import asyncio
import re
import logging
from urllib.parse import quote

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends
from arango import ArangoClient

from app.api.routers import (actions, agents, communication, goals,
                            knowledge_bases, mas_router, planning, plans,
                            tasks, version_control, world_model_router)
from app.api.routers.mdd_mas import router as mdd_router
from app.api.routers.togaf_mdd import router as togaf_router
from app.api.routers.tropos_mdd import router as tropos_router
from app.models.system.world_model import WorldModel
from app.models.system.world_model_provider import get_world_model
from app.services.agent_service import AgentService
from app.services.world_model_service import WorldModelService
from app.config.config import get_settings
from app.db.arango_db_client import ArangoDBClient

logging.basicConfig(level=logging.INFO)
app = FastAPI()
settings = get_settings()

print("Settings loaded:")
print(f"DATABASE_URL: {settings.database_url}")
print(f"DB_USERNAME: {settings.db_username}")
print(f"DB_PASSWORD: {'*' * len(settings.db_password)}")  # Don't print the actual password
print(f"DB_NAME: {settings.db_name}")

def construct_database_url(username, password, host, port, db_name):
    return f"http://{quote(username)}:{quote(password)}@{host}:{port}/{db_name}"

def validate_database_url(url: str):
    pattern = re.compile(r'^http://.*:.*@.*:\d+/.*$')
    if not pattern.match(url):
        print(f"URL validation failed for: {url}")
        raise ValueError("Invalid database URL format. Expected format: http://username:password@host:port/database")
    print(f"URL validation passed for: {url}")

try:
    # Extract host and port from DATABASE_URL
    url_parts = settings.database_url.split('//')
    if len(url_parts) != 2:
        raise ValueError(f"Invalid DATABASE_URL format: {settings.database_url}")
    
    host_port = url_parts[1].split(':')
    if len(host_port) != 2:
        raise ValueError(f"Invalid host:port format in DATABASE_URL: {url_parts[1]}")
    
    host, port = host_port

    database_url = construct_database_url(
        username=settings.db_username,
        password=settings.db_password,
        host=host,
        port=port,
        db_name=settings.db_name
    )

    validate_database_url(database_url)
except ValueError as e:
    print(f"Error: {str(e)}")
    sys.exit(1)

# Parse the database URL
if match := re.match(r'^http://(.*?):(.*?)@(.*?):(\d+)/(.*)$', database_url):
    username, password, host, port, db_name = match.groups()
    print("Successfully parsed database URL")
else:
    print(f"Failed to parse the constructed database URL: {database_url}")
    raise ValueError("Failed to parse the constructed database URL")

# Connect to ArangoDB
print(f"Attempting to connect to ArangoDB at http://{host}:{port}")
client = ArangoClient(hosts=f"http://{host}:{port}")
try:
    db = client.db(db_name, username=username, password=password)
    print("Successfully connected to ArangoDB")
except Exception as e:
    print(f"Failed to connect to ArangoDB: {str(e)}")
    raise

async def initialize_world_model():
    try:
        return await WorldModel.create()
    except Exception as e:
        logging.error(f"Failed to initialize WorldModel: {str(e)}")
        raise # Use the factory method

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
app.include_router(mdd_router, prefix="/api/v1/mdd", tags=["MDD"])
app.include_router(togaf_router, prefix="/api/v1/togaf", tags=["TOGAF"])
app.include_router(tropos_router, prefix="/api/v1/tropos", tags=["Tropos"])

# Dependency to get the WorldModel
async def get_world_model_dependency():
    return await get_world_model()

# Dependency to get the AgentService
async def get_agent_service():
    return await AgentService.get_instance()

# Dependency to get the WorldModelService
async def get_world_model_service():
    return await WorldModelService.get_instance()

@app.on_event("startup")
async def startup_event():
    arango_client = ArangoDBClient(
        url=settings.database_url,
        username=settings.db_username,
        password=settings.db_password
    )
    arango_client.connect()
    app.state.arango_client = arango_client

@app.on_event("shutdown")
async def shutdown_event():
    
    # Implement any necessary cleanup
    agent_service = app.state.agent_service
    world_model_service = app.state.world_model_service

    # Perform cleanup for agent_service
    await agent_service.cleanup()

    # Perform cleanup for world_model_service
    await world_model_service.cleanup()

if __name__ == "__main__":
    asyncio.run(initialize_world_model())