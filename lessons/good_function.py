import random


# Хорошая функция:
# - имеет читаемое название, нужную информацию получает в аргументах
# - короткая/читаемая
# - возвращает результат (NO PRINT!!!)
# - независима (NO GLOBAL!!!), и не меняет ничего вне себя
# - умеет делать что-то одно, но умеет это хорошо и знает всё для этого
# - если меняет пришедший аргумент, то возвращает None
# - хорошая функция, тестируема!

# Ниже плохая функция
# data = []
# value = 8
# def solution():
#     for i in range(5):
#         result = ''.join(str(random.randint(0, 9)) for _ in range(value))
#         print(result)
#         data.append(result)
#     print(data)
#     for index in range(len(data)):
#         if '5' in data[index]:
#             data[index] = data[index].replace('5', '6')
#     with open('good_function_test.txt', 'w') as file:
#         file.write('\n'.join(data))


def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def replace_fives(a_list: list, value: str) -> list[str]:
    return [element.replace('5', value) for element in a_list]

# Ниже альтернатива верхнему, но она уже меняет сам список(что не рекомендуется делать), пришедший, и возвращает None
# Такое имеет место быть, если например список огромный, и создание нового списка займёт память
# def replace_fives_inplace(a_list: list, value: str):
#     for index in range(len(a_list)):
#         a_list[index] = a_list[index].replace('5', value)
##     return None


def write_file(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]
    pins_without_fives = replace_fives(pins, '6')
    str_list = '\n'.join(pins_without_fives)
    print(pins_without_fives)
    write_file('good_function_test.txt', str_list)
