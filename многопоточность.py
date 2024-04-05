import threading
from time import sleep

# def user_interface():
#     while True:
#         sleep(0.2)
#         print("-", end="")
#
#
# def task():
#     while True:
#         sleep(0.61)
#         print("*", end="")
#
#
# import threading
#
# threading.Thread(target=user_interface).start()
# threading.Thread(target=task).start()

# def task1():
#     pass
#
# def task2():
#     pass
#
# def task3():
#     pass
#
# tasks = [task1, task2, task3]
# args = [args1, args2, args3]
#
# # for task in tasks:
# #     threading.Thread(target=task, name=task.__name__, args=(task,)).start()
# #     print(task.__name__)
#
#
# for task, arg in tasks, args:
#     thr = threading.Thread(target=task)
#     thr.name = task.__name__
#     thr.start()


# import threading
# from time import sleep
#
#
# def task():
#     print(f"-starting task with {threading.current_thread().name}, {threading.active_count()=}")
#     sleep(1)
#     print(f"---end task with {threading.current_thread().name}")
#
#
# task()
# thr_1 = threading.Thread(target=task)
# thr_1.start()
# # thr_1.join()
#
# print(f"{threading.active_count()=}")
# print("END MAIN")


# import requests
# from time import perf_counter
# import threading
#
# sources = ["https://ya.ru",
#            "https://www.bing.com",
#            "https://www.google.ru",
#            "https://www.yahoo.com",
#            "https://mail.ru"]
#
# headers_stor = {}  # Храним здесь заголовки
# start = perf_counter()
# sum_ex_time = 0
# threads = []
#
# def task(source):
#     global sum_ex_time
#     start_tmp = perf_counter()
#     headers_stor[source] = requests.get(source).headers  # получаем заголовки и формируем словарь
#     delta = perf_counter() - start_tmp
#     print(source, delta)
#     sum_ex_time += delta
#
# for source in sources:
#     threads.append(threading.Thread(target = task, args = (source,)))
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
# print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности



# import time
#
# headers_stor_test = {}
#
# sources = ["https://ya.ru",
#            "https://www.bing.com",
#            "https://www.google.ru",
#            "https://www.yahoo.com",
#            "https://mail.ru"]
#
#
# def get_request_header(url: str):
#     time.sleep(0.8)
#     headers_stor_test[url] = "OK"
#
#
# start_time = time.perf_counter()  # запускаем отсчет времени проверки решения
#
# import threading
# threads = []
#
# for url in sources:
#     threads.append(threading.Thread(target=get_request_header, args = (url,)))
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# try:
#     delta_time = time.perf_counter() - start_time
#     assert delta_time <= 1
# except AssertionError:
#     raise Exception("!!! решение не приводит к быстродействию !!!")
# print(*headers_stor_test.values(), sep="")



# from time import sleep, perf_counter
#
# headers_stor = {}
# sources = ["bing.com",
#            "google.ru",
#            "yahoo.com",
#            "mail.ru",
#            "ya.ru"]
#
# start_time = perf_counter()  # запускаем отсчет времени проверки решения
#
# def get_request_header(url: str):
#     # моделируем различное время ответа от ресурсов
#     if url == "yahoo.com":
#         sleep(10)
#     elif url == "mail.ru":
#         sleep(1.8)
#     elif url == "google.ru":
#         sleep(0.2)
#     else:
#         sleep(1.4)
#     headers_stor[url] = "ok"
#
#
# import threading
#
# threads = []
# for url in sources:
#     threads.append(threading.Thread(target=get_request_header, args=(url,), daemon=True))
#     if url not in headers_stor:
#         headers_stor[url] = "no_response"
#
# for thread in threads:
#     thread.start()
#
# sleep(1.5)
# print(headers_stor)
#
# assert perf_counter() - start_time <= 2  # проверка того, что решение выполняется не более 2 секунд
#
# print(", ".join(f'{k}-{v}' for k, v in sorted(headers_stor.items())))




from threading import Thread, Timer
from typing import Callable

# В коде определения функции thread_log присутствуют несколько ошибок (и, возможно, не хватает нескольких инструкций).
# Исправьте их. Функция очень простая, она принимает два вызываемых объекта:
# task - целевую задачу на выполнение отдельным демоническим потоком и log_task - целевую задачу логирования,
# которая должна выполниться, если выполнение task не завершилось за отведенное время (и не должна, если task выполнился за отведенное время).
# Контрольное время - третий аргумент функции.
#
# Тестирующая система вызовет функцию thread_log и проверит ее работу с различными аргументами.

# result = False
#
# def task(func: Callable):
#     pass
#
# def callback_task(result):
#     pass
#
# def callback_handler(task: Callable = None, args=(), callback_task: Callable = None) -> None:
#     global result
#     thr = Thread(target=task, args=args, daemon=True)
#     timer = Timer(interval=0.35, function=callback_task)
#     thr.start()
#     thr.join(0.3)
#     if result:
#         timer.start()
#         timer.join()
#
# callback_handler(task=callback_task, args=(), callback_task=callback_task)

# import threading
#
#
# class TwoTaskThread(threading.Thread):  # наследуем оригинальный класс Thread
#
#     def __init__(self, task=None, new_task=None, args=()):
#         super().__init__()
#         self.new_task = new_task
#         self.task = task
#         self.args = args
#
#     def run(self):
#         try:
#             if self.task is not None:
#                 self.new_task(self.task(*self.args))
#         finally:
#             del self.task, self.args, self.new_task
#
#
# def worker(*args) -> int:
#     return sum(args)
#
#
# def handler(n):
#     print(n)
#
#
# my_thread = TwoTaskThread(worker, handler, (1, 2, 3))
# print(my_thread.task)
# print(my_thread.new_task)
# print(my_thread.args)
# my_thread.start()


# class MyThread(threading.Thread):
#     def __init__(self, msg_error: str = "error", task: Callable = None):
#         super().__init__()
#         self.msg_error = msg_error
#         self.task = task
#
#     def start(self) -> None:
#         try:
#             self.task
#         except Exception:
#             print(self.msg_error)
#
#     def run(self):
#         try:
#             if self.task is not None:
#                 self.task(self.msg_error)
#         finally:
#             del self.task


# import threading
# import requests
# from time import perf_counter
#
# start_time = perf_counter()
#
# sources = ["https://ya.ru",
#            "https://www.bing.com",
#            "https://www.google.ru",
#            "https://www.yahoo.com",
#            "https://mail.ru"]
#
# def get_request_header(url: str) -> dict:
#     return requests.get(url).headers
#
# # Допишите код здесь
# class GetHeaders(threading.Thread):
#     def __init__(self, url: str, url_headers: dict=None):
#         super().__init__()
#         self.url = url
#         self.url_headers = url_headers
#
#     def run(self):
#         header = get_request_header(self.url)
#         self.url_headers = {self.url:header}
#         return self.url_headers
#
# threads = [GetHeaders(url=url) for url in sources]
# [thread.start() for thread in threads]
# [thread.join(2) for thread in threads]
#
# results = {url: t.url_headers[url] for url, t in zip(sources, threads)}
#
# print(f"after {perf_counter() - start_time:.2f} sec.")
# print(results)
# import threading, sys
#
# class NoTargetException(Exception):
#     pass
#
#
# # Создаем класс потока
# class MyThread(threading.Thread):
#     def __init__(self, target=None, result=None):
#         super().__init__()
#         self.target = target
#         self.result = result
#
#     def run(self):
#         try:
#             if self.target is not None:
#                 self.result = self.target()
#         except Exception:
#             raise NoTargetException(threading.current_thread().name)
#
#
# # Определяем функцию перехвата исключения
# def custom_hook(*args):
#     print(f'{threading.current_thread().name} (id={threading.current_thread().ident}) failed')
#
#
# # Назначаем ее перехватчиком
# threading.excepthook = custom_hook

import threading
import queue
# from itertools import count  # для генерации целых чисел
# from time import sleep
# from random import randint
#
# queue = queue.PriorityQueue(10)
# count = count()
#
# def producer(t: int | float):
#     while True:
#         i = randint(0, 100)
#         queue.put(i)
#         print(f"{threading.current_thread().name}\tput\t->\t{i}\tQueue size = {queue.qsize()}")
#         sleep(t)
#
# def consumer(t: int | float):
#     while True:
#         n = queue.get()
#         print(f"{threading.current_thread().name}\t<-\tget\t{n}")
#         sleep(t)
#
# thread_0 = threading.Thread(target=producer, args=(0.5,), name="producer_0")
# thread_1 = threading.Thread(target=producer, args=(0.6,), name="producer_1")
# thread_2 = threading.Thread(target=consumer, args=(1, ), name="consumer_1")
# thread_3 = threading.Thread(target=consumer, args=(2, ), name="consumer_2")
# thread_4 = threading.Thread(target=consumer, args=(3, ), name="consumer_3")
# thread_0.start()
# thread_1.start()
# thread_2.start()
# thread_3.start()
# thread_4.start()

# first_queue = queue.Queue()
# second_queue = queue.Queue()
#
# while first_queue!= 0:
#     a = first_queue.get()
#     second_queue.put(a)

# from queue import Queue
# from threading import Thread
#
# valid_queue = Queue()
# none_valid_queue = Queue()
#
#
# def task():
#     while True:
#         item = valid_queue.get(timeout=timeout_handler)  # Добавляем тайм-аут для get
#         handler(item)
#
#
# def main():
#     t1.start()
#     t2.start()
#     t1.join(timeout_handler)
#     t2.join(timeout_handler)
#     for elem in get_obj():
#         if is_valid(elem):
#             handler(elem)
#         else:
#             none_valid_queue.put(elem)
#
#
# t1 = Thread(target=task, daemon=True)
# t2 = Thread(target=task, daemon=True)
# main_th = Thread(target=main)
# main_th.start()
# main_th.join()


# import threading
# import traceback
#
#
# def task():
#     raise TypeError("ops, TypeError")
#
#
# def custom_hook(args):
#     exc_type, exc_value, exc_traceback, exc_thread = args
#     print(f"Тип исключения: {exc_type.__name__}")
#     print(f"Сообщение исключения: {exc_value}")
#     print(f"Номер потока: {exc_thread.ident}")
#     print(f"Имя потока: {exc_thread.name}")
#     print(f"Путь исключения:")
#     traceback.print_tb(exc_traceback)
#
#
# threading.excepthook = custom_hook
#
# thread = threading.Thread(target=task)
# thread.start()



# import threading
#
# # создайте функцию перехватчика исключений
# def task():
#     raise TypeError() or ValueError()
#
# def except_hook(args):
#     exc_type, exc_value, exc_traceback, exc_thread = args
#     try:
#         task()
#     except Exception as err:
#         msg = f'{exc_thread.name}, {exc_type.__name__}, {exc_value}'
#         with open('custom_errors.txt', 'w') as f:
#             f.write(msg)
#
# threading.excepthook = except_hook

# my_thread = threading.Thread(target=task, name="My thread")
# my_thread.start()

# import queue
# import threading
#
# def get_next_declar():
#     return []
#
# main_queue = queue.Queue(30)
# sup_queue = queue.Queue()
#
# def producer():
#     for item in get_next_declar() is not None:
#     # while True:
#         if main_queue.full():
#             sup_queue.put(item)
#         else:
#             main_queue.put(item)
#
# def consumer():
#     while True:
#         decl = main_queue.get()
#         handler(decl)
#         main_queue.task_done()
#
#
# prod_0 = threading.Thread(target=producer)
# prod_0.start()
# prod_0.join()
#
# insp_1 = threading.Thread(target=consumer, name='insp_1', daemon=True)
# insp_2 = threading.Thread(target=consumer, name='insp_2', daemon=True)
# insp_3 = threading.Thread(target=consumer, name='insp_3', daemon=True)
# insp_1.start()
# insp_2.start()
# insp_3.start()
# insp_1.join()
# insp_2.join()
# insp_3.join()



