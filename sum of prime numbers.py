#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

print("Program to get the sum of prime numbers")

num1 = int(input("Enter any integer:"))
num2 = int(input("Enter any integer:"))
sum = 0
flag = 0
for j in range(num1,num2):
    for i in range(2,j):
        if j%i == 0:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        print(j)
        sum += j
print("The sum of all the prime numbers:",sum)


    
