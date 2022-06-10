#!/usr/bin/python

######################
#   Project : Assignment passwords
#   Name    : Stephanie Mangereza
#   Date    : 03 /06 /2022
######################

#generate the password and username

username = input("Please enter your username : ")
password = input("Please enter your password : ")
print ("Greetings," , username, "you are now logged in now with a password")

command = input("Please type a command :")
if command == "log off":
    print ("You have now been logged off again",username)
username == ""
password == ""

username = input("Please enter your username : ")
password = input("Please enter your password : ")

while (username != "username" and password != "password"):
    print (" Sorry username and password incorrect please re-enter for validation ")

username = input("Please enter your username : ")
password = input("Please enter your password : ")

print ("Greetings," , username, "you are now logged in now with your password")
