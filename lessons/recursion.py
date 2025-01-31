# Предназначение рекурсии - разбивать/уменьшить поступившие данные до тех пор, пока не будет выполнено условие входа
# Рекурсивная функция всегда представлена комбинацией основного случая (base case) и рекурсивного вызова
# В Python рекурсия ограничена глубиной стека (по умолчанию - 1000) и не оптимизирована

# Частые ошибки:
# - нет условия выхода (base case)
# - нет return
# - нет уменьшения данных

def my_sum(a_list: list) -> int:
    if not a_list:
        return 0
    if len(a_list) == 1:
        return a_list[0]
    return a_list[0] + my_sum(a_list[1:])


def my_reverse(value: str) -> str:
    if not value:
        return ''
    if len(value) == 1:
        return value
    if len(value) == 2:
        return f'{value[1]}{value[0]}'
    return f'{my_reverse(value[1:])}{value[0]}'


def my_pow(x: int, y: int) -> int:
    if y == 0:
        return 1
    if y == 1:
        return x
    return x ** y

if __name__ == '__main__':
    assert my_sum([]) == 0
    assert my_sum([1]) == 1
    assert my_sum([1, 2]) == 3
    assert my_sum([-1, -4]) == -5
    assert my_sum([1, 2, 2, 2]) == 7
    assert my_reverse('') == ''
    assert my_reverse('a') == 'a'
    assert my_reverse('1') == '1'
    assert my_reverse('10') == '01'
    assert my_reverse('abgh') == 'hgba'
    assert my_pow(55, 0) == 1
    assert my_pow(7, 1) == 7
    assert my_pow(2, 2) == 4
    assert my_pow(3, 3) == 27

