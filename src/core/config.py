import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from functools import lru_cache

# Load .env file from the project root
# This ensures .env is loaded even when running scripts from subdirectories
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    RELOAD_APP: bool = True

    DATABASE_URL: str
    
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    WHATSAPP_API_TOKEN: str = ""
    WHATSAPP_VERIFY_TOKEN: str = "culturebridge_secret_verify_token"
    WHATSAPP_PHONE_NUMBER_ID: str = ""
    WHATSAPP_BUSINESS_ACCOUNT_ID: str = ""
    WHATSAPP_APP_SECRET: str = ""


    GOOGLE_APPLICATION_CREDENTIALS: str = "" # Path to service account JSON
    GCHAT_APP_NAME: str = "CultureBridgeBot"

    GOOGLE_TRANSLATE_PROJECT_ID: str = ""

    # SENTRY_DSN: Optional[str] = None # For error tracking

    class Config:
        env_file = ".env" # Tells pydantic-settings to load from .env
        env_file_encoding = 'utf-8'
        extra = 'ignore' # Ignore extra fields in .env

@lru_cache() # Cache the settings object
def get_settings() -> Settings:
    return Settings()

settings = get_settings()