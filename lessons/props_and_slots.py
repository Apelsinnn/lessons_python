# Нужно использовать set/get а также property ТОЛЬКО при наличии логики в получении или установке атрибута
# Возможность установки/получения атрибутов с логикой
# Запретить менять атрибут или добавлять новые атрибуты

# Нужно использовать __setattr__ если нужно проверять параметры, которые приходят в атрибуты класса,
# не надо делать проверку в __init__!!! Потому что эта проверка сработает только при создании объекта
# и не сработает при изменении атрибутов уже существующего объекта

# __dict__ это атрибут объектов в python, который хранит состояние объекта (что в нём записано, например name и age)
# __setattr__ вызывается при попытке установить или изменить атрибут

# Если мы добавляем метод __slots__, python меняет dict объекта на tuple и это сильно уменьшает занимаемую память,
# данные внутри теперь хранятся в tuple, а не в dict
# __slots__ - создан для уменьшения памяти, занимаемой объектами

from pympler import asizeof

class Cat:
    # Первый способ сделать проверку на входящие значения
    # FIELDS = ('name', 'age')

    # Второй способ сделать проверку на входящие значения
    __slots__ = ('_name', '_age')


    def __init__(self, name, age):
        # Первый способ сделать проверку на входящие значения
        # self.name = name
        # self.age = age

        # Второй способ сделать проверку на входящие значения
        # Стоит обратить внимание, что self.name это теперь ссылка на декоратор name, а не новый атрибут
        # Но это при условии, что мы делаем декоратор сеттер, если только геттер, то нужно будет сделать _name
        self.name = name
        self.age = age

    # Второй способ сделать проверку на входящие значения
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError('Name cant be empty!')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 1 or value > 15:
            raise AttributeError('Age shot be in range 1-15')
        self._age = value

    def __repr__(self):
        return f'Cat (name={self.name}, age={self.age})'

    # Первый способ сделать проверку на входящие значения
    # def __setattr__(self, key, value):
    #     if key not in self.FIELDS:
    #         raise AttributeError(f'No attribute {key}')
    #     if key == 'name' and not value:
    #         raise AttributeError('Name cant be empty!')
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError('Age shot be in range 1-15')
    #     self.__dict__[key] = value


if __name__ == '__main__':
    tom = Cat('Tom', 2)
    # Test raise
    # tom.age = 0
    # tom.name2 = 'Jerry'
    print(asizeof.asizeof(tom))
    # tom.name2 = 'Jerry'
    print(tom)
