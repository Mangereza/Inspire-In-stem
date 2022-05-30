#!/usr/bin/python

a=int(input("enter the first number"))
r=int(input("enter the common ratio"))
n=int(input("enter the number of terms"))

def printGp(a,r,n):
    for i in range(0, n):
        current_term= a * pow(r, i)
        print(current_term)

printGp(a,r,n)
