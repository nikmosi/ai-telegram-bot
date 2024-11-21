from collections import defaultdict

from ai_telegram_bot.data import settings as app_settings
from ai_telegram_bot.data.config import GptConfig
from ai_telegram_bot.services.gpt import Gpt, TaroGpt


class GptProvider:
    gpts: defaultdict[int, Gpt]
    taros: defaultdict[int, Gpt]

    def __init__(self) -> None:
        self.gpt_settings = app_settings.gpt
        self.gpts = defaultdict(lambda: Gpt(self._get_gpt_asgs()))
        self.taros = defaultdict(lambda: TaroGpt(self._get_gpt_asgs()))

    def _get_gpt_asgs(self) -> GptConfig:
        return self.gpt_settings

    def get(self, user_id: int) -> Gpt:
        return self.get_default_gpt(user_id)

    def get_default_gpt(self, user_id: int) -> Gpt:
        return self.gpts[user_id]

    def get_taro_gpt(self, user_id: int) -> Gpt:
        return self.taros[user_id]


def setup_gpt_provider() -> GptProvider:
    return GptProvider()
