from g4f import Provider, ProviderType
from g4f.Provider import ProviderUtils
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="aibot_", env_file=".env", env_file_encoding="utf-8"
    )

    token: str = "xxx"
    admin_id: int = 5623396563
    proxy: str | None = None
    provider: ProviderType = Field(default_factory=lambda: Provider.Bing)

    @field_validator('provider', mode="before")
    @classmethod
    def validate_provider(cls, value):
        if isinstance(value, str):
            return ProviderUtils().convert[value]
        return value
