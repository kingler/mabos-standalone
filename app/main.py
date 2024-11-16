import sys
import os
import asyncio
import re
import logging
from urllib.parse import quote
from datetime import datetime, timedelta, timezone

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional
from arango import ArangoClient
from fastapi_socketio import SocketManager

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

# Add this at the beginning of your file or before you use fake_users_db
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": get_password_hash("secret"),  # Use your actual password hashing function
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False,
    },
    # Add more users if necessary
}

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])
logger = logging.getLogger(__name__)

app = FastAPI()
socket_manager = SocketManager(app=app)
settings = get_settings()

# Authentication settings
SECRET_KEY = "YOUR_SECRET_KEY"  # Replace with a secure secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if user and verify_password(password, user.hashed_password):
        return user
    return False

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def construct_database_url(username, password, host, port, db_name):
    return f"http://{quote(username)}:{quote(password)}@{host}:{port}/{db_name}"

def validate_database_url(url: str):
    pattern = re.compile(r'^http://.*:.*@.*:\d+/.*$')
    if not pattern.match(url):
        logger.error(f"URL validation failed for: {url}")
        raise ValueError("Invalid database URL format. Expected format: http://username:password@host:port/database")
    logger.info(f"URL validation passed for: {url}")

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
    logger.error(f"Error: {str(e)}")
    sys.exit(1)

# Parse the database URL
if match := re.match(r'^http://(.*?):(.*?)@(.*?):(\d+)/(.*)$', database_url):
    username, password, host, port, db_name = match.groups()
    logger.info("Successfully parsed database URL")
else:
    logger.error(f"Failed to parse the constructed database URL: {database_url}")
    raise ValueError("Failed to parse the constructed database URL")

# Connect to ArangoDB
logger.info(f"Attempting to connect to ArangoDB at http://{host}:{port}")
client = ArangoClient(hosts=f"http://{host}:{port}")
try:
    db = client.db(db_name, username=username, password=password)
    logger.info("Successfully connected to ArangoDB")
except Exception as e:
    logger.error(f"Failed to connect to ArangoDB: {str(e)}")
    raise

async def initialize_world_model():
    try:
        return await WorldModel.create()
    except Exception as e:
        logger.error(f"Failed to initialize WorldModel: {str(e)}")
        raise

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
app.include_router(business_goals.router, prefix="/api", tags=["business_goals"])

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
    try:
        arango_client = ArangoDBClient(
            url=settings.database_url,
            username=settings.db_username,
            password=settings.db_password
        )
        arango_client.connect()
        app.state.arango_client = arango_client
        logger.info("Successfully initialized ArangoDB client")
    except Exception as e:
        logger.error(f"Failed to initialize ArangoDB client: {str(e)}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    try:
        # Implement any necessary cleanup
        agent_service = app.state.agent_service
        world_model_service = app.state.world_model_service

        # Perform cleanup for agent_service
        await agent_service.cleanup()

        # Perform cleanup for world_model_service
        await world_model_service.cleanup()

        logger.info("Successfully performed cleanup operations")
    except Exception as e:
        logger.error(f"Error during shutdown cleanup: {str(e)}")

@socket_manager.on('connect')
async def handle_connect(sid, environ):
    logger.info(f"Client connected: {sid}")

@socket_manager.on('disconnect')
async def handle_disconnect(sid):
    logger.info(f"Client disconnected: {sid}")

@socket_manager.on('message')
async def handle_message(sid, data):
    logger.info(f"Received message from {sid}: {data}")
    # Process the message and update the world model or agent states as necessary
    # You may want to use the world_model_service or agent_service here

if __name__ == "__main__":
    asyncio.run(initialize_world_model())