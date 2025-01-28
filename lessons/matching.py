# Example 1
def calculate(a, b, operation) -> str:
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '/':
            return a / b
        case '*':
            return a * b
        case _:  # wildcard
            return f'Не знаю такой операции {operation}'


# Example 2
# Написать функцию, которой на вход может прийти полное имя студента (ФИО) в формате строки, кортежа, списка, словаря
# функция должна возвращать текст "Error", при неверных или недостаточных данных, или возвращать строку
# типа f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'

def parse_names(value: str | tuple | list | dict) -> str:
    match value:
        case [surname, name, second_name]:
            # or pass
            return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
        case {'surname': surname, 'name': name, 'second_name': second_name} if len(value) == 3:
            # or pass
            return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            # or pass
            return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'
        case _:
            return 'Error'
    # or return f'Фамилия: {surname}, Имя: {name}, Отчество: {second_name}'


# Example 3
def parse_response(value):
    match value:
        case {'key': 1000, **rest}:
            return rest['id']
        case ('error', message) | ('error', message, *_):
            # Если для проверки шаблонов используется или '|', то имена шаблонов(message) должны совпадать
            raise ValueError(message)
        case {'meta': val, **rest} if not rest:
            return val['id']
        case {'meta': {'code': _, 'error': error}, 'info': [{'allowed': allowed}, _]}:
            return f'{error}, {allowed}'
        case (set() as x, _) if len(x) == 2:
            return max(x)
        case _:
            raise ValueError(f'Unknown value: {value}')

# Example 4
def check(value: tuple):
    match value:
        case (name, _, salary) if name in ('John', 'Ana'):
            return salary
        case ('Helen', age, _):
            return age
        case (_, _, _, _, str(something)):
            return f'Strange! {something}'
        case (*_, something) if len(value) == 6:
            return f'{something}'
        case tuple():
            return f'Unknown content {value}'
        case _:
            raise ValueError('Expected a tuple!')


if __name__ == '__main__':
    # Example 1
    print('----------------------------------------------Example 1----------------------------------------')
    print(calculate(2, 2, '+'))
    print(calculate(2, 2, '-'))
    print(calculate(2, 2, '/'))
    print(calculate(2, 2, '*'))
    print(calculate(2, 2, '&'))

    # Example 2
    print('----------------------------------------------Example 2----------------------------------------')
    assert parse_names(('Иванов', 'Иван', 'Иванович')) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names(('Иванов', 'Иван')) == 'Error'
    assert parse_names(['Иванов', 'Иван', 'Иванович']) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names({'surname': 'Иванов',
                        'name': 'Иван',
                        'second_name': 'Иванович'}) == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names('Иванов Иван Иванович') == 'Фамилия: Иванов, Имя: Иван, Отчество: Иванович'
    assert parse_names(['Иванов', 'Иван']) == 'Error'
    assert parse_names(['Иванов', 'Иван', 'Иван', 'Иван', 'Иван']) == 'Error'
    assert parse_names({'a': 'Иванов', 'b': 'Иван', 'c': 'Иванович'}) == 'Error'
    assert parse_names(['Иванов Иван Иванович 122']) == 'Error'
    assert parse_names({'surname': 'Иванов',
                        'name': 'Иван',
                        'second_name': 'Иванович',
                        'salary': 100_000}) == 'Error'

    # Example 3
    print('----------------------------------------------Example 3----------------------------------------')
    first = {'key': 1000, 'id': 999, 'uwu': 'yes', 'kuku': 'no'}
    second = ['error', 'Slow network connection!', 333, 444, 555]
    third = {'meta': {'id': 333}}
    fourth = {'meta': {'code': 200, 'error': 'no'}, 'info': [{'allowed': 'yes'}, 111]}
    fifth = ({10, 11}, 5)
    print(parse_response(first))
    # raise print(parse_response(second))
    print(parse_response(third))
    print(parse_response(fourth))
    print(parse_response(fifth))

    # Example 4
    first = ('Ana', 22, 100_000)
    second = ('Helen', 21, 100_000)
    third = (1, 2, 3, 4, '100')
    fourth = (1, 2, 3, 4, 5, 1000)
    print(check(first))
    print(check(second))
    print(check(third))
    print(check(fourth))

