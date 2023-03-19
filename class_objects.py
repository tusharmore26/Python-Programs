class myclass:
    x=10

print(myclass())


#creating object
class newclass:
    x=10
    y=10
    z=x+y

n1=newclass()
print(n1.z)


#the __init__() function
class thisclass():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
            return f"{self.name}{self.age}"

    def function(self):
        print("Name is:"+self.name)
        
t1=thisclass("Tushar",21)
print(t1)
t1.function()




