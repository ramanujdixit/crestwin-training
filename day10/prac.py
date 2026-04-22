# Async Python:

# -async is a keyword in pythn which is used to define asynchronous functions.
# -allows task to run wothout blocking the execution of other code.

# await:
# await is used to execute a coroutine and pause the current function until it completes,without blocking the program.
# -it only works inside async function.
# -it allows other taks to run while waiting.

# event loop:
# it is a core engine of async python that manages and runs all asynchronous tasks.
# it checks whcih task is ready and runs it.

# asyncio.run(main()):
# this is used to start event loop and execute main async function.

# asyncio.gather():
# it is used to run multiple async functions concurrently and wait for all of them to finish.
# -it starts task in a sequential way.

# asyncio.create_task():
# schedules and starts the task immediately and await determine when we pause to retrieve result.

# multithreading:
# python allows multiple threads to run concurrently enabling efficient multitaasking.
# it seems that multiple threads are working parallely but they work concurrently means one after another.
# when one thread stops or sleeps then next thread runs because of gil.
# gil is global interpreter lock which passes only one thread at a time.
# ex:
# mainly used in i/o bound tasks.
# like in ms word one thread is responsible for typing , and another is to check spelling.

# multiprocessing:
# Multiprocessing refers to the ability of a system to support more than one processor at the same time.
# this is an example of pure parallelism.
# computer have only sngle processor, and if multiple tasks are assigned to it then it have to interpypt each taks.
# and switch breifly between tasks so as to keep all of them going.
# if we do this then we can not keep the track of all of them.
# cpu can easily executes several tasks at once with each task having its own processor.

# type hint:
# it is a feature in python that allows developer to annotate the types of variables as well as functions.

# optional type :
# it returns value that are hinted or returns none.


# list[str]:
# this is again a type hint hinting that the object should be list but having string elements.

# mypy:
# it is a static type hint checker.
# pythin does not enforces type hint it will execute and also can through errors.


# import asyncio

# import time


# def name():
#     time.sleep(3)
#     print("Ramanuj Dixit")


# async def hello():
#     print("hello world")
#     await asyncio.sleep(1)
#     print("second statement")


# name()
# asyncio.run(hello())


# import asyncio


# async def brand():
#     await asyncio.sleep(2)
#     print("is a car of BMW")


# async def car():
#     print("M4 Competition")
#     await asyncio.sleep(1)
#     print("code done")


# async def main():
#     t1 = asyncio.create_task(car())
#     t2 = asyncio.create_task(brand())

#     for i in range(3):
#         print("working", i)
#     await t2
#     await t1


# asyncio.run(main())


# async def task1():
#     await asyncio.sleep(2)
#     print("Task1 done")


# async def main():
#     t1 = asyncio.create_task(task1())

#     for i in range(3):
#         print("Working...", i)
#         await asyncio.sleep(1)

#     await t1


# asyncio.run(main())


# async def task1():
#     await asyncio.sleep(5)
#     print("task 1 entered")


# async def task2():
#     await asyncio.sleep(3)
#     print("task2 entered")


# async def main():
#     t1 = asyncio.create_task(task1())
#     t2 = asyncio.create_task(task2())

#     await asyncio.sleep(2)
#     print("waiting to get printed")

#     await t1
#     await t2


# asyncio.run(main())


# async def task1():
#     await asyncio.sleep(5)
#     print("task 1 entered")


# async def task2():
#     await asyncio.sleep(3)
#     print("task2 entered")


# async def main():
#     print("waiting to print")
#     await asyncio.gather(task1(), task2())


# asyncio.run(main())
from typing import List, Optional, Dict

# def add(a: int, b: int) -> Optional[int]:
#     return a + b


# print(add(5, 5))


# def add(*args: int):
#     total = 0
#     for i in args:
#         total += i
#     return total


# print(add(2, 3, 4, 5))


# def my_dict(d: Dict[str, str]):
#     return d


# print(my_dict({"name": "ram", "lname": "lal"}))


# def add(l1: List[int]):
#     return sum(l1)


# print(add([1, 2, 3, 4, 5]))


# def my_list(list1: List[str]):
#     return list1


# print(my_list(["ram", "shyam"]))

# import threading
# import time


# def square(num):
#     print(f"Square: {num*num}")
#     time.sleep(1)


# def cube(num):
#     print(f"Cube: {num*num*num}")
#     time.sleep(1)


# t1 = threading.Thread(target=square, args=(4,))
# t2 = threading.Thread(target=cube, args=(4,))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print("Done!")

import asyncio


# async def name():
#     await asyncio.sleep(3)
#     print("Rohan")


# async def hello():
#     print("Hello")


# async def main():
#     for i in range(2):
#         print("nothing to print")
#         await asyncio.sleep(1)
#     await asyncio.gather(name(), hello())


# async def main():
#     t1 = asyncio.create_task(name())
#     t2 = asyncio.create_task(hello())
#     for i in range(2):
#         print("Nothing to work")
#         await asyncio.sleep(1)
#     await t1
#     await t2


# asyncio.run(main())
