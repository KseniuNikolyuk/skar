from datetime import datetime


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    функция сортировки списка словарей по статусу операции.
    """
    result = []
    for i in operations:
        if i["state"] == state:
            result.append(i)
    return result


def sort_by_date(operations: list[dict], revers: bool = True) -> list[dict]:
    """
    функция сортировки списка словатей по ключу даты.
    """
    return sorted(operations, key=lambda date: datetime.strptime(date["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=revers)
