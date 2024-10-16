import logging
from aiogram import Bot, Dispatcher, types
import g4f
from aiogram.utils import executor

# Включите логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота
API_TOKEN = '7448755655:AAHqKs0arVbnf45ocqyT-20L21O5Rhqonf4'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ID администратора (твой Telegram ID)
ADMIN_ID = 5623396563  # Замени это на свой Telegram ID

# Словарь для хранения истории разговоров
conversation_history = {}

# Функция для обрезки истории разговора
def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history

@dp.message_handler(commands=['clear'])
async def process_clear_command(message: types.Message)