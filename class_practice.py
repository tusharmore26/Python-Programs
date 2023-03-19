class myclass:
    def __init__(a,name,age):
        a.name=name
        a.age=age

    def myfunction(var):
        print("Name is :",var.name)
        print("Age is :",var.age)
m1=myclass("Tushar",21)
print(m1.name)
del m1
m1.name="Ajay"
m1.myfunction()
