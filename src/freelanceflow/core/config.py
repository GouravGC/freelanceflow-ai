
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_ENV = os.getenv("APP_ENV", "development")

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/free")

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:270m")
    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434/v1",
    )

    AI_PROVIDER = os.getenv("AI_PROVIDER", "openrouter")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
