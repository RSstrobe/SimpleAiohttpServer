from pydantic import Field
from pydantic_settings import BaseSettings


class _BaseSettings(BaseSettings):
    """Changing the base class settings"""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class Settings(_BaseSettings):
    """Base settings for service"""

    service_name: str = Field(default="hash_app", description="Name of service")
    log_path: str = Field(default="logs/hash_logs.log", description="Path log")
    length_hash_string: int = Field(default=32, description="Length of hashed string")
    app_port: int = Field(default=8080, description="Port of application")
    app_host: str = Field(default="0.0.0.0", description="Host of application")


settings = Settings()
