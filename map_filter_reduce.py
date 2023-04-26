from functools import reduce
# map function
li=[12,24,4,65,8,32,10]
cube=list(map(lambda a:a*a*a, li))
print(cube)

# filter function
def filt(a):
    return a>24

val=list(filter(filt, li))
print(val)

# reduce function
sum=list(reduce(lambda a,b:a+b, li))
print(sum)