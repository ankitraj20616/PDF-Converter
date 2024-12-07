from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_nested_delimiter = "__"

setting = Settings(_env_file = os.path.join(os.getcwd(), "app/.env"))