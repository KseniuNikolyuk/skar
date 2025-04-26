import json
import os
import logging

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

import re
def banking_operations(transactions, search_text):
    pattern = re.compile(re.escape(search_text), re.IGNORECASE)
    result = []

    for transaction in transactions:
        description = transaction.get('description', '')
        if pattern.search(description):
            result.append(transaction)

    return result


def categories_of_operations(operations, categories):
    result = {category: 0 for category in categories}

    for operation in operations:
        description = operation.get('description', '')
        for category in categories:

            if re.search(re.escape(category), description, re.IGNORECASE):
                result[category] += 1

    return result

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