from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="aibot_", env_file=".env", env_file_encoding="utf-8"
    )

    token: str = "xxx"
    admin_id: int = 5623396563
    proxy: str | None = None
