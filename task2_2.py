from queue import Queue
from threading import Thread, Lock
import math

"""
Для своего индивидуального задания лабораторной работы 2.23 необходимо
организировать конфейер, в котором сначала в отдельном потоке вычисляется значение
первой функции, после чего результаты вычисления должны передаваться второй функции,
вычисляемой в отдельном потоке. Потоки для вычисления значений двух функций должны
запускаться одновременно
"""

CONST_PRECISION = 1e-07
qe = Queue()
lock = Lock()


def sum(x=-0.7):
    lock.acquire()
    n, s, m, curr = 0, 0, 0, 0
    while True:
        pre = (n + 1) * x**n
        n += 1
        curr = (n + 1) * x**n
        if abs(curr - pre) < CONST_PRECISION:
            break
        s += curr
        qe.put(s)
    lock.release()


def func_y(x):
    result = 1/(math.pow((1 - x), 2))
    print(result)


if __name__ == '__main__':
    t1 = Thread(target=sum).start()
    t2 = Thread(target=func_y(qe.get())).start()



