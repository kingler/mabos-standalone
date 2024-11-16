import json
from pathlib import Path
from typing import Any, Dict, List

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

class ModelingServiceConfig(BaseModel):
    """Configuration for the modeling service"""
    enabled: bool = True
    storage_path: str = "data/models"
    cache_enabled: bool = True
    max_cache_size: int = 1000
    default_model_type: str = "agent_model"

class AgentConfig(BaseModel):
    """Configuration for agents"""
    num_agents: int = 5
    num_states: int = 10
    state_size: int = 64
    action_size: int = 32
    learning_rate: float = 0.001
    discount_factor: float = 0.99
    exploration_rate: float = 0.1

class OntologyConfig(BaseModel):
    """Configuration for ontology"""
    path: str = "data/ontologies/base_ontology.nt"  # Changed to .nt
    format: str = "nt"  # Changed to nt format
    base_uri: str = "http://example.org/ontology#"
    version: str = "1.0.0"
    cache_enabled: bool = True
    cache_path: str = "data/ontologies/cache"
    validation_enabled: bool = True
    repo_path: str = "data/ontologies/repo"

class ArangoDBConfig(BaseModel):
    host: str = "localhost"
    port: int = 8529
    database: str = "mdd_knowledge_base"
    username: str = "root"
    password: str = "yourpassword"
    collections: List[str] = [
        "knowledge_nodes",
        "knowledge_edges",
        "business_goals",
        "model_artifacts",
        "ontologies"
    ]
    graph_name: str = "knowledge_graph"
    edge_definitions: List[Dict[str, Any]] = [
        {
            "collection": "knowledge_edges",
            "from": ["knowledge_nodes"],
            "to": ["knowledge_nodes"]
        }
    ]

class Config(BaseModel):
    NAICS_CODES_PATH: str = "data/2022_naics_codes.csv"
    BUSINESS_DESCRIPTION_PATH: str = "data/business_description.md"
    INITIAL_QUESTIONS: list[str] = [
        "What is your business name?",
        "What is your business industry?",
        "What is your business size?",
    ]
    LLM_CONFIG: Dict[str, Any]
    ARANGO_CONFIG: ArangoDBConfig = Field(default_factory=ArangoDBConfig)
    MODELING_CONFIG: ModelingServiceConfig = Field(default_factory=ModelingServiceConfig)
    AGENT_CONFIG: AgentConfig = Field(default_factory=AgentConfig)
    ONTOLOGY_CONFIG: OntologyConfig = Field(default_factory=OntologyConfig)

    # ArangoDB property getters
    @property
    def ARANGO_HOST(self) -> str:
        return self.ARANGO_CONFIG.host

    @property
    def ARANGO_PORT(self) -> int:
        return self.ARANGO_CONFIG.port

    @property
    def ARANGO_DB(self) -> str:
        return self.ARANGO_CONFIG.database

    @property
    def ARANGO_DATABASE(self) -> str:  # Alias for ARANGO_DB
        return self.ARANGO_CONFIG.database

    @property
    def ARANGO_USER(self) -> str:
        return self.ARANGO_CONFIG.username

    @property
    def ARANGO_USERNAME(self) -> str:  # Alias for ARANGO_USER
        return self.ARANGO_CONFIG.username

    @property
    def ARANGO_PASSWORD(self) -> str:
        return self.ARANGO_CONFIG.password

    @property
    def ARANGO_COLLECTIONS(self) -> List[str]:
        return self.ARANGO_CONFIG.collections

    @property
    def ARANGO_GRAPH_NAME(self) -> str:
        return self.ARANGO_CONFIG.graph_name

    @property
    def ARANGO_EDGE_DEFINITIONS(self) -> List[Dict[str, Any]]:
        return self.ARANGO_CONFIG.edge_definitions

    # Modeling service property getter
    @property
    def modeling_service(self) -> ModelingServiceConfig:
        return self.MODELING_CONFIG

    # Agent configuration property getters
    @property
    def num_agents(self) -> int:
        return self.AGENT_CONFIG.num_agents

    @property
    def num_states(self) -> int:
        return self.AGENT_CONFIG.num_states

    @property
    def state_size(self) -> int:
        return self.AGENT_CONFIG.state_size

    @property
    def action_size(self) -> int:
        return self.AGENT_CONFIG.action_size

    # Ontology configuration property getters
    @property
    def ontology_path(self) -> str:
        return self.ONTOLOGY_CONFIG.path

    @property
    def ontology_format(self) -> str:
        return self.ONTOLOGY_CONFIG.format

    @property
    def ontology_base_uri(self) -> str:
        return self.ONTOLOGY_CONFIG.base_uri

    @property
    def ontology_repo_path(self) -> str:
        return self.ONTOLOGY_CONFIG.repo_path

def load_json_config(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)

def get_config() -> Config:
    base_path = Path(__file__).parent
    llm_config = load_json_config(base_path / 'llm_config.json')
    
    return Config(
        LLM_CONFIG=llm_config,
    )

CONFIG = get_config()

# Add these lines at the end of the file
LLM_CONFIG = CONFIG.LLM_CONFIG
API_KEYS = LLM_CONFIG.get('api_keys', {})

class Settings(BaseSettings):
    database_url: str
    db_username: str
    db_password: str
    db_name: str
    openai_api_key: str
    replicate_api_key: str
    groq_api_key: str
    anthropic_api_key: str
    google_ai_api_key: str
    huggingface_api_key: str
    togetherai_api_key: str
    helicone_api_key: str
    deepgram_api_key: str
    deepgram_audio_url: str
    openrouter_api_key: str
    ontology_repo_path: str = "data/ontologies/repo"  # Added this line

    class Config:
        env_file = ".env"
        extra = "ignore"  # Allow extra fields in environment variables

def get_settings() -> Settings:
    return Settings()
