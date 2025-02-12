# yield показывает, что функция = генератор
# генератор ВСЕГДА возвращает генератор(не list, не int, не None)
# генератор ленивый (lazy), одноразовый, кидает StopIteration при исчерпании
# после выполнения yield встаёт на паузу

squares = (e ** 2 for e in range(0, 11, 2))

def squares_gen_function():
    print('Generator working......')
    for e in range(0, 11, 2):
        yield e ** 2

gen = squares_gen_function()

def pause():
    print('Infinite generator working....')
    while True:
        yield a

a = 10
gen_inf = pause()

if __name__ == '__main__':
    print(gen)
    print(squares)
    print(next(squares))
    print(next(squares))
    print('---------------------')
    for i in squares:
        print(i)
    print('---------------------2')
    for i in gen:
        print(i)
    print('---------------------3')
    print(gen_inf)
    print(next(gen_inf))
    a = 20
    print(next(gen_inf))