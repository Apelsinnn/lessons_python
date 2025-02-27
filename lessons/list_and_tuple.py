# O(1) - обозначает, что время работы алгоритма не зависит от входных данных
# list - список, изменяемый упорядоченный, обычно хранит значения одного типа, 0(1) доступ к элементу
# tuple - кортеж, неизменяемый упорядоченный, обычно хранит значения разного типа, 0(1) доступ к элементу
# в списке и тапле не данные хранятся в памяти, а ссылки на эти данные!!! поэтому вес у элементов всегда одиннаков

# используй кортежи везде, где это возможно и обоснованно
# 1) используй [] для создания пустого списка ({} для словаря)
# 2) если заранее известен размер, то не используй append (для 8000 добавлений выделяется 8600 ячеек памяти)
# Потому что если использовать append, то пайтон думает, что в лист сейчас добавились данные и точно добавятся ещё,
# поэтому он резервирует сразу с запасом, для будущих данных
# Если нужен список для 100 элементов, лучше сделать 100 элементов нулями сначала, а потом просто по индексу их поменять
# 3) используй листкомпс
# Листкомпс более оптимизирован!
# 4) не пытайся заменять список кортежом, там где идет изменение размера

# При старте, пайтон сразу резервирует определённое количество памяти в процессоре, для таплов, поэтому они быстрее
# при создании листа пайтон обращается к процессору, а при создании тапла, нет, потому что он уже зарезервировал место,
# поэтому тапл быстрее листа
# Ещё тапл занимает меньше места в памяти, чем лист

from terminaltables import AsciiTable
from pympler import asizeof
from timeit import timeit
import dis

a_list = list(range(1000_000))

print('-----------------Пример того, что время обращения к элементам по индексу плюс минус одиннаковое-----------')
print(timeit('a_list[0]', 'from __main__ import a_list'))
print(timeit('a_list[5000]', 'from __main__ import a_list'))
print(timeit('a_list[-1]', 'from __main__ import a_list'))

print('-----------------Условный пример, как хранятся ссылки в памяти-----------')
table = AsciiTable([list(range(10))]).table
print(table)

print('-----------------Пример того, как работает тапл-----------')
new_list = [1, 2, 3]
a_tuple = (new_list, 1, 'A')
print(a_tuple)
print([id(x) for x in a_tuple])
new_list.append(1000)
print(a_tuple)
print([id(x) for x in a_tuple])
# тапл не изменился, изменился Лист, на который ссылка, адрес ссылки не поменялся!!

print('-----------------Сравнение времени создания листа и тапла-----------')
print(timeit('list()'))
print(timeit('tuple()'))

print('-----------------Сравнение размеров структур-----------')
print(asizeof.asizeof(list()))
print(asizeof.asizeof(tuple()))

print('-----------------Сравнение времени создания списка через лист и через пустые скобки-----------')
print(timeit('list()'))
print(timeit('[]'))
# Создание листа через пустые скобки в разы быстре!!!!!

print('-----------------Какие операции выполняет пайтон на базовом уровне и сколько их-----------')
print('----------------------------------list()------------------------------------------------')
dis.dis('list()')
print('----------------------------------[]------------------------------------------------')
dis.dis('[]')
