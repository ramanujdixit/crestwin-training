# Iteration:
# Iteration us a general term for taking each item of something after another.


# Iterator:
# An iterator is an object that allows the programmer to transversethrough a sequence of data without storing entire data in memory.
# -memory efficient
# -instead of loading eerything once, iterators give one item at a time.


# Iterable:
# iterable is an object, which one can iterate over.it generates an iterator when passed inter() method.

# to check that any obj is iterable:
# -using dir() function it will give all the function just check if it contains iter() function if yes then it is a iterable.

# to check if any obj is iterator:
# -using same dir() look for iter() as well as __next__() if yes then it is a iterator.


# Generators:
# they are the special function for creating iterators.
# - it does not return all values at once.
# -it yields value one by one.
# -it uses yield keyword instead of return.

# Generator Expression:
# it is a single line creation of generators same like list comprehension.
# ex:
# gen = (x**2 for x in range(1, 5))
# print(list(gen))


# itertools:
# it is a module provides a set of fast, memory efficient tools for working with iterables.

# -itertools.chain():
# it combines differet iterables into one continous stream.
# ex:
# a = [1, 2, 3]
# b = [4, 5]
# c = [6]

# result = chain(a, b, c)
# print(list(result))


# -itertools.islice():
# it is used to slice iterator.
# -iterator does not supports slicing.
# -islice() solves this.

# from itertools import chain, groupby, islice

# num = range(1, 10)
# result = islice(num, 2, 7)
# print(list(result))

# =itertools.groupby():
# it groups consecutive elements of an iterable that have same value.
# ex:
# my_list = [1, 1, 2, 3, 2, 3]

# for key, group in groupby(sorted(my_list)):
#     print(key, list(group))


# Lambda:
# Lamda functions are anonymous small function of single line which implements logic on a single line.

# ex:
# name = "ram"
# upper = lambda x: x.upper()
# print(upper(name))

# num = int(input("enter any number:"))
# check_integer = lambda x: "Positive" if x > 0 else "Negative"
# print(check_integer(num))

# -filter:
# it is usd to filter particular elements of a list based on the given condition.
# ex:
# nums = [i for i in range(1, 25)]
# even = filter(lambda x: x % 2 == 0, nums)
# print(list(even))

# -map():
# it is used to map values or elements of given list based on the given condition.
# ex:
# nums = [i for i in range(5)]
# squares = map(lambda x: x**2, nums)
# print(list(squares))

# functools.reduce():
# it is a type of function which will reduce a value of whole list to a one value like it performs a aggregation on whole list.
# ex:
# from functools import reduce, lru_cache, partial

# nums = [1, 2, 3, 4, 5]
# addition = reduce(lambda x, y: x + y, nums)
# print(addition)

# multiplication = reduce(lambda x, y: x * y, nums)
# print(multiplication)

# largest = reduce(lambda x, y: x if x > y else y, nums)
# print(largest)

# - functools.partial
# fix some arguments of a function, creating a new function.

# - functools.lru_cache()
# Cache(stores) results of recent function calls, avoids recomputing.
# -used as a decorator @lru_cache
# lru=Least Recently Used


# def my_own_for_loop(interable):

#     iterator = iter(interable)

#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break


# this shows if on any iterator we use iter then it will return same iterator as there ids are same its been proved.
# num = [1, 2, 3]
# iter_num = iter(num)
# print(id(iter_num))
# iter_num2 = iter(iter_num)
# print(id(iter_num2))


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_own_for_loop(my_list)


# def generator():
#     yield "Hello World"
#     yield "Welcome to World of code"
#     yield "Vamosss!!"


# obj = generator()

# print(next(obj))
# for i in obj:
#     print(i)
