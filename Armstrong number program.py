#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

print("Program tc check whether the given number is armstrong or not")
num = int(input("Enter any integer:"))
import math
sum_armstrong = 0
if num<100:
    c = (num//10)
    d = num%10
    sum_armstrong = math.pow(c,3)+math.pow(d,3)    
elif num<1000:
    e = (num//100)
    h = ((num%100)//10)
    d = (num%10)
    sum_armstrong = math.pow(e,3)+math.pow(h,3)+math.pow(d,3)
elif num<10000:
    g = (num//1000)
    f = ((num%1000)//100)
    h = ((num%100)//10)
    d = (num%10)
    sum_armstrong = math.pow(g,3)+math.pow(f,3)+math.pow(h,3)+math.pow(d,3)
elif num<100000:
    i = (num//10000)
    k = ((num%10000)//1000)
    f = ((num%1000)//100)
    h = ((num%100)//10)
    d = (num%10)
    sum_armstrong = math.pow(i,3)+math.pow(k,3)+math.pow(f,3)+math.pow(h,3)+math.pow(d,3)
if sum_armstrong == num:
    print(1)
else:
    print(0)


