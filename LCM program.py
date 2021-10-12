#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

num1 = int(input("Enter any integer:"))
num2 = int(input("Enter any integer:"))
if num1>num2:
    c = num1
else:
    c = num2
d = (num1*num2)
for i in range(c,d+1,1):
    if i%num1 == 0 and i%num2 == 0:
        break
print("The LCM of the given number is",i)
    
