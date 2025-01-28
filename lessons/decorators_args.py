# Дублирование кода - плохо

def typed_int(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError('Тип должен быть int')
        return function(*args)

    return wrapped


def typed_str(function):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError('Тип должен быть str')
        return function(*args)

    return wrapped


# Функция ниже вмещает в себя две функции выше и другие типы данных тоже
def typed(type_):
    def real_decorator(function):
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип должен быть {type_}')
            return function(*args)

        return wrapped

    return real_decorator

# @typed_int
# def calculate(a: int, b: int, c: int) -> int:
#     # Logic
#     return a + b + c
#
# @typed_str
# def convert(a: str, b: str) -> str:
#     # Logic
#     return a + b


@typed(int)
def calculate(a: int, b: int, c: int) -> int:
    # Logic
    return a + b + c


@typed(str)
def convert(a: str, b: str) -> str:
    # Logic
    return f'{a} {b}'


if __name__ == '__main__':
    print(calculate(1, 2, 3))
    print(convert('Hello', 'world'))
