from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8000
    buffer_size: int = 1000
    apache_log_file: str
    api_key: str

    class Config:
        env_file = ".env"
