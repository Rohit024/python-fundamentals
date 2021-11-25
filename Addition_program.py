num = int(input("Enter any number:"))
def addition(num):
    if num<100:
        c = (num//10)
        d = num%10
        print("The addition of number is:",c+d)
    elif num<1000:
            e = (num//100)
            h = ((num%100)//10)
            d = (num%10)
            print("The addition of number is:",e+n+d)

    elif num<10000:
                g = (num//1000)
                f = ((num%1000)//100)
                h = ((num%100)//10)
                d = (num%10)
                print("The addition of number is:",g+f+h+d)

    elif num<100000:
                    i = (num//10000)
                    k = ((num%10000)//1000)
                    f = ((num%1000)//100)
                    h = ((num%100)//10)
                    d = (num%10)
                    print("The addition of number is:",i+k+f+h+d)

addition(num)
