from typing import TypedDict, override

import g4f
from ai_telegram_bot.exceptions.exceptions import GptConversationException
from ai_telegram_bot.models import GptArgs


class Message(TypedDict):
    role: str
    content: str


class Gpt:
    conversation_history: list[Message]

    def __init__(self, gptArgs: GptArgs) -> None:
        self.gptArgs = gptArgs
        self.conversation_history = []

    async def ask(self, prompt: str) -> str:
        self.conversation_history.append(Message(role="user", content=prompt))
        chat_gpt_response = await g4f.ChatCompletion.create_async(
            messages=self.conversation_history,
            model=self.gptArgs.model,
            provider=self.gptArgs.provider,
            proxy=self.gptArgs.proxy,
            api_key=self.gptArgs.api_key,
        )
        self.conversation_history.append(
            Message(role="assistant", content=chat_gpt_response)
        )
        if not isinstance(chat_gpt_response, str):
            raise GptConversationException()
        return chat_gpt_response

    def clear_history(self) -> None:
        self.conversation_history = []


class TaroGpt(Gpt):
    @override
    async def ask(self, prompt: str) -> str:
        self.clear_history()
        prompt = f"Определи, является ли запрос '{prompt}' запросом к таро. Ответь 'Да' или 'Нет'."
        return await super().ask(prompt)


async def answer_on_text(text: str, gpt: Gpt) -> str:
    try:
        response = await gpt.ask(text)
    except Exception:
        response = "Извините, произошла ошибка."
    return response


async def determine_taro_request(text: str, gpt: Gpt) -> bool:
    response = await answer_on_text(text, gpt)

    return "Да" in response.strip()
