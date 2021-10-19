#Functions
#--used for better organization of code
#--they can be reused
# if, else, elif, while , or, and, for, range, len, list, int, pass, continue, &, |, ~, break etc


name = input("Enter your name:")
age = input("Enter your Age:")
phone = input("Enter your Mob no:")

#function definition
def greetings(n, a, p):
    #function body
    print("hello",n , "Good Morning")
    print("I think you are", a, "years old.")
    print("I got your number from Facebook. is it",p, "?")
    
greetings(name, age, phone) #functiion calling    



    
