#!/usr/bin/python

######################
#   Functions
#   Name    : Stephanie Mangereza
#   Date    : 31 /5 /2022
######################

#functions is a block of code which gets executed together
#initializing the function is saying what the function does
#calling the function happens after creating and initializing the functions

#Defining a function

def say_hello():
    #print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    #print(z)
#say_hello()

#def sounds():
    #print("Dogs bark woof woof")
    #print("cats meows meow meow")
    #print("cow moows moow moow")
#sounds()

#def neigh():
    #print("donkeys neigh")
#def meow():
    #print("cats meow meow")
#def moowing():
    #print("cows mooow moooow")
#neigh()
#meow()
#moowing()

#def add_numbers(x,y):
#    sum_numbers=x+y
#    print("the sum of numbers:",sum_numbers)
#add_numbers(40,50)
#add_numbers(100,450)
#add_numbers(1,4)

#def product_numbers(a,b):
#   multiply_numbers=a*b
#    print("the product of numbers:",multiply_numbers)
#product_numbers(40,50)
#product_numbers(100,450)
#product_numbers(1,4)

def print_name(name="Bob Afwata"):
    print(name)

print_name("Joseph")

#return from a function
def get_sum(num1,num2):
    sum_nums=num1+num2
    return sum_nums
print(get_sum(7,12))

#square of numbers

def powers(number,power):
    pow_num=number**power
    return pow_num
print(powers(6,4))

#getting full names

def get_full_names(F_name,S_name):
    full_name=F_name + S_name
    return full_name
print(get_full_names("Stephanie " , "Mangereza"))

#returning a dictionary from a function 

def create_full_name(first_name,second_name):
    person={'first':first_name,'second':second_name}
    return person
student=create_full_name('Stephanie','Mangereza')
print (student)

#parsing a list in a function

def greet_friends(names):
    for name in names: 
        msg="Hello " + name.title() + "!"
        print (msg)
friends=['Cassandra','Debby','Makai','Racheal','James','Kendi']
greet_friends(friends)