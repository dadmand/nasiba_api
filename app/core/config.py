from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, field_validator, ConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Database configuration
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    SQLALCHEMY_DATABASE_URL: Optional[PostgresDsn] = None

    @field_validator("SQLALCHEMY_DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info) -> PostgresDsn:
        if isinstance(v, str):
            return PostgresDsn(v)
        values = info.data
        connection_str = f"postgresql://{values['DB_USERNAME']}:{values['DB_PASSWORD']}@{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}"
        return PostgresDsn(connection_str)

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_file_encoding='utf-8'
    )

# Create an instance of Settings
settings = Settings()