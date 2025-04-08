import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_convert_rub(transaction):
    """Конвертирует сумму транзакции в рубли."""
    try:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        res = response.json()
        return res.get("result")
    except (KeyError, ValueError, TypeError):
        return None


def amount_transaction(transaction):
    count = 0
    for i in transaction:
        try:
            if not isinstance(i, dict) or not i:
                continue
            else:
                if i["operationAmount"]["currency"]["code"] == "RUB":
                    count += float(i["operationAmount"]["amount"])
                else:
                    converted = get_convert_rub(i)
                    if converted is not None:
                        count += converted
        except (KeyError, TypeError, ValueError):
            continue
    return count
