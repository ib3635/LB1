import requests
from datetime import datetime, timedelta

# 1. Определяем даты для предыдущей недели
today = datetime.today()
start_date_obj = today - timedelta(days=today.weekday() + 7)  # Начало прошлой недели (понедельник)
end_date_obj = today - timedelta(days=today.weekday() + 1)   # Конец прошлой недели (воскресенье)

# Форматируем для API (YYYYMMDD) и для отображения (DD.MM.YYYY)
start_date_api = start_date_obj.strftime("%Y%m%d")
end_date_api = end_date_obj.strftime("%Y%m%d")
start_date_display = start_date_obj.strftime("%d.%m.%Y")
end_date_display = end_date_obj.strftime("%d.%m.%Y")

# 2. Формируем URL для запроса
base_url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
params = {
    "start": start_date_api,
    "end": end_date_api,
    "valcode": "usd",  # Код валюты (например, USD)
    "sort": "exchangedate",
    "order": "desc",
    "json": ""  # Указывает формат ответа JSON
}

# 3. Делаем запрос к API НБУ
response = requests.get(base_url, params=params)

# 4. Проверяем статус ответа
if response.status_code == 200:
    data = response.json()
    print(f"Курс USD за прошлую неделю (с {start_date_display} по {end_date_display}):\n")
    for rate in data:
        print(f"Дата: {rate['exchangedate']}, Курс: {rate['rate']} UAH")
else:
    print(f"Ошибка: {response.status_code}. Проверьте URL или параметры.")
