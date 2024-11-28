import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# 1. Отримуємо дати для попереднього тижня
today = datetime.today()
start_date_obj = today - timedelta(days=today.weekday() + 7)  # Початок минулого тижня (понеділок)
end_date_obj = today - timedelta(days=today.weekday() + 1)  # Кінець минулого тижня (неділя)

# Форматуємо дати для API
start_date_api = start_date_obj.strftime("%Y%m%d")
end_date_api = end_date_obj.strftime("%Y%m%d")
start_date_display = start_date_obj.strftime("%d.%m.%Y")
end_date_display = end_date_obj.strftime("%d.%m.%Y")

# 2. Формуємо URL для запиту
base_url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
params = {
    "start": start_date_api,
    "end": end_date_api,
    "valcode": "usd",  # Код валюти (USD)
    "sort": "exchangedate",
    "order": "asc",  # Порядок сортування по зростанню дати
    "json": ""  # Формат відповіді JSON
}

# 3. Робимо запит до API НБУ
response = requests.get(base_url, params=params)

# 4. Перевіряємо статус відповіді
if response.status_code == 200:
    data = response.json()

    # Якщо дані отримано, витягуємо дати та курси
    dates = [datetime.strptime(item['exchangedate'], "%d.%m.%Y") for item in data]
    rates = [item['rate'] for item in data]

    # 5. Побудова графіка
    plt.figure(figsize=(10, 5))  # Розмір графіка
    plt.plot(dates, rates, marker="o", linestyle="-", color="blue", label="Курс USD")

    # Налаштування графіка
    plt.title(f"Курс USD за період: {start_date_display} - {end_date_display}", fontsize=14)
    plt.xlabel("Дата", fontsize=12)
    plt.ylabel("Курс (UAH)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45)
    plt.legend()

    # Відображення графіка
    plt.tight_layout()
    plt.show()

else:
    print(f"Помилка: {response.status_code}. Не вдалося отримати дані.")
