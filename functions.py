def myfunction():
    print("First Function")

myfunction()


#function with arguments
def my_function(x,y):
    print(x+y)

my_function(10,10)

def newfunction(first,last):
    print(first+" "+last)

newfunction("TUshar","More")


#arbitary arguments
def function(*args):
    print("Name is:"+args[2])

function("Tushar","Ajay","Ashlesh")


#keyword Arguments
def thisfunction(first,second,third):
    print("City Name:"+second)

thisfunction(first="Pune",second="Mumbai",third="Solapur")


#arbitary keyword argument
def lastfunction(**args):
    print("First name:"+args[fname])

lastfunction(fname="Tushar",lname="More")
