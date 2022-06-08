#!/usr/bin/python

######################
#   Classes : Vehicle Class
#   Name    : Stephanie Mangereza
#   Date    : 03 /06 /2022
######################

#function which return reverse 

def  isPalindrome (s):
    return s== s[::-1]

#driver code

s = "malayalam"
ans = isPalindrome (s)

if ans: 
    print("yes")
else:
    print("no")

#function to check string is palindrome or not

def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range (0, int(len(str)/2)):
        if str [i] != str[len(str)-i-1]:
            return False
        return True
#main function
s="radar"
ans= isPalindrome

if (ans):
    print("yes")
else:
    print("no")

#if string ia a palindrome

x="ere"

w=""
for i in x:
    w = i + w
if (x==w):
    print("This is a palindrome")
else:
    print("This is not a palindrome")

#to check if a number is a palindrome

num = input ('Enter any number')
try:
    val = int(num)
    if num == str(num)[::1]:
        print('The given number is a Palindrome')
    else:
        print('The given number is not a palindrome')
except ValueError:
    print('That is not a valid number')
