#!/usr/bin/python

######################
#   loops   : for loops if else
#   Name    : Stephanie Mangereza
#   Date    : 24 /5 /2022
######################

acc_bal= input("enter your acc_bal")

if  (int(acc_bal) > 100000 and int(acc_bal) < 200000):
     acc_bal = acc_bal - 25000
     print(" we have deducted ksh 25000/n")
     print("your new balance is 25000")
elif (int(acc_bal) > 500000 and int(acc_bal) < 1000000):
       acc_bal = float(acc_bal) - (0.3*float(acc_bal))
       print(" we have deducted 30 percent from your account")
elif (int(acc_bal) > 1000000):
    acc_bal = acc_bal- 15000
    print(" We have deducted ksh15000 from your account")
else :
    print("No deduction done")