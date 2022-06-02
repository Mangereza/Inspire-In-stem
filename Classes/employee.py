#!/usr/bin/python

######################
#   Classes
#   Name    : Stephanie Mangereza
#   Date    : 02 /06 /2022
######################


class employee:
    def __init__(self, _name, _salary,_ID):
        self.name =_name
        self.salary =_salary
        self.ID=_ID

    def sayHi(self):
        print("Hello, my name is " + self.name, " my salary is " + self.salary,  " Kenyan shillings "  " my ID " +self.ID)
employee1 = employee("Bob", str(30000), str(91736536))
employee1.sayHi()

