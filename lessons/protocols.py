# Магические методы = dunder методы - методы которые начинаются с __
# __init__ по умолчанию не ждёт аргументов
# __repr__ это вывод для программистов, возвращает строку, по которой видно(и можно воссоздать) состояние объекта)
# __str__ это вывод для пользователя, возвращает строку
# Если один из этих двух методов не определён, то python просто использует repr
# Если не реализованы repr и str, то будет возвращён адрес объекта в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверять тип
# если методы сравнения не реализованы, то падает исключение
# contains для реализации проверки in
# bool для самодельных объектов, всегда вернёт True
# len() вернёт исключение, если не переопределить
# чтобы объект стал вызываемым (callable) нужно реализовать __call__, иначе упадёт исключение
# __iter__ возвращает объект итератор, тот кто реализует итер = Итерабл
# __next__ должен вернуть следующий объект из контейнера, кто его реализует = Итератор, for работает до StopIteration

# __getitem__ нужен для функционала [] (аналог списка и словаря), __setitem__ для присвоения через [],
# если не реализовать, бросается исключение
# Если в объекте не реализован __iter__, то для цикла будет использован __getitem__, там ожидается падение IndexError

class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'

    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'

    # Equal
    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    # Less than
    def __lt__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value < other.value

    # Greater than
    def __gt__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value > other.value

    # Less or equal
    def __le__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value <= other.value

    # Greater or equal
    def __ge__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value >= other.value


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    # для перебора в цикле for, связан с методом __iter__
    def __next__(self):
        while 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    # Метод проверки наличие В
    def __contains__(self, item) -> bool:
        return item in self.container

    def __bool__(self) -> bool:
        # Интересный факт, лен не занимает время на вычисление, потому что всегда известно сколько содержит элементов
        return len(self.container) > 0

    def __len__(self) -> int:
        return len(self.container)

    # Позволяет вызывать объект ()
    def __call__(self):
        return f'{sum(e.value for e in self.container)} рублей'

    # Если не определён метод __iter__ pycharm будет использовать __getitem__
    # Позволяет объекту быть iterable, связан с методом __next__
    def __iter__(self):
        return Iterator(self.container)

    # Если не определён метод __iter__ pycharm будет использовать __getitem__
    # Если работает в for, то его сигналом для остановки будет не StorIteration, а IndexError
    # Позволяет выводить элемент по индексу (может приходить как индекс, так и kvalue)
    def __getitem__(self, item: int):
        if item < 0 or item >= len(self.container):
            raise IndexError
        return self.container[item]

    # Позволяет переназначить элемент по индексу, на нужное значение (может приходить как индекс, так и kvalue)
    def __setitem__(self, key: int, value):
        if key < 0 or key >= len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == '__main__':
    banknote = Banknote(10)
    other = eval(repr(banknote))
    print(banknote)
    print(f'{banknote!r}')
    fifty = Banknote(50)
    hundred = Banknote(100)

    # ------part 2----------
    wallet = Wallet(fifty, hundred)
    print(wallet)
    print(hundred in wallet)
    if wallet:
        print('!')
    print(len(wallet))
    print(wallet())

    for money in wallet:
        print(money)

    print('---------test one more time------')
    for money in wallet:
        print(money)

    print('-------Вызов по индексу--------')
    print(wallet[1])

    wallet[0] = Banknote(500)
    print(wallet[0])
