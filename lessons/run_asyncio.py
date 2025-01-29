import asyncio
import aiohttp
import requests
import time


# asyncio - асинхронное выполнение, подходит для IO-bound задач, работает ровно 1 поток
# Плюсы:
# + скорость и экономия времени, вместо x + y + z -> max(x, y, z)
# + управляемость
# + меньше потребление ресурсов
# Минусы:
# - "умирает" из-за одного блокирующего вызова(!)
# - event loop не резиновый

# 1) корутина(coroutines) работает как генератор
# 2) async - явный флаг, что данная функция является асинхронной (корутиной)
# 3) await - явный флаг, что в этом месте корутина встаёт на паузу и даёт работать другим, пока ждёт свои данные
# 4) event loop - цикл событий, механизм, который отвечает за планирование и запуск корутин. Можно представить как
# список/очередь, из которого в вечном цикле достаются и запускаются корутины

# Частые ошибки:
# - не использовать await внутри корутин
# - создание корутины, но использование ее, как функции
# - использование в корутинах синхронного(блокирующего) кода, в том числе IO

def gen():
    x = 10
    print(x)
    yield x


# print(gen)


async def one():
    print('Start one')
    await asyncio.sleep(2)
    print('Stop one')


async def two():
    print('Start two')
    await asyncio.sleep(2)
    # time.sleep(5)
    print('Stop two')


async def three():
    print('Start three')
    await asyncio.sleep(3)
    print('Stop three')


async def main():
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # await asyncio.create_task(three())

    # или так
    # await asyncio.gather(one(), two(), three())

    await asyncio.gather(*(async_http() for _ in range(10)))

# Пример плохой, блокирующей корутины
async def blocking():
    resp = requests.get('https://ya.ru')
    print(resp.status_code)

# Пример хорошой, асинхронной корутины
async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://ya.ru') as resp:
            print(resp.status)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
