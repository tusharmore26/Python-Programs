#Local Scope
x=10
def myfun():
    x=100
    print(x)
myfun()
print(x)

#global Scope
x=5
def thisfun():
    print(x)
thisfun()
print(x)