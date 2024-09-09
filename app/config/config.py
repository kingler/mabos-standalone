import json
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from app.config.settings import Settings

class Config(BaseModel):
    NAICS_CODES_PATH: str = "data/2022_naics_codes.csv"
    BUSINESS_DESCRIPTION_PATH: str = "data/business_description.md"
    INITIAL_QUESTIONS: list[str] = [
        "What is your business name?",
        "What is your business industry?",
        "What is your business size?",
    ]
    LLM_CONFIG: Dict[str, Any]

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

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()
