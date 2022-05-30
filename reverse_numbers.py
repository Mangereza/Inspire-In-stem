#!/usr/bin/python

#program to write numbers in reverse
#input is 700
#output is 007

number=5678

reversed_number_string=str(number)[::-1]
if type (number) == float:
    reversed_number=float(reversed_number_string)
elif type(number)==int:
    reversed_number=int(reversed_number_string)

print(reversed_number)

number = 67890
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
    
print(reversed_number)

number = 67890.123
reversed_number_string = str(number)[::-1]
if type(number) == float:
    reversed_number = float(reversed_number_string)
elif type(number) == int:
    reversed_number = int(reversed_number_string)
    
print(reversed_number)

def reverse_number(number):
    """Reverses a number (either float or int) and returns the appropriate type.
    Args:
        number (int|float): the number to reverse
    Returns:
        int|float: the reversed number
    """
    if type(number) == float:
        return float(str(number)[::-1])
    elif type(number) == int:
        return int(str(number)[::-1])
    else:
        print('Not an integer or float')

