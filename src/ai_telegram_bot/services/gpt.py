import g4f

from ai_telegram_bot.models import GptArgs


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

    def clear_history(self):
        self.conversation_history = []


async def answer_on_text(text: str, gpt: Gpt) -> str:
    try:
        response = await gpt.ask(text)
    except Exception:
        response = "Извините, произошла ошибка."
    return response
