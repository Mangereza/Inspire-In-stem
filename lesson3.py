#!/usr/bin/python

######################
#   loops   : for loops
#   Name    : Stephanie Mangereza
#   Date    : 23 /5 /2022
######################

for i in range(4) :
    for j in range(4-i) :
        print("*",end="")

    print()

row = int(input("enter the number of rows: "))

for i in range(row) :
    print(" "*(row-i)+" *"*(i+1) )


    
for j in range(row-1) :
    print(" "*(j+2)+" *"*(row-1-j))


for i in range(row) :
    print(" "*(row-i)+" *"*(i+1) )

for i in range(4) :
    for j in range(4-i) :
        print("*",end="")

    print()
    