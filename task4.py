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

from telethon.sync import TelegramClient

# Ваши данные
API_ID = 27858738  # Ваш API ID
API_HASH = "9579706afbf22261d76849c418f9e173"  # Ваш API Hash
BOT_TOKEN = "7697238010:AAHlBETPBHGhaz6D7t2hvge9o93lO3cAXUc"  # Ваш токен бота

# Ссылка на группу
GROUP_LINK = "https://t.me/+f_bXgWAWdN8zOTdi"  # Ссылка на вашу группу
MESSAGE = "Привіт! Це тестове повідомлення від бота."  # Сообщение, которое бот отправит

# Подключение через бота
with TelegramClient('bot_session', API_ID, API_HASH) as client:
    client.start(bot_token=BOT_TOKEN)  # Подключаемся через токен бота

    try:
        # Получаем информацию о группе по ссылке
        group = client.get_entity(GROUP_LINK)

        # Отправляем сообщение в группу
        client.send_message(group, MESSAGE)
        print(f"Повідомлення надіслано в групу {group.title}!")

    except Exception as e:
        print(f"Помилка: {e}")




