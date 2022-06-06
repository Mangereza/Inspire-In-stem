#!/usr/bin/python

######################
#   Project : Passwords
#   Name    : Stephanie Mangereza
#   Date    : 03 /06 /2022
######################

#Ask user numbers of passwords they want to generate 
#covert the num_password into integer
#Ask user for password/length and covert
 
import random
print('Welcome to our python generator')
characters='grandmahen1256'
password_length=12
num_password=4
for password in range (num_password):
    password=''
    for c in range (password_length):
        password+=random.choice(characters)
    print(password)