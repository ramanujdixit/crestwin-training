# Advanced OOPS
# abc:
# an Abstract Base Class defines required or forces us to follow a particular structure.
# any subclass have to implement all the abstractmethod compulsorily before it can be instantiated.


# Decorators:
# decorator is function that takes another function as in put and adds some functionality to it and returns it.
# -this can be possible because python is first class citizens i.e. objects in programming language on which all the operations can be performed.


# from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")

#     def speak(self):
#         print("Dog Barks")


# d = Dog()
# d.speak()
# d.sound()


# def my_decor(func):
#     def wrapper():
#         func()
#         print("_________")

#     return wrapper


# @my_decor
# def name():
#     print("Ramanuj")


# name()

from functools import wraps


# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args):
#         print("********")
#         func(*args)
#         print("********")

#     return wrapper


# @my_decorator
# def info():
#     """this will give us information"""
#     print("My name is Ramanuj")


# print(info.__name__)
# print(info.__doc__)


# def check_zero(func):
#     def wrapper(a, b):
#         if b == 0:
#             print("denominator cant be zero")
#             return

#         func(a, b)

#     return wrapper


# @check_zero
# def divide(a, b):
#     print(a / b)


# divide(8, 0)

# import logging

# logging.basicConfig(
#     filemode="w",
#     filename="app.log",
#     level=logging.DEBUG,
#     format="%(asctime)s:%(levelname)s:%(name)s:%(message)s:%(process)s:%(lineno)s",
#     # datefmt=
# )
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")

# f = open("f1.txt", "w")
# f.write("hello world")
# f.close()
# with open("f1.txt", "r") as f:
#     print(f.read())
