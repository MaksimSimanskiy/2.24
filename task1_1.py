from threading import Thread
import time
import random
from queue import Queue
import math

queue = Queue()


class Shooter():

    def __init__(self, p, name):
        self.p = p
        self.i = 1
        self.name = name

    def prb(self):
        p = math.pow(self.p, self.i)
        self.i += 1
        return p


class ProducerThread(Thread):
    def run(self):
        while True:
            i = random.randint(0, 5)
            queue.put(shoot[i])
            print (f"Стреляет {shoot[i].name}  -  {shoot[i].i} раз \n")
            time.sleep(0.1)
            if shoot[i].i == 10:
                break


class ConsumerThread(Thread):
    def run(self):
        while True:
            num = queue.get()
            queue.task_done()
            print (f"Вероятность попадания {num.i} выстрелов подряд -  {num.prb()} \n")
            time.sleep(0.1)


if __name__ == '__main__':
    str_1 = Shooter(0.5, "Иван ")
    str_2 = Shooter(0.79, "Сергей ")
    str_3 = Shooter(0.57, "Дима ")
    str_4 = Shooter(0.45, "Павел ")
    str_5 = Shooter(0.66, "Миша ")
    str_6 = Shooter(0.9, "Егор ")
    shoot = [str_1, str_2, str_3, str_4, str_5, str_6]
    ProducerThread().start()
    ConsumerThread().start()