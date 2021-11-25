#Created by:-Rohit kumar
#Email id:- rohit03112005sah@gmail.com

from Combination_o import addition,reverse,odd,even,prime,natural,perfect,AP,LCM,HCF,factor,sum_prime,sum_odd,Area

print("1.to get addition of digits")
print("2. to get sum_odd")
print("3. to get sum_even")
print("4. to know either the given number is odd or even")
print("5. to get sum_prime")
print("6. to know either the given number is prime or not")
print("7. to get factor of a number")
print("8. to get series of a natural numbers")
print("9. to get reverse  series order of the natural numbers")
print("10. to get HCF")
print("11. to get LCM")
print("12. to Know whether the number is Armstrong or not")
print("13. to know whether the number is perfect number or not")
print("14. to know the AP series")
print("15. to know the Area")

c = input("Enter your choice:-")
import math
if c == '1':
    num1 = int(input("Enter any integer:"))
    addition(num1)
elif c == '2':
    num1 = int(input("Enter any integer:"))
    num2 = int(input("Enter any integer:"))
    sum_odd(num1,num2)
elif c == '3':
    num1 = int(input("Enter any integer:"))
    num2 = int(input("Enter any integer:"))
    sum_even(num1,num2)
elif c == '4':
    num1 = int(input("Enter any integer:"))
    even(num1)
elif c == '5':
    num1 = int(input("Enter any integer:"))
    num2 = int(input("Enter any integer:"))
    sum_prime(num1,num2)
elif c == '6':
    num1 = int(input("Enter any integer:"))
    prime(num1)
elif c == '7':
    num1 = int(input("Enter any integer:"))
    factor(num1)
elif c == '8':
    num1 = int(input("Enter any integer:"))
    natural(num1)
elif c == '9':
    num1 = int(input("Enter any integer:"))
    num2 = int(input("Enter any integer:"))
    reverse(num1,num2)
elif c == '10':
    num1 = int(input("Enter any integer:"))
    HCF(num1,num2)
elif c == '11':
    num1 = int(input("Enter any integer:"))
    num2 = int(input("Enter any integer:"))
    LCM(num1,num2)
elif c == '12':
    num1 = int(input("Enter any integer:"))
    Armstrong(num1)
elif c == '13':
    num1 = int(input("Enter any integer:"))
    perfect(num1)
elif c == '14':
    num1 = int(input("Enter any integer:"))
    num2 = int(input("Enter any integer:"))
    num3 = int(input("Enter any integer:"))
    AP(num1,num2,num3)
elif c == '15':
    print("press N = 1 to get the Area of circle")
    print("press N = 2 to get the Area of rectangle")
    print("press N = 3 to get the Area of triangle")
    num1 = int(input("Enter any integer:"))
    Area(num1)







