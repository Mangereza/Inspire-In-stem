#!/usr/bin/python
start_num=int(29)
end_num=int(36)
cnt=start_num

while cnt <=end_num:
    if cnt% 7 ==0 and cnt % 5==0 :
        print(cnt, "is divisible by 7 and 5")
    cnt+=1


x = int(input("enter number:"))
if (x % 7==0) or (x %5==0):
    print (f"the number {x} is divisible by 7 or 5")
else:
    print(f"the number {x} is not divisible by 7 or 5")
