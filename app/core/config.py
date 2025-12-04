from functools import lru_cache
from typing import Optional
from pydantic import PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI School Management System"
    API_V1_STR: str = "/api/v1"
    
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    def assemble_db_connection(
        cls, v: Optional[str], info: ValidationInfo
    ) -> str:
        if isinstance(v, str):
            return v
        # Build PostgreSQL URL - Pydantic v2 PostgresDsn.build expects path WITHOUT leading slash
        db_name = info.data.get('DB_NAME') or ''
        return str(PostgresDsn.build(
            scheme="postgresql",
            username=info.data.get("DB_USER"),
            password=info.data.get("DB_PASSWORD"),
            host=info.data.get("DB_HOST"),
            path=db_name,  # Just the database name, no leading slash
        ))

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
