from typing import Any

from g4f import Provider, ProviderType
from g4f.Provider import ProviderUtils
from pydantic import BaseModel, Field, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 50
    pool_size: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="aibot_",
        env_nested_delimiter="__",
        env_file=(".env.example", ".env"),
        env_file_encoding="utf-8",
    )

    token: str = "xxx"
    admin_id: int = 5623396563
    proxy: str | None = None
    model: str = "gpt-4o"
    api_key: str | None = None
    provider: ProviderType = Field(default_factory=lambda: Provider.Bing)

    db: DatabaseConfig = Field(default="default")

    @field_validator("provider", mode="before")
    @classmethod
    def validate_provider(cls, value: Any) -> ProviderType:
        if isinstance(value, str):
            return ProviderUtils().convert[value]
        return value


settings = Settings()
print(settings.model_dump())
