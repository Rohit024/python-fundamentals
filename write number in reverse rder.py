#Created by:-Rohit kumar
Email.no:-rohit03112005sah@gmail.com

print("Note:- please enter the number less than 100000 and don't put the num end with zero(0).")

num = int(input("Enter any integer:"))
if num<100:
    c = (num//10)
    d = num%10
    a = c+d*10
elif num<1000:
    e = (num//100)
    h = ((num%100)//10)
    d = (num%10)
    a = e+h*10+d*100
elif num<10000:
    g = (num//1000)
    f = ((num%1000)//100)
    h = ((num%100)//10)
    d = (num%10)
    a = g+f*10+h*100+d*1000
elif num<100000:
    i = (num//10000)
    k = ((num%10000)//1000)
    f = ((num%1000)//100)
    h = ((num%100)//10)
    d = (num%10)
    a = i+k*10+f*100+h*1000+d*10000
if num == a:
    print("palaindrom")
else:
    print("not palaindrom")
