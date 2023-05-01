class vehical:
    def __init__(self,company,model):
        self.company=company
        self.model=model
        
    def __str__(self):
        return self.company

    def demo(self):
        print("First Class")

class bike:
    def __init__(self,company,model):
        self.company=company
        self.model=model

    def demo(self):
        print("Second class")

class car:
    def __init__( self,company,model):
        self.company=company
        self.model=model

    def demo(self):
        print("Third class")

v1=vehical("Audi", 2002)
b1=bike("Honda", 2013)
c1=car("BMW", 2022)


for x in(v1,b1,c1):
    
    x.demo()
