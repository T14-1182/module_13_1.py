# Домашнее задание по теме "Асинхронность на практике"
# импорт необходимых библиотек
import asyncio

# объявление асинхронной функции (корутины) start_strongman
async def start_strongman(name: str, power: int):
    # количество шаров
    ball = 5
    # вывод на консоль начала выступления силача
    print(f'Силач {name} начал соревнования.')
    # цикл выступления силача
    for i in range(ball):
        # оператор await внутри асинхронной функции приостанавливает
        # выполнение одной операции до завершения другой асинхронной операции
        # и задержка на выполнение операции (asyncio.sleep())
        await asyncio.sleep( 1 / power)
        # вывод на консоль выполненой операции
        print(f'Силач {name} поднял {i+1} шар')
    # вывод на консоль окончания выступления силача
    print(f'Силач {name} закончил соревнования.')

# объявление асинхронной функции (корутины) start_tournament
async def start_tournament():
    # задачи для параллельного выполнения
    task1 = asyncio.create_task(start_strongman('Pasha', 6))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    # оператор await внутри асинхронной функции приостанавливает
    # выполнение одной операции до завершения другой асинхронной операции
    await task1
    await task2
    await task3

# метод для запуска асинхронной функции start_tournament
asyncio.run(start_tournament())