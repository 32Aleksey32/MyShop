# import asyncio
# # Определение асинхронной функции (корутины) cook_dish(n), которая имитирует повара, готовящего блюдо.
# # Используется корутина для того, чтобы одновременно запускать несколько "поваров" ииспользовать время ожидания (приготовление) эффективно.
#
# async def cook_dish(n):
#     print(f"Повар {n} начинает готовить") # Повар n начинает готовить
#     await asyncio.sleep(n) # Повар готовит блюдо n секунд. asyncio.sleep(n) используется для имитации задержки, которая требуется для приготовления блюда.
#     print(f"Повар {n} закончил готовить") # Повар n закончил готовить
#     return f"Блюдо от повара {n}" # Возвращает строку, указывающую, что блюдо от повара n готово.
#
# # Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.
# async def main():
#     tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)] # Создаются задачи для каждого повара (от 1 до 3). Используется create_task для запуска корутины.
#     print(await asyncio.gather(*tasks)) # Ожидает завершения всех задач, затем выводит результат. asyncio.gather используется для ожидания всех корутин, затем собирает их результаты в список.
#
# # Запуск главной корутины
# asyncio.run(main())



# import asyncio
# async def access_resource(resource, lock):
#     await lock.acquire() # получаем блокировку. lock.acquire используется для получения контроля над ресурсом
#     try:
#         print(f"Доступ получен {resource}") # сообщаем, что доступ к ресурсу получен
#         await asyncio.sleep(1) # создаем паузу для имитации работы с ресурсом. asyncio.sleep используется для создания паузы в асинхронном коде
#         print(f"Доступ завершён {resource}") # сообщаем, что работа с ресурсом завершена
#     finally:
#         lock.release() # освобождаем блокировку. lock.release используется для возврата контроля над ресурсом
#
# async def main():
#     lock = asyncio.Lock() # создаем объект блокировки. asyncio.Lock используется для синхронизации доступа к общему ресурсу
#     resource = "--Защищаемый ресурс--" # инициализируем ресурс
#     tasks = [access_resource(resource, lock) for _ in range(5)] # создаем список задач на доступ к ресурсу
#     await asyncio.gather(*tasks) # выполняем все задачи параллельно. asyncio.gather используется для параллельного выполнения задач
#
# asyncio.run(main()) # запускаем главную асинхронную функцию. asyncio.run используется для запуска корутины и ожидания её завершения

# import asyncio
#
# bank_account = 1000 # Инициализация банковского счета
#
# async def withdraw_money(amount, lock): # Асинхронная функция для снятия денег
#     global bank_account # Объявление bank_account как глобальной переменной, чтобы изменить значение вне функции
#     async with lock:
#         if bank_account >= amount: # Проверка наличия достаточных средств на счете
#             print(f"Снятие {amount}р успешно") # Вывод сообщения об успешном снятии средств
#             await asyncio.sleep(1) # Используется асинхронная задержка, чтобы имитировать обработку банковской операции
#             bank_account -= amount # Вычитание суммы снятия из общего банковского счета
#
# async def main(): # Главная асинхронная функция
#     lock = asyncio.Lock()
#     task1 = asyncio.create_task(withdraw_money(900, lock)) # Создание задачи для асинхронного снятия средств.
#     # Используется asyncio.create_task для создания и запуска корутины без блокировки основного потока
#     task2 = asyncio.create_task(withdraw_money(900, lock)) # То же самое для второй операции снятия денег
#     await asyncio.gather(task1, task2) # asyncio.gather используется для запуска и ожидания завершения всех задач.
#     # Позволяет запускать несколько задач одновременно
#     print(f'Остаток средств {bank_account}р') # Вывод оставшегося баланса банковского счета
#
# asyncio.run(main()) # Запуск главной функции. asyncio.run запускает переданную асинхронную функцию и ожидает ее завершения.
# # Это самый простой способ запустить асинхронный код



# import asyncio
#
# async def activate_portal(x):
#     print(f'Активация портала в процессе, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x * 2
#
# async def perform_teleportation(x):
#     print(f'Телепортация в процессе, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x + 2
#
#
# # async def portal_operator():
# #     task1 = asyncio.create_task(activate_portal(2))
# #     task1_result = task1.result()
# #     await task1
# #     if task1_result > 4:
# #         task2 = asyncio.create_task(perform_teleportation(1))
# #         await task2
# #     else:
# #         task2 = asyncio.create_task(perform_teleportation(task1_result))
# #         await  task2
# #     print(f'Результат активации портала: {task1.result()} единиц энергии')
# #     print(f'Результат телепортации: {task2.result()} единиц энергии')
#
# async def portal_operator():
#     task1 = asyncio.create_task(activate_portal(2))
#     task2 = asyncio.create_task(perform_teleportation(1) if await task1 > 4 else perform_teleportation(await task1))
#     await asyncio.gather(task1, task2)
#     print(f'Результат активации портала: {task1.result()} единиц энергии')
#     print(f'Результат телепортации: {task2.result()} единиц энергии')
#
#
# asyncio.run(portal_operator())


# import asyncio
#
# async def activate_portal(x):
#     print(f'Активация портала в процессе, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x * 2
#
# async def perform_teleportation(x):
#     print(f'Телепортация в процессе, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x + 2
#
# async def recharge_portal(x):
#     print(f'Подзарядка портала, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x * 3
#
# async def check_portal_stability(x):
#     print(f'Проверка стабильности портала, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x + 4
#
# async def restore_portal(x):
#     print(f'Восстановление портала, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x * 5
#
# async def close_portal(x):
#     print(f'Закрытие портала, требуется времени: {x} единиц')
#     await asyncio.sleep(x)
#     return x - 1
#
#
# async def portal_operator():
#     tasks = [
#         activate_portal(2),
#         perform_teleportation(3),
#         recharge_portal(4),
#         check_portal_stability(5),
#         restore_portal(6),
#         close_portal(7)
#     ]
#
#     results = await asyncio.gather(*tasks)
#
#     print(f'Результат активации портала: {results[0]} единиц энергии')
#     print(f'Результат телепортации: {results[1]} единиц энергии')
#     print(f'Результат подзарядки портала: {results[2]} единиц энергии')
#     print(f'Результат проверки стабильности: {results[3]} единиц энергии')
#     print(f'Результат восстановления портала: {results[4]} единиц энергии')
#     print(f'Результат закрытия портала: {results[5]} единиц энергии')
#
# asyncio.run(portal_operator())


# mport asyncio
#
#
# async def task_func():
#     print("Задача запустилась")  # Вывод сообщения при запуске задачи
#     await asyncio.sleep(1)  # Ожидание 1 секунды
#     print("Задача завершилась")  # Вывод сообщения при завершении задачи
#     return "Результат выполнения задачи"  # Возврат результата выполнения задачи
#
#
# async def main():
#     task = asyncio.create_task(task_func())  # Создание новой задачи
#     print('Первая проверка задачи -', task.done())  # Вывод статуса задачи до ее выполнения
#     print("Задача отправилась в цикл событий")  # Вывод сообщения о том, что задача запущена
#     await task  # Ожидание завершения задачи
#     print('Вторая проверка задачи -', task.done())  # Вывод статуса задачи после ее выполнения
#     print("Проверка результата задачи", task.result())  # Вывод результата выполнения задачи
#
# asyncio.run(main())


# import asyncio
#
# async def process_item(item): # Асинхронная функция, обрабатывающая один элемент списка
#     if item == 13 or item == 'i':
#         try:
#             raise ValueError(f"Обработка исключения для элемента: {item}") # Если элемент равен числу 13 или букве 'i', вызываем исключение ValueError
#         except ValueError as _ex:
#             print(_ex)
#     print(f"Элемент соответствует условию: {item}")
#     return item
#
# async def process_list(items): #  Асинхронная функция, обрабатывающая список элементов
#     tasks = [asyncio.create_task(process_item(item)) for item in items] # Создаем асинхронные задачи для каждого элемента списка с помощью list comprehension
#     for task in tasks: # Цикл для обработки каждой задачи
#         try:
#             await task # Если задача успешно завершена, получаем результат
#         except ValueError as e:
#             task.set_exception(ValueError(f'Установленное исключение {e}')) # Если задача вызывает исключение ValueError, устанавливаем исключение для задачи и выводим сообщение
#             print(e)
#
# async def main(): # Асинхронная функция для запуска обработки списка
#     items = [13, 2, 13, 4, 13, 'a', 'b', 'c', 'i', 13, 6, 7, 8, 13, 10, 11, 13, 'i', 'e', 'f', 'i', 'h'] # Список элементов для обработки
#     await process_list(items) # Запускаем обработку списка
# asyncio.run(main())

# import asyncio
# from data import data
#
# async def call_company(dict_data: dict):
#     call_time = dict_data['call_time']
#     name_company = dict_data['Name']
#     phone = dict_data['Phone']
#     await asyncio.sleep(call_time)
#     try:
#         if call_time < 5:
#             print(f'Company {name_company}: {phone} дозвон успешен')
#     except asyncio.CancelledError as e:
#         print(e)
#         # print(f'Company {name_company}: была отменена')
#
#
# async def main():
#     # tasks = [asyncio.create_task(call_company(dict_data)) for dict_data in data]
#     for dict_data in data:
#         tasks = asyncio.create_task(call_company(dict_data))
#         for task in tasks:
#             if await asyncio.wait_for(task, 10):
#                 task.cancel()
#             # print(task)
#
# asyncio.run(main())


# import asyncio
# from data import messages, codes
#
#
# async def async_operation(code):
#     return code
#
# def print_message(task):
#     code = task.result()
#     print(code)
#     for message in messages:
#         print(message)
#
# async def main():
#     for code in codes:
#         task = asyncio.create_task(async_operation(code))
#         await task
#         task.add_done_callback(print_message)
#
#
# asyncio.run(main())

# import asyncio
# from data import verses
#
# async def blacks(i, verse):
#     if i-1 != 0 and i-1 != 7:
#         print(f"{i}{verse}{i-1}")
#         await asyncio.sleep(1)
#     else:
#         print(f"{i}{verse}")
#         await asyncio.sleep(1)
#
# async def main():
#     tasks = [blacks(10-i, verse) for i, verse in enumerate(verses)]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())

# import asyncio
#
# from data import banned_words, message
#
# async def check_message():
#     raise asyncio.CancelledError()
#
#
# async def main():
#     task = asyncio.create_task(check_message())
#     for word in banned_words:
#         for msg in message:
#             if word in msg.get("message").lower():
#                 task.cancel()
#                 print(f'В сообщении {msg.get("message_id")} стоп-слово: {task.done()}')
#             # else:
#             #     print(f'{msg.get("message_id")}: {msg.get("message")}')
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("Задача отменена")
#
# asyncio.run(main())


# import asyncio
# import random
# import itertools
# from data import colors, shapes, actions
#
# async def launch_firework(color, shape, action):
#     await asyncio.sleep(random.randint(1, 5))
#     print(f'Запущен {color} {shape} салют, в форме {action}!!!')
#     return color, shape, action
#
# def finish_firework(task):
#     result = task.result()
#     color = result[0]
#     shape = result[1]
#     action = result[2]
#     print(f'Салют {color} {shape} завершил выступление {action}')
#
# async def main():
#     tasks = []
#     combinations = list(itertools.product(colors, shapes, actions))
#     for color, shape, action in combinations:
#         task = asyncio.create_task(launch_firework(color, shape, action))
#         # task.add_done_callback(finish_firework)
#         tasks.append(task)
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())

# import asyncio
# from random import random
#
# async def producer(queue):
#     print('Производитель: запущен')
#     for i in range(10): # генерация работы
#         value = random() # генерация значения
#         await asyncio.sleep(value) # блокировка для имитации работы
#         await queue.put(value) # добавление в очередь
#     await queue.put(None) # отправка сигнала об окончании
#     print('Производитель: Done')
#
#
# async def consumer(queue):
#     print('Потребитель: Запущен')
#     # выполнение работы
#     while True:
#         item = await queue.get() # получение элемента из очереди
#         if item is None: # проверка сигнала остановки
#             break
#         print(f'>Потребитель получил {item}') # Отчёт
#     print('Потребитель: Done') # все завершено
#
# async def main():
#     queue = asyncio.Queue()
#     await asyncio.gather(producer(queue), consumer(queue))
#
#
# asyncio.run(main())

# import asyncio
# # Создаем экземпляр Lock
# lock = asyncio.Lock()
# async def my_coroutine(id):
#     print(f'Корутина {id} хочет получить блокировку')
#     async with lock:
#         # Код внутри этого блока будет выполняться только одной корутиной в один момент времени
#         print(f'Корутина {id} получила блокировку')
#         await asyncio.sleep(1)
#     print(f'Корутина {id} отпустила блокировку')
#
# # Запускаем несколько корутин
# async def main():
#     await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))
#
# asyncio.run(main())


# import asyncio
# from data import robot_names
#
# lock = asyncio.Lock()
# counter_A = 0
#
# async def start_robot(id_, name):
#     global counter_A
#     async with lock:
#         print(f'Робот {name}({id_}) передвигается к месту A')
#         counter_A += 1
#         print(f'Робот {name}({id_}) достиг места A. Место A посещено {counter_A} раз')
#
#
# async def main():
#     tasks = []
#     for id_, name in enumerate(robot_names):
#         task = asyncio.create_task(start_robot(id_, name))
#         tasks.append(task)
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())


# import asyncio
# import random
#
# # Создаем событие
# event = asyncio.Event()
#
#
# # Определяем корутину number_generator, которая генерирует случайные числа
# async def number_generator():
#     # Проверяем, установлено ли событие
#     event.is_set()
#     # Генерируем список из 5000 случайных чисел от 1 до 100
#     lst = [random.randint(1, 100) for x in range(5000)]
#
#     # Перебираем сгенерированный список
#     for en, i in enumerate(lst):
#         # Ждем от 0 до 0.1 секунды
#         await asyncio.sleep(random.uniform(0, .1))
#         # Если число равно 33, устанавливаем событие
#         if i == 33:
#             event.set()
#             # Выводим номер генерируемого числа
#         print(f"Генерируем число: {i}")
#         # Если событие установлено, выходим из цикла
#         if event.is_set():
#             # Выводим сообщение, что число найдено и за сколько попыток
#             print(f'Событие наступило, число {i} найдено, через {en} попыток')
#             break
#
#
# # Определяем функцию main, которая запускает number_generator через asyncio.gather
# async def main():
#     await asyncio.gather(number_generator())
#
#
# # Запускаем функцию main через asyncio.run
# asyncio.run(main())


# import asyncio
# from data import ips
#
#
# async def sensor_1(id, ip, alarm):
#     print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
#     alarm.set()
#     await asyncio.sleep(5)
#
# async def sensor_2(id, ip, alarm):
#     print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
#     alarm.set()
#     await asyncio.sleep(5)
#
# async def sensor_3(id, ip, alarm):
#     print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
#     alarm.set()
#     await asyncio.sleep(5)
#
# async def sensor_4(id, ip, alarm):
#     alarm.set()
#     print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
#     await asyncio.sleep(5)
#
# async def sensor_5(id, ip, alarm):
#     alarm.set()
#     print(f'Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания')
#     await asyncio.sleep(5)
#
# async def manager(id, ip, alarm):
#     if ip == '192.168.0.1':
#         await sensor_1(id, ip, alarm)
#     elif ip == '192.168.0.2':
#         await sensor_2(id, ip, alarm)
#     elif ip == '192.168.0.3':
#         await sensor_3(id, ip, alarm)
#     elif ip == '192.168.0.4':
#         await sensor_4(id, ip, alarm)
#     elif ip == '192.168.0.5':
#         await sensor_5(id, ip, alarm)
#
#     print('Датчики зафиксировали движение')
#     if alarm.is_set():
#         print(f'Датчик {id} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')
#
#
# async def main():
#     alarm = asyncio.Event()
#     tasks = []
#     for id, ip in enumerate(ips):
#         tasks.append(asyncio.create_task(manager(id, ip, alarm)))
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())


# import asyncio
# from data import users
#
# async def name(condition, user):
#     async with condition:
#         print(f'Пользователь {user} ожидает доступа к базе данных')
#         await condition.wait()
#         print(f'Пользователь {user} отключается от БД')
#
# async def controller(condition):
#     user = 'alice'
#     async with condition:
#         print(f'Пользователь {user} подключился к БД')
#         condition.notify()
# async def main():
#     condition = asyncio.Condition()
#     tasks = []
#     for user in users:
#         task = asyncio.create_task(name(condition, user))
#         tasks.append(task)
#     await asyncio.gather(*[controller(condition), *tasks])
#
# asyncio.run(main())

# import asyncio
# sem = asyncio.Semaphore(3) # Семафоры используются для ограничения одновременно выполняемых задач до указанного количества (в данном случае до трех)
# async def task(id):
#     async with sem: # Контекстный менеджер используется для автоматического освобождения ресурсов после использования
#         print(f'Задача {id} начала выполнение') # Информируем о начале выполнения задачи
#         await asyncio.sleep(1) # Имитируем работу задачи, приостанавливая выполнение на 1 секунду
#     print(f'Задача {id} завершила выполнение') # Информируем о завершении выполнения задачи
#
# async def main():
#     tasks = [task(i) for i in range(50)] # Создаем список из 50 задач
#     await asyncio.gather(*tasks) # Используем asyncio.gather для одновременного выполнения всех задач
#
# # Запускаем все задачи
# asyncio.run(main())

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
#
# print(a==b)
# print(a==c)
# print(a is b)
# print(a is c)

# a = 'hello world'
# b = a
# c = 'hello world'
# print(a==b)
# print(a is b)
# print(a==c)
# print(a is c)
#
# print(id(a))
# print(id(b))
# print(id(c))

a = (1, 2, 3)
b = a
c = (1, 2, 3)

print(a==b)
print(a is b)
print(a==c)
print(a is c)