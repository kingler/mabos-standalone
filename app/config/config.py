import json
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel
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

# Ensure this function is defined and exported
def get_settings():
    return Settings()
