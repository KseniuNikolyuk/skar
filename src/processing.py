from datetime import datetime

def filter_by_state(lists: list[dict], state = "EXECUTED") -> list[dict]:
    result =[]
    for i in lists:
        if i['state'] == 'EXECUTED':
            result.append(i)
    return result

def sort_by_date(lists: list[dict], revers = True) -> list[dict]:
    return sorted(lists, key=lambda date: datetime.strptime(date["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse= revers)



