import time
from multiprocessing import Process, Pool
import requests

# multiprocessing - любые задачи (IO-bound или CPU-bound)
# Ускоряет любые задачи, распараллеливая их на ядра процессора (лишь до определённого предела, закон Амдала)
# Создаёт несколько процессов, каждый из которых выполняет свою задачу, взаимодействие между ними требует pickle

# API принципиально похоже на многопоточность, выгодно использовать Pool,
# а для взаимодействия между процессами Queue и Pipe

# Плюсы:
# + реальная параллельность любых задач
# + не умирает из-за одного(!)
# + процессы не зависят друг от друга(у каждого процесса своя память и GIL)
# Минусы:
# - потребление ресурсов (памяти, процессора, времени)
# - необходимость сериализации в pickle
# - проблемы синхронизации (взаимодействие между процессами)

def activity():
    result = 0
    for e in range(1000_000):
      result += abs(round(e ** 2 / 122) + e * 3.14)
    print(result)
    # requests.get('https://ya.ru')
    # print('OK')


def run(parallel=True):
    start = time.time()
    if not parallel:
        for e in range(4):
            activity()
    else:
        processes = [Process(target=activity, daemon=True) for _ in range(4)]
        for e in processes:
            e.start()
        for e in processes:
            e.join()

    end = time.time()
    print(f'Time: {end - start} seconds')

def work():
    arr = list(range(1000_000))
    step = len(arr) // 4
    position = 0
    processes = []
    for _ in range(4):
        split = arr[position:position + step]
        processes.append(Process(target=calc_sum_print, args=(split,), daemon=True))
        position += step
    start = time.time()
    for e in processes:
        e.start()
    for e in processes:
        e.join()
    end = time.time()
    print(f'Time: {end - start} seconds')

def work_pool():
    arr = list(range(1000_000))
    step = len(arr) // 4
    start = time.time()
    with Pool(10) as pool:
        result = pool.map(calc_sum, [arr[position:position + step] for position in range(0, len(arr), step)])
        print(result)
    end = time.time()
    print(f'Time: {end - start} seconds')

def calc_sum(a_list: list):
    return sum(a_list)

def calc_sum_print(a_list: list):
    print(sum(a_list))

if __name__ == '__main__':
    run()