class myclass:
    name="Tushar"
    age=21
    lname="More"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name},{self.age}"    

    def myfun(self):
        print(self.name,"is ",self.age,"years old.")
        print(f"{self.name} is {self.age} years old.")


m2=myclass("Tushar",21)
print(m2)
m2.myfun()
