from src.transaction_reader import transaction_read_from_csv, transaction_read_from_xlsx
from src.utils import load_transactions, filter_state
from datetime import datetime


def main():
    print(
        """Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    while True:
        try:
            choise_file = int(input("Пользователь: "))
            if choise_file not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Программа: Введите число 1, 2 или 3")

    transaction = None

    if choise_file == 1:
        print("Программа: Для обработки выбран JSON-файл. ")
        transaction = load_transactions("data/operations.json")
    elif choise_file == 2:
        print("Программа: Для обработки выбран CSV-файл. ")
        transaction = transaction_read_from_csv("data/transactions.csv")
    elif choise_file == 3:
        print("Программа: Для обработки выбран XLSX-файл. ")
        transaction = transaction_read_from_xlsx("data/transactions_excel.xlsx")

    print(
        """Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    transaction = choise_state(transaction)

    transaction = date_by_sort(transaction)
    transaction = filter_currency(transaction)
    transaction = filter_by_description(transaction)

    print("\nПрограмма: Распечатываю итоговый список транзакций...")

    if not transaction:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"\nПрограмма:\nВсего банковских операций в выборке: {len(transaction)}\n")
        for tx in transaction:
            date_str = tx["date"].strftime("%d.%m.%Y") if isinstance(tx["date"], datetime) else tx.get("date", "???")
            description = tx.get("description", "Без описания")
            account_info = tx.get("from", "") + (" -> " + tx["to"] if "to" in tx else "")
            amount = tx.get("operationAmount", {}).get("amount", "???")
            currency = tx.get("operationAmount", {}).get("currency", {}).get("name", "???")

            print(f"{date_str} {description}")
            if account_info.strip():
                print(account_info)
            print(f"Сумма: {amount} {currency}\n")


def choise_state(transaction):
    while True:
        choise_state = input("Пользователь: ")
        choise_state = choise_state.upper()
        if choise_state in ("EXECUTED", "CANCELED", "PENDING"):
            print(f'Программа: Операции отфильтрованы по статусу "{choise_state}"')
            return filter_state(transaction, choise_state)
        else:
            print(f'Программа: Статус операции "{choise_state}" недоступен. Попробуйте снова.')


def date_by_sort(transactions):
    date_sort = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ")
    if date_sort.lower() == "да":
        for i in transactions:
            try:
                i["date"] = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
            except Exception:
                continue

        while True:
            sort_on_date = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
            if sort_on_date in ("по убыванию", "по возрастанию"):
                reverse = sort_on_date == "по убыванию"
                transactions = [tx for tx in transactions if "date" in tx and isinstance(tx["date"], datetime)]
                return sorted(transactions, key=lambda tx: tx["date"], reverse=reverse)
            else:
                print("Неверный ввод: введите 'по убыванию' или 'по возрастанию'")
    return transactions


def filter_currency(transactions):
    currency = input("Программа: Выводить только рублевые тразакции? Да/Нет\nПользователь: ").lower()
    if currency == "да":
        filtered = []
        for tx in transactions:
            try:
                if (
                    tx["operationAmount"]["currency"]["name"] == "руб."
                    or tx["operationAmount"]["currency"]["code"] == "RUB"
                ):
                    filtered.append(tx)
            except Exception:
                continue
        return filtered
    return transactions


def filter_by_description(transactions):
    choice = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    ).lower()
    if choice == "да":
        keyword = input("Программа: Введите ключевое слово:\nПользователь: ").lower()
        return [tx for tx in transactions if keyword in tx.get("description", "").lower()]
    return transactions


main()
