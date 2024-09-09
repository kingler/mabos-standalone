from pydantic_settings import BaseSettings


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