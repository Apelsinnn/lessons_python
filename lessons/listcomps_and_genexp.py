#   List comprehenshion = listcomps
#   Generator expressions = genexp
from time import sleep

#   [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for ЭЛЕМЕНТ in ИСТОЧНИК if УСЛОВИЕ]
# переменные в листкомпс и генексп недоступны извне
# читается слева направо
# для словаря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ

# генератор вернет объект, а не коллекцию
# генератор ленивый, не выполняет действий и не занимает память, пока не потребуется
# генератор проверяет источник при создании!! Функцию выполняет сразу, чтобы проверить получит ли он в конце концов лист
# генератор одноразовый, если исчерпан(exhausted), то бросает исключение StopIteration
# цикл for перехватывает(не позволяет ошибки выйти) StopIteration
# для производительности, лучше использовать genexp вместо liscomps, кроме случаев, когда нужна длина len или индексы


squares = [e * e for e in range(10) if e % 2 == 0]

text = 'hello world'
words = [word.capitalize() for word in text.split()]

ints = [-1, -2, 0, 3, 4]
positives = [e for e in ints if e > 0]

letters = [letter for word in text.split() for letter in word if letter <= 'l']

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

alphabet = {index: letter for index, letter in enumerate('abcdefghijklnop', 1)}

positives_gen = (e for e in range(10_000_000_000_000_000_000_000_000_000) if e > 0)


def some_source():
    print(111)
    return [1, 2, 3]

def some_filter(x):
    sleep(3)
    return x

def some_mapping(x):
    sleep(3)
    return x


if __name__ == '__main__':
    print(squares)
    print(words)
    print(positives)
    print(letters)
    print(unique_letters)
    print(alphabet)

    print(positives_gen)
    print(next(positives_gen))
    print(next(positives_gen))

    gen = (e for e in some_source())
    print(next(gen))
    print(next(gen))

    it = (some_mapping(e) for e in some_source() if some_filter(e))
    print(next(it))