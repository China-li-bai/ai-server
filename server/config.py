import os

class Config:
    DS_API_KEY = os.getenv("DS_API_KEY")
    DS_BASE_URL = os.getenv("DS_BASE_URL")
    DS_MODEL_NAME = os.getenv("DS_MODEL_NAME", "deepseek-v3-241226")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    FREE_OPENAI_API_KEY = os.getenv("FREE_OPENAI_API_KEY")
    FREE_OPENAI_BASE_URL = os.getenv("FREE_OPENAI_BASE_URL")
    FREE_OPENAI_MODEL_NAME = os.getenv("FREE_OPENAI_MODEL_NAME", "gpt-3.5-turbo")