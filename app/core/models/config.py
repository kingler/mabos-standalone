from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str = ""
    num_agents: int = 10
    num_states: int = 5
    state_size: int = 10
    action_size: int = 5
    ontology_path: str = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/core/ontologies/mabos.owl"

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

def get_settings() -> Settings:
    return Settings()

settings = get_settings()