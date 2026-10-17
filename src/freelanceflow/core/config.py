
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_ENV = os.getenv("APP_ENV", "development")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/free")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "openrouter")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
