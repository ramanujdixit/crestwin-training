# What is Data types?
# data types in python is the way to classify data items and perform their respective operations.

# types:
# int, float, complex numbers, str, bool, list tuple, set, dictionary.

# and python is a dynamic type language in which interpreter define type of data at runtime based on what value we assign to a variable.

# 1. int: if dtype of variable is int it shows numeric values which does not have decimal.
# 2. float:if dtype of variable is float it shows numeric values which have decimal.
# 3. str:if dtype of variable is str it shows it contains a word or sentence.

# list:
# it is types of data structure which is used to store multiple heterogenous elements in a variable
# is is ordered and mutable.

# tuple:
# it is not mutable but its ordered.

# set:
# is is unordered and mutable and duplicates are not allowed.

# dictionary:
# Python is a collection of data values, used to store information like a map.
# it stores a value in a key-pair form. each key pair are separated using (:) colon.

# example: accessing an element in dictionary
# d = {'name': 'Ramanuj', 'lname': 'dixit'}
# print(d['name'])
# print(d.get('name'))

# Comprehensions:
# short and clean way of creating list generators sets and dictionaries
# list comprehensions
# set comprehensions
# dictionary comprehensions
# generator comprehensions

# Unpacking
# *- list and tuple
# **- dictionary

# type():
# it is used to find the data type of variable
# also sed to create a new class with attributes.

# f-strings:
# f strings in python is used for formatting, interpolation.

# string methods:
# string methods are the methods used in strings to make manipulation in strings easier like .upper(), capitalize() etc.

# slicing:
# taking out particular portion from list strings tuple is known as slicing.
# a='ram'
# a[start:stop:step]

	






# a=2
# print(type(a))

# b=2.3
# print(type(b))

# c=True
# print(type(c))

# l1=[1,2,3,4,5]
# for i in l1:
#     print(i)

# d={'a':25, 'b':30}
# for i in d:
#     print(i)
#     print(d[i])

# list_comp=[x**2 for x in [1,2,3,4,5]]
# print(list_comp)

# list_comp_2=[x**2 for x in [1,2,3,4,5] if x%2==0]
# print(list_comp_2)

# s='my name is rAmaNuj'
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())

# l2=[1,2,3,4,5]
# l2.append(6)
# print(l2)
# l2.pop(5)
# print(l2)

# def info(name='guest'):
#     return name

# print(info())
# print(info(name='ramanuj'))


# def info(name, age):
#     return f'My name is {name}, and my age is {age}.'

# r={'name':'Ramanuj Dixit', 'age': 50}

# print(info(**r))

# s='ramanuj'
# print(s[1:2])
# print(s[2:5])
# print(s[::-1])

