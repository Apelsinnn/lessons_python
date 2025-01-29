# multithreading - многопоточность, подходит для IO-bound задач, использует ОС, страдает от GIL
# Полезно для ускорения выполнения задач или для того, чтобы текущий поток занялся другой задачей
# Любая программа это минимум один процесс и один поток
# Полезно использовать daemon=True, очереди разные, pool executor, НО в любом случае всё зависит от программиста!
# Плюсы:
# 1) просто(сравнительно)(например в asyncio больше нужно изучать)
# 2) быстро
# 3) не умирает из-за одного(!)(asyncio умирает)
# Минусы:
# - потребление ресурсов(потоки занимают ресурсы)
# - неуправляемость
# - проблемы потоков(lock, queue)

# Гонка потоков, это когда например первый поток взял информацию о переменной, но не успел изменить её,
# подключился второй поток, тоже взял информацию о переменной, и потом первый поток
# изменил информацию о первой переменной, например counter, на 1. После этого второй поток,
# по старой информации тоже изменил переменную, но в итоге он ничего не изменил, потому что у него была
# записана "старая" переменная которая уже изменена первым потоком. В итоге они сделали одну работу

# Для избежания гонки потоков используется lock, первый поток зашёл в функцию,
# и lock заблокировал пока что вход для следующего потока

# Deadlock - когда lock заблокировал один поток, но его забыли освободить или по какой-то причине он не освободился,
# в итоге процесс встаёт намертво бесконечно, потому что первый поток не освободил lock,
# а другие потоки не могут зайти из-за lock

import os
import threading
import time
from queue import Queue
from threading import Thread
from tkinter import *
from tkinter import ttk


def waiting(timeout):
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print('OK')


def thread_wait(timeout):
    thread = Thread(target=waiting, args=(timeout,), daemon=True)
    thread.start()
    return thread


counter = [0]
lock = threading.Lock()
queue = Queue()
queue.put(0)


def inc():
    lock.acquire()
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1
    lock.release()


def inc_queue():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c + 1)


def info():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f'Process {pid}, name {name}')


if __name__ == '__main__':
    # tk = Tk()
    # button1 = ttk.Button(tk, text='WAIT', command=lambda: waiting(3))
    # button1.pack(side=LEFT)
    # button2 = ttk.Button(tk, text='THREAD', command=lambda: thread_wait(3))
    # button2.pack(side=LEFT)
    # tk.mainloop()
    threads = [Thread(target=inc_queue, daemon=True) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(queue.qsize())
    print(queue.get_nowait())


    # print(counter)
    # info()
