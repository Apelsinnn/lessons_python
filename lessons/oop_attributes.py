# Атрибуты - просто переменные внутри класса, метода
# LEGB-rule действует для атрибутов без приставок (self)
# Для self атрибутов поиск идёт сначала в объекте, потом в классе,
# затем у предков OCP(Object Class Parent)(такой аббревиатуры офф нету)
# Если через self попытаться поменять неизменяемый атрибут (строка), то будет создана локальная копия
# Если менять неизменяемый атрибут, то он изменится для ВСЕХ объектов класса
# cls - ссылка на класс (но не на объект!!), питон передаёт его под капотом
# @classmethod используется для работы с атрибутами класса и с методами класса, также используется как конструктор
# @staticmethod не получает ссылок под капотом, это просто функция, связанная контекстом с классом
# Если self или cls не используется нигде в методе, то это @staticmethod
# cls == BlueCat


class BlueCat:
    breed = 'Russian Blue'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Код ниже изменит атрибут breed у всех объектов
        # BlueCat.breed = 'Other'
        BlueCat.increment_count()
        self.names.append(name)

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        if name == 'Tom':
            return cls('Tom', 10)
        elif name == 'Angela':
            return cls('Angela', 8)
        return cls('Ginger', 1)

    @staticmethod
    def get_human_age(age):
        return age * 8


if __name__ == '__main__':
    tom = BlueCat.make_cat('Tom')
    angela = BlueCat.make_cat('Angela')
    tom.breed = 'Other'
    tom.meow()
    angela.meow()
    print(tom.names)
    print(angela.names)
    print(BlueCat.count)

    print(angela.get_human_age(angela.age))
    # Код ниже ранвый коду выше (по правилу поиска OCP)
    # print(BlueCat.get_human_age(angela.age))
