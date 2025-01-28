import csv
from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple

print("-----------------------------------------OrderedDict----------------------------------")

# OrderedDict нужен для действий со словарём, где необходим порядок элементов, например сравнение с учётом порядка,
# перестановки элементов с сохранением порядка. МИНУС этот словарь занимает в 2 раза больше памяти!

first = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
second = {2: 2, 1: 1, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

order1 = OrderedDict(first)
order2 = OrderedDict(second)

print(first == second)  # смотрит на сходство элементов, вне зависимости от порядка
print(order1 == order2)  # смотрит на сходство элементов, С ЗАВИСИМОСТЬЮ от порядка
print(order1.popitem())  # выдёргивает ласт элемент
print(order1.popitem(last=False))  # выдёргивает первый элемент
order2.move_to_end(1)  # перемещает элемент с указанным ключом в конец
print(order2)
order2.move_to_end(7, last=False)  # перемещает элемент с указанным ключом в начало
print(order2)

print("-----------------------------------------ChainMap----------------------------------")

# ChainMap нужен для логического объединения словарей, для поиска информации, но при изменениях, меняется первый словарь
# Рекомендация: использовать ChainMap только для чтения, а не для изменения


third = {1: 1, 2: 2, 3: 3}
fourth = {4: 4, 5: 5}

chain = ChainMap(third, fourth)  # объединяет указанные словари, для поиска в них

print(chain)
print(2 in chain)
print(5 in chain)
chain[5] = 200
print(chain)

print("-----------------------------------------Counter----------------------------------")

# Counter работает и считает только Hashable объекты
# Counter нужен для подсчёта элементов в последовательности

counter = Counter(['hello', 'world'])  # Разбивает лист на каждый элемент и считает, сколько в нём одиннаковых символов
print(counter)
counter.update('world')  # Позволяет добавить нужное слово в counter
print(counter)
print(counter.most_common(3))

print("-----------------------------------------defaultdict----------------------------------")

# defaultdict нужен для создания словаря со значением по умолчанию. Значение подставляется из указанного в скобках,
# при обращении к несуществующему ключу

a_dict = defaultdict(int)
print(int())  # Фишка, если вызвать int без параметров, вернётся 0
for char in 'hello':
    a_dict[char] += 1
print(a_dict)
print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))

b_dict = defaultdict(list)
for char in 'hello':
    b_dict[char].append(char)
print(b_dict)

print("-----------------------------------------deque----------------------------------")

a_deque = deque([1, 2, 3], maxlen=3)
print(a_deque)
a_deque.append(4)
print(a_deque)

with open('points.csv') as file:
    a_deque = deque(file, maxlen=2)

# deque потокобезопасна, быстро оперирует с обеими сторонами
# если использовать в многопотоке, один поток не будет брать данные такие же, какие на другом потоке

for line in a_deque:
    print(line.rstrip())

print("-----------------------------------------namedtuple----------------------------------")

# namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом
# namedtuple Неизменяемый, позволяет обращаться, как по индексу, так и по имени атрибута

tom = ('Tom', 4, 'yellow')

Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)
print(tom[0])
print(tom.name)

Point = namedtuple('Point', 'x y')
with open('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)
