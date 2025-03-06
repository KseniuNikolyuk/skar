def log(filename=None):
    """Декоратор для записи логов выполнения функций в консоль или файл."""
    def decorator(func):
        """Оборачивает функцию для добавления логирования её вызова и результата."""
        def log_line(line):
            """Записывает строку лога в консоль или в указанный файл."""
            if filename is None:
                print(line)
            else:
                with open(filename, "a") as file:
                    file.write(line + "\n")

        def wrapper(*args, **kwargs):
            """Выполняет оборачиваемую функцию и записывает результат её выполнения в лог."""
            try:
                result = func(*args, **kwargs)
                log_line(f"{func.__name__} ok: {result}. Inputs: {args}, {kwargs}")
            except Exception as e:
                log_line(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
        return wrapper
    return decorator