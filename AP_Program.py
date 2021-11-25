#Created by:-Rohit kumar
#Email.no:-rohit03112005sah@gmail.com

a = int(input("Enter your starting number:"))
d = int(input("Enter the common difference:"))
n = int(input("Enter the last term:"))
def AP(a,d,n):
    for i in range(a,n,d):
        print(i, end = ',')
AP(a,d,n)

        

