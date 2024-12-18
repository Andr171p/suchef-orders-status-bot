import os
from typing import Dict
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class SQLiteConfig(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/src/database/data/users.db"


class PostgreSQLConfig(BaseSettings):
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/railway"


class RMQConfig(BaseSettings):
    user: str = os.getenv("RMQ_USER")
    password: str = os.getenv("RMQ_PASSWORD")
    host: str = os.getenv("RMQ_HOST")
    port: str = os.getenv("RMQ_PORT")
    url: str = f"amqp://{user}:{password}@{host}:{port}"


class APIServiceConfig(BaseSettings):
    url: str = os.getenv("API_URL")
    headers: Dict[str, str] = {"Content-Type": "application/json; charset=UTF-8"}


class QueueConfig(BaseSettings):
    name: str = "orders"


class MessagesConfig(BaseSettings):
    start: Path = BASE_DIR / "src" / "app" / "statics" / "messages" / "start.json"
    auth: Path = BASE_DIR / "src" / "app" / "statics" / "messages" / "auth.json"
    statuses: Path = BASE_DIR / "src" / "app" / "statics" / "messages" / "statuses.json"


class TelegramConfig(BaseSettings):
    token: str = os.getenv("BOT_TOKEN")


class Config(BaseSettings):
    telegram: TelegramConfig = TelegramConfig()
    sqlite: SQLiteConfig = SQLiteConfig()
    postgresql: PostgreSQLConfig = PostgreSQLConfig()
    messages: MessagesConfig = MessagesConfig()
    rmq: RMQConfig = RMQConfig()
    queue: QueueConfig = QueueConfig()
    api: APIServiceConfig = APIServiceConfig()


config = Config()
