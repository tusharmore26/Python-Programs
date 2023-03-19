x= lambda a,b,c : a*b*c
print(x(2,2,2))



#lambda function within another function
def myfunction(n):
    return lambda a:a*n

x=myfunction(5)
print(x(11))


def newfunction(n,m):
    return lambda a,b: a+b+n+m
y=newfunction(10,10)
print(y(10,10))
