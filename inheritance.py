class parent:
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname

    def function(self):
        print("Name of the student is :",self.name)
        print("Last name is :",self.lname)

class child(parent):
    def __init__(self,name,lname,city):
        super().__init__(name,lname)
        self.city=city

    def welcome(self):
        print("Welcome ",self.name,self.lname," in ",self.city)
    

ch=child("Tushar","More","Pune")
ch.welcome()
ch.function()



