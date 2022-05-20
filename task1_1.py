from threading import Thread
import time
import random
from queue import Queue

"""
Разработать приложение, в котором выполнить решение вычислительной задачи
(например, задачи из области физики, экономики, математики, статистики и т. д.) с помощью
паттерна “Производитель-Потребитель”, условие которой предварительно необходимо
согласовать с преподавателем
"""
"""
Взята задача обработок  посылок на почте.
"""
queue = Queue()


class Package():
    def __init__(self, weight, tip):
        self.id = random.randint(1, 1000)
        self.weight = weight
        self.tip = tip

    def handling(self):
        if self.weight >= 1000:
            print("Большой пакет, цена отправки - ", round(self.weight * 0.7, 2))
        else:
            print("Мелкий пакет,  цена отправки - ", round(self.weight * 0.8, 2))
        print("--------------")


class ProducerThread(Thread):
    def run(self):
        counter = 0
        while counter < 20:
            queue.put(parsels[counter])
            print(f"Получена посылка, id - {parsels[counter].id} \n")
            time.sleep(0.1)
            counter += 1

            
class ConsumerThread(Thread):
    def run(self):
        parsels_consumed = 0
        while parsels_consumed < 20:
            obj = queue.get()
            queue.task_done()
            print(f"Посылка {obj.tip}")
            obj.handling()
            time.sleep(0.1)
            parsels_consumed += 1


if __name__ == '__main__':
    parsels = [Package(random.randint(20, 2000), random.choice(['с наложным платежем', 'заказная', 'простая'])) for i in range(20)]
    ProducerThread().start()
    ConsumerThread().start()
