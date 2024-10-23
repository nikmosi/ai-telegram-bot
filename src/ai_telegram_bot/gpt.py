from dataclasses import dataclass

import g4f
from g4f import ProviderType


@dataclass
class GptArgs:
    model: str
    provider: ProviderType
    proxy: str | None
    api_key: str | None


class Gpt:
    conversation_history: list

    def __init__(self, gptArgs: GptArgs) -> None:
        self.gptArgs = gptArgs
        self.conversation_history = []

    async def ask(self, prompt: str) -> str:
        self.conversation_history.append({"role": "user", "content": prompt})
        chat_gpt_response = await g4f.ChatCompletion.create_async(
            messages=self.conversation_history,
            model=self.gptArgs.model,
            provider=self.gptArgs.provider,
            proxy=self.gptArgs.proxy,
            api_key=self.gptArgs.api_key,
        )
        self.conversation_history.append({"role": "user", "content": chat_gpt_response})
        return chat_gpt_response
