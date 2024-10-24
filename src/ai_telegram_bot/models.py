from aiogram.types import Message


class UserInfo:
    def __init__(self, message: Message):
        id = message.from_user
        if id is None:
            raise Exception("from_user is None")
        text = message.text
        if text is None:
            raise Exception("text is None")

        self.id = id
        self.text = text
