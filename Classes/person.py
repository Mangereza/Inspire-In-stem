#!/usr/bin/python

######################
#   Classes
#   Name    : Stephanie Mangereza
#   Date    : 02 /06 /2022
######################

class Person:
    def __init__(self, _name, _age):
        self.name= _name
        self.age= _age

    def sayHi (self):
        print('Hello, my name is ' + self.name,  ' I am ' + self.age + ' years old.')
person1 = Person("Bob",str (16))
person1.sayHi()

person2 = Person("Sarah",str (21))
person2.sayHi()
