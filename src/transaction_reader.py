import csv
import pandas as pd


def transaction_read_from_csv(file_wey):
    with open(file_wey, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def transaction_read_from_xlsx(file_wey):
    reader = pd.read_excel(file_wey)
    res = reader.to_dict(orient="records")
    return res

