#Created by:-Rohit kumar
#Email.no:-rohit03112005sah@gmail.com

print("press N = 1 to get the Area of circle")
print("press N = 2 to get the Area of rectangle")
print("press N = 3 to get the Area of triangle")

import math
num = int(input("Enter any number of your choice(N):- "))
def Area(num):
    if num == 1:
        Radius = int(input("Enter Radius:- "))
        print("Area of circle =",math.pi*Radius**2)

    if num == 2:
        Length = int(input("Enter Length:- "))
        Breadth = int(input("Enter Breadth:- "))
        print("Area of rectangle =",Length*Breadth)

    if num == 3:
        Base = int(input("Enter Base:- "))
        Height = int(input("Enter Height:- "))
        print("Area of triangle =",0.5*Base*Height)

    if num!= 1 or 2 or 3:
        print("please enter the right choice")
Area(num)

