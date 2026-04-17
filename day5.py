# what is oops?
# oops stands for object oriented programming its a way of organizing code using class and objects.
# - it makes code modular
# - is makes code easily maintainable
# - though it have four pillars likes encapsulation, inheritance, polymorphism, abstraction which provides code a functionality of binding together, security etc.

# what is class?
# class is a blueprint to create a object.

# what is __init__?
# it is a special type of function known as constructor which run automatically when object is created.

# what is self?
# self refers current object which is used to access instance variable.

# what is inheritance in oops?
# it is a concept  of oops which allows a class to inherit methods and attributes from another class.
# advantages:
# -code reusability -simplifies maintainence - enebales method overriding

# super() function:
# it is used to call the parent class methods.
# - commonly used in child class's __init__ to initialize inherited attributes.
# - it ensures that parent class functionality is reused without needing to rewrite the code in child class.

# types of inheritance
# single inheritance- derived class to inherit properties from single parent class.
# mulitple inheritance- derived class inherits properties from more than one base class.
# multilevel inheritance - features of base class and child class are further inherited in derived class.
# heirarchical inheritance - more than one derived classes from a single parent class.
# hybrid inheritance- combination of more than one type of inheritance, it can be mix of single , multiple, multilevel inheritance.

# MRO:
# it defines the order in which python searches for a method in a class adn base classes
# it becomes important because more than one class have same methods.
# it uses c3 linearization algorithm it says it uses order in which parent classes are witten.

# class methods:
# class methods are special type of methods in which class has been passed as a first agrument with a convention name as cls.
# they are used to operate on class level data.
# they helps in modifying class varibles and creating factory methods.

# static methods:
# static methods are as normal as normal function which have a particular utility like helper function.
#  they dont recieve cls or self automatically
# placed inside class for logical grouping
# still belongs to class's namespace.


# what is class attributes?
# class attributes belongs to class itself they can be shared by all the instances, such attributes are defined under class body parts at the top.


# what is instance attributes?
# unlike class attributes, instance attributes are not shared by objects, instead each objects have there own attributes.


# Inheritance
# class Animal():
#     def __init__(self,name):
#         self.name=name

#     def info(self):
#         return F"Animal name: {self.name}"

# class Cat(Animal):
#     def speak(self):
#         return F"{self.name} meows"

# c=Cat('Kitten')
# print(c.info())
# print(c.speak())


# using super()
# class Person:
#     def __init__(self, name):
#         self.name=name

#     def give_name(self):
#         return F"my name is {self.name}"

# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary=salary

#     def info(self):
#         return f"Name: {self.name}, Salary:{self.salary}"

# a1=Employee('Rohit', 6200)
# print(a1.info())


# Multilevel Inheritance
# class Grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername=grandfathername

# class Father(Grandfather):
#     def __init__(self, grandfathername, fathername):
#         super().__init__(grandfathername)
#         self.fathername=fathername
# class Son(Father):
#     def __init__(self, grandfathername, fathername, sonname):
#         super().__init__(grandfathername, fathername)
#         self.sonname=sonname
#     def info(self):
#         print("GrandFather name:", self.grandfathername)
#         print("Father name:", self.fathername)
#         print("Son name:", self.sonname)
# obj=Son("Kishore","Kamal","Kamal Kishore")
# obj.info()


# Heirarchical Inheritance
# class Father:
#     def advise(self):
#         print("Father advise are always best")
# class Son(Father):
#     def sometime(self):
#         print("Listens Sometimes")
# class Daughter(Father):
#     def always(self):
#         print("Father always listens to her")

# r=Son()
# k=Daughter()
# r.advise()
# r.sometime()
# k.advise()
# k.always()


# class Simple:
#     pass


# class Two:
#     def __init__(self, name):
#         self.name=name

#     def print_name(self):
#         return f"My name is {self.name}"

# obj=Two('Kishore')
# print(obj.print_name())


# encapsulation
# class Bank:
#     def __init__(self, amount, balance):
#         self.amount=amount
#         self.__balance=balance

#     def withdraw(self):
#         if self.amount<self.__balance:
#             self.__balance-=self.amount
#             return f'{self.amount} is withdrawn successfuly'
#         return f'Insufficient funds'

#     def deposit(self):
#         self.__balance+=self.amount
#         return f'{self.amount} is deposited successfuly'

#     def get_balance(self):
#         return f'Balance:{self.__balance}'

# a=Bank(5000,15000)

# print(a.deposit())
# print(a.get_balance())

# dunder methods
# class Magic:
#     def __init__(self,marks):
#         self.marks=marks

#     def __eq__(self, other):
#        return self.marks==other.marks

#     # def __str__(self):
#     #     return 'Nice Output'


#     def __add__(self, other):
#         return self.marks+other.marks

#     def __repr__(self):
#         return 'Magic'

# s1=Magic(85)
# s2=Magic(85)
# print(s1==s2)
# print(s1+s2)
# print(s1)
# print(s2)


# class method      - factory method
# from datetime import date
# class Age:
#     def __init__(self, age):
#         self.age=age

#     @classmethod
#     def display_age(cls, year):
#         age=date.today().year-year
#         return cls(age)

# a=Age.display_age(2000)
# print(a.age)
