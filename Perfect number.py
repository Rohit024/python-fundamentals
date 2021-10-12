num = int(input("Enter any input:"))
sum_i = 0
for i in range(1,num):
    if num%i == 0:
        sum_i += i
if sum_i == num:
    print("perfect number")
else:
    print("put another input")
    
    

