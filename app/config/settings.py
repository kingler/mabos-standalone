from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    openai_api_key: str = "OPENAI_API_KEY"
    anthropic_api_key: str = "ANTHROPIC_API_KEY"
    groq_api_key: str = "GROQ_API_KEY"
    gemini_api_key: str = "GEMINI_API_KEY"
    replicate_api_key: str = "REPLICATE_API_KEY"
    google_ai_api_key: str = "GOOGLE_AI_API_KEY"
    huggingface_api_key: str = "HUGGINGFACE_API_KEY"
    togetherai_api_key: str = "TOGETHERAI_API_KEY"
    helicone_api_key: str = "HELICONE_API_KEY"
    arango_url: str = "ARANGO_URL"
    arango_username: str = "ARANGO_USERNAME"
    arango_password: str = "ARANGO_PASSWORD"
    ontology_repo_path: str = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/repositories/ontologies"

    model_config = ConfigDict(env_file=".env", extra='allow')

def get_settings():
    return Settings()