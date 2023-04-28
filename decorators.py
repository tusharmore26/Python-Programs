def greet(fx):
    def sub(*args, **kwrgs):
        print("Good Morning")
        fx(*args, **kwrgs)
        print("Thank You!")
    return sub

@greet 
def fun():
    print("Heyy How are you?")

@greet
def sum(a,b):
    print(a+b)

fun()
sum(5,10)