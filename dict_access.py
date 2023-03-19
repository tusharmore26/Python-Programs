thisdict={
    "Name" : "Tushar",
    "Surname" : "More",
    "Gender" : "Male",
    "Year" : 2002
    }
print(thisdict)
x=thisdict.keys()
thisdict["Date"]=26
print(x)
y=thisdict.values()
print(y)
print(thisdict)

#updating dictionary

thisdict["Name"]="Ajay"
print(thisdict)

#update using update method

thisdict.update({"Year":2000})
print(thisdict)


#adding items to dictionary

thisdict["City"]="Pune"
print(thisdict)

#adding items using update method

thisdict.update({"Age":21})
print(thisdict)


#removing items
thisdict.pop("Age")
print(thisdict)

#using popitem()
thisdict.popitem()
print(thisdict)

#using del keyword
del thisdict["Year"]
print(thisdict)
