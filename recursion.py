#recursion means calling the function inside the same function
def myfunction(n):
    rec=n * myfunction(n-1)
myfunction(5)
print(rec)