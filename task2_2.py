from queue import Queue
from threading import Thread, Lock
import math

"""
Для своего индивидуального задания лабораторной работы 2.23 необходимо
организировать конфейер, в которм сначала в отдельном потоке вычисляется значение
первой функции, после чего результаты вычисления должны передаваться второй функции,
вычисляемой в отдельном потоке. Потоки для вычисления значений двух функций должны
запускаться одновременно
"""

CONST_PRECISION = 1e-07
qe = Queue()
lock = Lock()


def sum():
    lock.acquire()
    x = -0.7
    pre = 0
    s = 0
    n = 0
    curr = (n + 1) * math.pow(x, n)
    s += curr
    n += 1
    while abs(curr - pre) > CONST_PRECISION:
        pre = curr
        curr = (n + 1) * math.pow(x, n)
        n += 1
        s += curr
    qe.put(s)
    lock.release()

def compare(x, y):
    result = x - y
    print(f"Результат сравнения {result}")


def func_y(x=-0.7):
    result = 1/(math.pow((1 - x), 2))
    return result


if __name__ == '__main__':
    t1 = Thread(target=sum).start()
    t2 = Thread(target=compare(qe.get(), func_y())).start()




