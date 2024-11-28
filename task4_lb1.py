from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# Получаем данные из переменных окружения
API_ID = os.getenv('API_ID')  # Ваш API ID
API_HASH = os.getenv('API_HASH')  # Ваш API Hash
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Ваш токен бота
CHAT_USERNAME = "infocommunications"  # Юзернейм чату (без t.me/)

# Підключення до Telegram через Telethon
with TelegramClient('session_name', API_ID, API_HASH) as client:
    try:
        # Отримуємо список учасників чату
        participants = client.get_participants(CHAT_USERNAME)

        # Виводимо список учасників
        print("Список учасників:")
        for participant in participants:
            print(f"ID: {participant.id}, Ім'я: {participant.first_name}, Username: {participant.username}")
    except ValueError as e:
        print(f"Помилка: {e}")

import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# Получаем данные из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Ваш токен бота
CHAT_USERNAME = "@bot_lb1"  # Юзернейм вашей группы (соблюдайте формат с @)

# Асинхронная функция для отправки сообщения
async def send_message():
    # Создаем объект бота
    bot = Bot(token=BOT_TOKEN)

    try:
        # Отправляем сообщение в группу по юзернейму
        await bot.send_message(chat_id=CHAT_USERNAME, text="Привіт! Це тестове повідомлення від бота.")
        print(f"Повідомлення надіслано в групу {CHAT_USERNAME}!")
    except Exception as e:
        print(f"Помилка: {e}")

# Запускаем асинхронную задачу
asyncio.run(send_message())

