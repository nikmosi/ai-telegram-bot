from collections import defaultdict

from ai_telegram_bot.data import settings
from ai_telegram_bot.models.gpt import GptArgs
from ai_telegram_bot.services.gpt import Gpt, TaroGpt


class GptProvider:
    gpts: defaultdict[int, Gpt] = defaultdict(
        lambda: Gpt(
            GptArgs(
                model=settings.model,
                provider=settings.provider,
                proxy=settings.proxy,
                api_key=settings.api_key,
            )
        )
    )

    taros: defaultdict[int, Gpt] = defaultdict(
        lambda: TaroGpt(
            GptArgs(
                model=settings.model,
                provider=settings.provider,
                proxy=settings.proxy,
                api_key=settings.api_key,
            )
        )
    )

    def get(self, user_id: int) -> Gpt:
        return self.get_default_gpt(user_id)

    def get_default_gpt(self, user_id: int) -> Gpt:
        return self.gpts[user_id]

    def get_taro_gpt(self, user_id: int) -> Gpt:
        return self.taros[user_id]


def setup_gpt_provider() -> GptProvider:
    return GptProvider()
