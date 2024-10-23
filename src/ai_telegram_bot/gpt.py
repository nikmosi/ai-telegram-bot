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
        chat_gpt_response = g4f.ChatCompletion.create_async(
            messages=self.conversation_history,
            model=self.gptArgs.model,
            provider=self.gptArgs.provider,
            proxy=self.gptArgs.proxy,
            api_key=self.gptArgs.api_key,
        )
        if not isinstance(chat_gpt_response, str):
            buffer = []
            async for part in chat_gpt_response:
                buffer.append(part)
            chat_gpt_response = "".join(buffer)
        self.conversation_history.append({"role": "user", "content": chat_gpt_response})
        return chat_gpt_response
