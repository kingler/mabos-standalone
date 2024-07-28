from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    """
    Configuration settings for the application.

    Attributes:
        openai_api_key (str): The API key for OpenAI services.
        num_agents (int): The number of agents in the system.
        num_states (int): The number of states in the environment.
        state_size (int): The size of each state representation.
        action_size (int): The size of the action space.
        ontology_path (str): The path to the ontology file.
    """
    openai_api_key: str = ""
    num_agents: int = 10
    num_states: int = 5
    state_size: int = 10
    action_size: int = 5
    ontology_path: str = os.path.join(os.path.dirname(__file__), "ontologies", "mabos.owl")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

def get_settings() -> Settings:
    """
    Retrieve the application settings.

    Returns:
        Settings: An instance of the Settings class.
    """
    return Settings()

# Create a global instance of Settings
settings: Optional[Settings] = None

def initialize_settings():
    """
    Initialize the global settings instance.
    """
    global settings
    settings = get_settings()

# Initialize settings when the module is imported
initialize_settings()