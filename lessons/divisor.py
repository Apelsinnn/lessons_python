# import doctest

def divide(a: int, b: int) -> int:
    """
    Делит первое число на второе и возвращает результат
    :param a: целое число(делимое)
    :param b: целое число(делитель)
    :return: целое число(частное)
    :raises: ValueError: если делить равен нулю

    >>> divide(10, 5)
    2
    >>> divide(2, 2)
    1
    """
    if b == 0:
        raise ValueError("На 0 делить нельзя")
    return a // b

# if __name__ == '__main__':
#     doctest.testmod()