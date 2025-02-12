# лямбда - аналог def
# В лямбде можно писать всё то, что можно писать в return в обычной функции
# нельзя например писать в return присвоение: a=1
# не выполняется до вызова: ()!!!

# решение задач питон рашиа через лямбду:
# нахождение факториала
factorial = lambda x: 1 if x == 1 else x * factorial(x-1)
print(factorial(5))

def square(x):
    return x ** 2

square(2)

square_lambda = lambda x: x ** 2
even_odd = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat: {self.name}, age: {self.age}'


if __name__ == '__main__':
    print(square(2))
    print(square_lambda(3))
    print(even_odd(1))
    print(even_odd(2))
    # ниже интересно
    x = 2
    result = lambda: x ** 2
    result_n = lambda n=x: n ** 2
    x = 3
    result_2 = lambda: x ** 2
    print(result())
    print(result_n())
    print(result_2())

    ints = list(range(10))
    print(ints)
    print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, ints))))

    a_dict = {'a': 3, 'c': 2, 'b': 1}  # ('a' 3)
    print(sorted(a_dict.items(), key=lambda x: x[0]))

    cats = [Cat('Tom', 4), Cat('Angela', 5)]
    print((sorted(cats, key=lambda x: x.name)))
    print((sorted(cats, key=lambda x: x.age)))
