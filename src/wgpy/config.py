from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class RabbitMQSettings(BaseModel):
    hostname: str
    port: str
    username: str
    password: str

    @property
    def url_string(self) -> str:
        return f"amqp://{self.username}:{self.password}@{self.hostname}:{self.port}"


class Settings(BaseSettings):
    rabbitmq: RabbitMQSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
