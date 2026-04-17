# control flow:
# control flow statements are the statements which are used to control the flow of code that needs to be executed.
# controlling statements
# if else
# if elif else

# looping statements:
# for
# while

# jumping statements
# continue
# break
# return


# functions:
# a function in python is defined using def keyword, a function is re-useable block of code which have particular operation to perform.
# example:
# def reverse_string(s):
#    return s[::-1]

# return is used to return a output and then terminating the loop.

# *args:
# when we dont know how many number of positional arguments will be passed in function then we simply use *args.

# args is just a name → you can write anything
# def test(*numbers):
#     print(numbers)

# **kwargs:


# scope in python:
# scope in python means a particular variable can be accessed from which part of location in a code.

# different scopes in python:

# local: local scopes means if a variable is defined inside a function then it can only be accessed inside that function.
# global: global scope means a variable can be accessed from anywhere in a code no matters if its defined inside a function or not.
# enclosing: enclosing scope means if there are two function outer and inner function then outer functions variable is accessed in inner function but inner functions variable is not accessible in outer function.
# built-in: contains all predefined functions and objects in python like print(), len() etc.


# modules:
# a file saved with .py extension is a module.
# and using import we can import the user created as well as built in modules or any specific function from that module.

# stdlib: standard library- python comes with built in libraries , no need of installation.

# 1.OS library:
# it is used to interact with os files.
# some functions are:
# os.getcwd()
# os.listdir()
# os.mkdir()
# os.rmdir()
# os.path.exists()
# os.rename()

# 2.sys module:
# it is used for system level interaction.
# some functions are:
# sys.version
# sys.argv
# sys.exit()

# 3. Pathlib:
# it is used for path handling but its cleaner and style is object oriented like we create a object of Path and then using it we access methods or functions of lib.
# some functions are:
# p=Path()
# p.exists()
# p.name
# p.suffix
# p.mkdir()
# p.touch()


# note:
# os.path.exists() in os and Path.exists() in pathlib both have same functionality
# os.path.join() in os and / operator also used to perform same tasks.
# os is procedural type and pathlib is object oriented type.


# prime number for loop and controlling statement
# num=int(input('enter any number:'))

# isprime=True

# if num<2:
#     print('Prime Number')
# else:
#     for i in range(2,(num//2)+1):
#         if num%i==0:
#             isprime=False

# if isprime:
#     print('Prime Number')
# else:
#     print('Not a prime number')


# reverse a number for while loop practice
# num=int(input('enter any number:'))
# rem=0
# rev_num=0

# while num>0:
#     rem=num%10
#     rev_num=rev_num*10+rem
#     num=num//10

# print(rev_num)

# def information(name='Varun', salary=2000):
#     return f"My name is {name} and my salary is {salary}"

# print(information())
# print(information(name='Lal', salary=3500))

# def local_scope():
#     name='Rakul'
#     print(name)

# local_scope()
# print(name)    cannot access it as its scope is local

# def global_scope():
#     global l_name
#     l_name='aaron'
#     print(l_name)
# global_scope()
# print(l_name)       it is accessible as its scope is global


# def outer():
#     a='raj'

#     def inner():
#         print(a)      it will be printed as outer scope variable is accessed in inner function

#     inner()
# outer()


# def outer():
# print(a)    it will not printed as its in inner function variable and we are trying to access it in outer function

#     def inner():
#         a='raj'
#         print(a)     this will get executed
#     inner()
# outer()


# import os

# print(os.getcwd())

# print(os.listdir())

# os.mkdir('test')
# print(os.listdir())

# os.rmdir('test')
# print(os.listdir())


# *args
# def sum(*args):
#     total=0
#     for i in args:
#         total+=i
#     print(total)
# sum(1,2,3)

# def print_i(*args):
#     print(args)
# print_i(1,2,3,4,5,6,7,8,9,10)

# def get_number(*number):
#     for i in number:
#         print(i)

# get_number(1,2,3)


# **kwargs
# def print_details(**kwargs):
#     print(kwargs)

# print_details(name='lala', age=25)

# def func(**info):
#     return info["name"]

# print(func(name="Ram", age=22))

# def func(a, *args, **kwargs):
#     print(a, args, kwargs)

# func(10, 20, 30, x=40)
