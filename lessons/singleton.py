# Паттерны или шаблоны разработки - это общие способы решения частых задач или проблем

# Singleton позволяет создавать и использовать только ОДИН объект

# Singleton Одиночка - это шаблон предоставления глобального доступа к состоянию, объект всегда один
# Monostate - это шаблон предоставления глобального доступа к состоянию, объекты могут быть разными

# нужен для одной точки доступа к ресурсам/данным и для того, чтобы ресурсоёмкие задачи сделать один раз

# Плюсы: 1 раз выполняем тяжёлые задачи, имеет 1 вход для всей системы
# Минусы: общесистемная глобальная переменная

# Модуль в python - это синглтон

class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('Do some hard work')
        # parse, db, work with data/resources etc....
        self.data = 101

# Ещё один паттерн Monostate
class Monostate:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('Do some hard work')
            # parse, db, work with data/resources etc....
            self.data = 101


if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 102
    print(second.data)

    print('---------------------------------Pattern Monostate---------------------------')
    third = Monostate()
    print(first)
    fourth = Monostate()
    print(fourth)
    print(third is fourth)
    print(third.data)
    third.data = 102
    print(fourth.data)
