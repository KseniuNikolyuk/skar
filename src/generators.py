def filter_by_currency(operations, currency):
    """Фильтрует операции по заданному коду валюты."""
    return (
        operation for operation in operations
        if operation.get("operationAmount").get("currency").get("code") == currency
    )


def transaction_descriptions(transactions):
    """Извлекает описания из списка транзакций."""
    return(
        transaction.get("description") for transaction in transactions
    )


def format_number(number):
    """ Форматирует число в строку, вставляя пробелы каждые четыре цифры для удобства чтения."""
    st = ""
    for i in range(16):
        nmr = number % 10
        alp_str = str(nmr)
        st = alp_str + st
        number = number // 10
        if (i + 1) % 4 == 0 and i != 15:
            st = " " + st
    return st


def card_number_generator(start, finish):
    """Генерация списков номеров карт"""
    for i in range(start, finish + 1):
        yield format_number(i)