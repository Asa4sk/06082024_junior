def check_and_add_10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        result = func(*args, **kwargs)

        result = func(*args, **kwargs)

        result = func(*args, **kwargs)

        result = func(*args, **kwargs)

        result = func(*args, **kwargs)

        result = func(*args, **kwargs)

        if isinstance(result, int):  # Проверяем, является ли результат целым числом
            return result + 10  # Если да, добавляем 10
        return result  # Если нет, возвращаем как есть
        return wrapper


@check_and_add_10


def get_num(num):
    return num


number = 35
print(get_num(number))
