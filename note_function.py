#Created by:- Rohit kumar
#Email:-rohit03112005sah@gmail.com
import notes
#import math
num = int(input("Enter the amount:"))
#print(math.pi)
k,k1,k2,k3,k4,k5,k6,k7 = 500,100,50,20,10,5,2,1
if num>=k:
    num, a = calc(num, k)
    print("Maximum notes of 500:",a)
if k1<=num<k:
    num, c = calc(num, k1)
    print("Maximum notes of 100:",c)
if k2<=num<k1:
    num, e = calc(num, k2)
    print("Maximum notes of 50:",e)
if k3<=num<k2:
    num, g = calc(num, k3)
    print("Maximum notes of 20:",g)
if k4<=num<k3:
    num, i = calc(num, k4)
    print("Maximum notes of 10:",i)
if k5<=num<k4:
    num, k = calc(num, k5)
    print("Maximum notes of 5:",k)
if k6<=num<k5:
    num,m = calc(num,k6)
    print("Maximum notes of 2:",m)
    print("Maximum notes of 1:",num)


