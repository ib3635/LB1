from telethon.sync import TelegramClient

# Ваші дані
API_ID = 27858738  # Ваш API ID
API_HASH = "9579706afbf22261d76849c418f9e173"  # Ваш API Hash
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

# Ваши данные
BOT_TOKEN = "7697238010:AAHlBETPBHGhaz6D7t2hvge9o93lO3cAXUc"  # Ваш токен бота
CHAT_USERNAME = "@bot_lb1"  # Юзернейм вашей группы (соблюдайте формат с @)
MESSAGE = "Привіт! Це тестове повідомлення від бота."

# Асинхронная функция для отправки сообщения
async def send_message():
    # Создаем объект бота
    bot = Bot(token=BOT_TOKEN)

    try:
        # Отправляем сообщение в группу по юзернейму
        await bot.send_message(chat_id=CHAT_USERNAME, text=MESSAGE)
        print(f"Повідомлення надіслано в групу {CHAT_USERNAME}!")
    except Exception as e:
        print(f"Помилка: {e}")

# Запускаем асинхронную задачу
asyncio.run(send_message())

