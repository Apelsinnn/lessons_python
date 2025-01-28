# Closures Замыкание
# Замыкания между собой не пересекаются
# Каждое замыкание хранит своё состояние
# Замыкание это внутренняя функция, которая возвращается из внешней и использует переменные из внешнего скоупа
# Хранит состояние(данные), предоставляет интерфейс для работы с ними, "скрывает" данные, помогает избегать global

def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    all_values = []

    def inner(value: int) -> float:
        all_values.append(value)
        return sum(all_values) / len(all_values)

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):
    def inner(value):
        return value ** base

    return inner


def pow_lambda(base):
    return lambda value: value ** base


if __name__ == '__main__':
    print('-------------------------------------------------names-------------------------------------------')
    boys = names()
    girls = names()
    print(boys('Vasya'))
    print(boys('Petya'))
    print(boys('Dima'))
    print(girls('Lena'))
    print(girls('July'))
    print(girls('Nastya'))

    # Ниже показан пример, как можно достучаться до данных внутри замыкания
    peoples = names()
    peoples('John')
    peoples('Albert')
    # ||||||||||||||||||||||||||||||||||||||||||
    # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
    print(peoples.__closure__[0].cell_contents)

    print('-------------------------------------------------averages-------------------------------------------')
    averages = average()
    print(averages(5))
    print(averages(4))
    print(averages(3))
    print(averages(5))
    print(averages(2))
    print(averages(4))
    print(averages(5))

    print('-------------------------------------------------counter-------------------------------------------')
    count = counter()
    print(count(1))
    print(count(1))
    print(count(1))

    print('-------------------------------------------------pow-------------------------------------------')
    pow_2 = pow_(2)
    pow_3 = pow_(3)
    print(pow_2(2))
    print(pow_2(3))
    print(pow_2(4))
    print(pow_2(2))

    print(pow_3(2))
    print(pow_3(3))
    print(pow_3(4))

    print('-------------------------------------------------lambda-------------------------------------------')
    pow_lmbd = pow_lambda(2)
    print(pow_lmbd(2))
    print(pow_lmbd(3))
    print(pow_lmbd(4))
