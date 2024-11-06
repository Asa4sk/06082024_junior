import random


def check_and_add_10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is int:
            new_result = {result + 10}
        else:
            new_result = {result}
        return new_result

    return wrapper


@check_and_add_10
def get_num(num):
    return num


number = 73
print(get_num(num=number))
