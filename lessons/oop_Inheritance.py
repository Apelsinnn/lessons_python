# Inheritance - Наследование, это механизм получения доступа к данным и поведению своего предка,
# И расширению (изменению поведения) классов, не меняя код
# Наследование нужно для избежания повторения кода(DRY)(dont repeat yourself)
# Можно наследоваться от стандартных классов python(print, list, etc...)
# Любой объект в python наследуется от object [class Empty(object): pass]
# IS-A является (каждый класс является Employee, это важно!!)(это корень всего наследования)

# HAS-A содержит (композиция)
# Ниже пример HAS-A (композиции)
# class Engine:
#     pass
# class Wheel:
#     pass
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#         self.Wheels = [Wheel()] * 4
#     def start(self):
#         self.engine.start()



class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}, '
                f'total bonus={self.calculate_total_bonus()} rub')


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)

    # Чтобы постоянно не повторять весь этот код ниже, мы вывели его в родительский класс и наследуем его
    #     self.name = name
    #     self.salary = 15000
    #     self.bonus = 1
    #
    # def calculate_total_bonus(self):
    #     return self.salary // 100 * self.bonus
    #
    # def __str__(self):
    #     return (f'{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}, '
    #             f'total bonus={self.calculate_total_bonus()} rub')


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)


if __name__ == '__main__':
    maria = Cleaner('Mariya Petrovna')
    dmitriy = Manager('Dmitry Petrovich')
    evgeniy = CEO('Evgeniy Viktorovich')
    print(maria)
    print(dmitriy)
    print(evgeniy)
