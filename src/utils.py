import json
import os
import logging

logger = logging.getLogger(__name__)

# Настроим формат логирования правильно
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Добавляем обработчик для записи в файл
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
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
