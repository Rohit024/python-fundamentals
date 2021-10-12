num1 = int(input("Enter any integer:"))
num2 = int(input("Enter any integer:"))
d = (num1*num2) 
for i in range(1,d+1,1):
    if num1%i == 0 and num2%i == 0:
        r = i
print("The HCF of the given number is",r)
    

