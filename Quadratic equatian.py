#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

print("Note:- Quadratic Equations program")

a = int(input("Enter any integer:"))
b = int(input("Enter any integer:"))
c = int(input("Enter any integer:"))
import math
d = (b**2-(4*a*c))
print('{0}x^2+{1}x+{2} = 0'.format(a,b,c))
print(d)
if d > 0:
        print("root1 =", (-b+math.sqrt(d)/2*a) , "root2 =",-b-math.sqrt(d)/2*a)
elif d < 0:
        print("root1 =", (-b+math.sqrt(d)/2*a) , "root2 =",(-b-math.sqrt(d)/2*a))
elif d == 0:
        print("root1 =", -b/2*a,"= root2")

    


