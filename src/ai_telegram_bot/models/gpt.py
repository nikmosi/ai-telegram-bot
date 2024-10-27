from dataclasses import dataclass

from g4f import ProviderType


@dataclass
class GptArgs:
    model: str
    provider: ProviderType
    proxy: str | None
    api_key: str | None
