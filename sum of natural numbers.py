#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

print("Program for sum and average of the natural numbers")

num1 = int(input("Enter the first:"))
num2 = int(input("Enter the last:"))
sum_natural = 0
for i in range(num1,num2+1,1):
    sum_natural += i
print( "sum of natural numbers:", sum_natural )
d = (num2-num1)+1
print("The average of the number is",sum_natural/d) 
