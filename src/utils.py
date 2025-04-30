import json
import os
import logging
import re
from collections import Counter

logger = logging.getLogger(__name__)

# Настроим формат логирования правильно
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Добавляем обработчик для записи в файл
file_handler = logging.FileHandler("../logs", mode="w", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    if not os.path.exists(file_path):
        logger.error("путь не найден")
        return []

    try:
        logger.info("чтение файла")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):  # Проверяем, что это список
                logger.error("формат данных неверный")
                return []

            return data
    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка при чтении JSON: {e}")
        return []


def banking_operations(transaction, search):
    pattern = re.compile(search, re.IGNORECASE)
    return [t for t in transaction if "description" in t and pattern.search(t["description"])]


def categories_of_operations(operations, categories):
    pattern = re.compile("|".join(categories), re.IGNORECASE)
    tt = []
    for i in operations:
        try:
            if re.search(pattern, i["description"]):
                tt.append(i["description"])
        except (KeyError, TypeError, ValueError):
            continue

    compbined = " ".join(tt)
    matches = re.findall(pattern, compbined)
    counter = Counter(matches)

    return dict(counter)


def filter_state(transaction, state):
    pattern = re.compile(state, re.IGNORECASE)
    result = []
    for i in transaction:
        try:
            if re.search(pattern, i["state"]):
                result.append(i)
        except (KeyError, TypeError, ValueError):
            continue

    return result
