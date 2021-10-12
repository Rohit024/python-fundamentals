#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the last number:"))
sum_even = 0
count = 0
#To check whether the first number is even or odd.
if num1%2 == 0:
    for i in range(num1,num2+1,2):
        sum_even += i
        count += 1
elif num1%2 == 1:
    for i in range(num1+1,num2+1,2):
        sum_even += i
        count += 1
print("Sum of even numbers are:", sum_even)
print("The average of the even number are", sum_even/count) 
