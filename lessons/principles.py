# DRY - don't repeat yourself - не повторяйся
# YAGNI - You aren't gonna need it - это не понадобится
# KISS - Keep it simple, stupid - будь проще
# POLA - Principle Of Least Astonishment - не удивляй пользователя
# EAFP - Easier to Ask for Forgiveness than Permission - проще извиниться, чем просить разрешения (сначала действуй)
# LBYL - Look Before You Leap - смотри, прежде чем прыгнуть (сначала спроси)
from pathlib import Path


# DRY before
def one():
    # some code
    with open('text.txt') as file:
        result = file.readlines()
    return result


def two():
    # some code
    with open('text2.txt') as file:
        result = file.readlines()
    return result


# DRY after
def three():
    # some code
    return read_from_file('text.txt')


def four():
    # some code
    return read_from_file('text2.txt')


def read_from_file(name):
    with open(name) as file:
        result = file.readlines()
    return result


# YAGNI, не нужно тратить время на написание того, что может никогда не понадобится
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says: Meow!')

    # Этот метод царапания, может никогда не понадобится
    def scratch(self):
        # code
        pass


# EAFP and LBYL
def five():
    # some code
    return read_from_file_eafp('text.txt')


def six():
    # some code
    return read_from_file_lbyl('text2.txt')


# EAFP
def read_from_file_eafp(name):
    try:
        with open(name) as file:
            result = file.readlines()
        return result
    except:
        # sorry
        pass


# LBYL
def read_from_file_lbyl(name):
    if Path(name).exists:
        with open(name) as file:
            result = file.readlines()
        return result
    else:
        # code
        pass
