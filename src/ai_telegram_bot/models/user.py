from sqlalchemy.orm import Mapped, mapped_column

from ai_telegram_bot.models import Base


class User(Base):
    tg_id: Mapped[int] = mapped_column(unique=True)
    balance: Mapped[int]
