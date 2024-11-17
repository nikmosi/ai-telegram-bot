from typing import TypedDict, override

import g4f
from loguru import logger

from ai_telegram_bot.data.config import GptConfig
from ai_telegram_bot.data.constants import taro_gpt_prompt
from ai_telegram_bot.exceptions.exceptions import GptConversationException


class Message(TypedDict):
    role: str
    content: str


class Gpt:
    conversation_history: list[Message]

    def __init__(self, gptArgs: GptConfig) -> None:
        self.gptArgs = gptArgs
        self.conversation_history = []

    async def ask(self, prompt: str) -> str:
        self.conversation_history.append(Message(role="user", content=prompt))
        chat_gpt_response = await g4f.ChatCompletion.create_async(
            messages=self.conversation_history,
            **self.gptArgs.model_dump(),
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
        prompt = taro_gpt_prompt.format(prompt=prompt)
        return await super().ask(prompt)


async def answer_on_text(text: str, gpt: Gpt) -> str:
    logger.debug(f"{text=}")
    try:
        response = await gpt.ask(text)
    except Exception as e:
        response = "Извините, произошла ошибка."
        logger.error(e)
    return response


async def determine_taro_request(text: str, gpt: Gpt) -> str:
    logger.debug("taro request")
    response = await answer_on_text(text, gpt)

    return response.strip().lower()
