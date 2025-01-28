# LEGB - rule
# L - Local
# E - Enclosed
# G - Global
# B - Builtins
# Порядок поиска переменной интерпретатором такой же, какое и название. Сначала он ищет локально, потом enclosed, потом глобально, потом во внутренних переменных pycharm
# Интерпретатор останавливает поиск переменной, сразу, как только нашёл переменную

import builtins

builtins.scope = 'Builtins'

scope = 'Global'


def outer():
    scope = 'Enclosed'

    def inner():
        scope = 'Local'
        print(scope)

    inner()


if __name__ == '__main__':
    outer()
    print(scope)
