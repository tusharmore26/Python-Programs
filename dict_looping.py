thisdict={
    "Brand":"Tata",
    "Model": "Safari",
    "Year" : 2016
    
    }

for i in thisdict:
    print(i)

for i in thisdict:
    print(thisdict[i])

for i in thisdict.keys():
    print(i)

for i in thisdict.values():
    print(i)

for x,y in thisdict.items():
    print(x,y)


#copying dictionaries

newdict=thisdict.copy()
print(newdict)

new_dict=dict(newdict)
print(new_dict)
