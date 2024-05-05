from pydantic_settings import BaseSettings


class TestSettings(BaseSettings):
    app_host: str = "127.0.0.1"
    app_port: int = 8080


settings = TestSettings()
