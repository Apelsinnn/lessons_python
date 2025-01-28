# Функция - полноправный объект и делать с ним можно всё то, что можно делать с объектом, например с переменной
# Внутренняя функция может получать переменные из внешней

# Декоратор - обёртка какой-то функции, она добавляет какие-то доп свойства или выводит какую-то информацию,
# но не меняет саму функцию


def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b): # В этот момент summ = wrapper
    return a + b


if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 4))

    # print(logger(summ)(2, 4))
    # Тот же код, что и выше, но короче

    # summ = logger(summ)
    # print(summ(2, 4))
    # Тот же код, что и 2 выше, но якобы ещё легче

    print(summ(2, 4))
