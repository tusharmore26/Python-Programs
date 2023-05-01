# parent class

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        print(self.fname,self.lname)

# child class

class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # pass


        


s1=student("Tushar", "More")
s1.__str__()

    