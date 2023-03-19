x=["Pune","Mumbai","Solapur","Bengalore"]
print(x)
print(type(x))

#accessing list items
print(x[3])
print(x[0:3])
print(x[:5])
print(x[2:])

print("Pune" in x)
print("Delhi" not in x)

#changing items values
x[2]="Delhi"
print(x)
x[2:4]=["Nagpur","Chennai"]
print(x)

#Addingitems to the list
x.append("Ahemadabad")
print(x)

#adding another list to this list
y=["Lucknow","Hydrabad"]
x.extend(y)
print(x)

#removing list items
x.remove("Lucknow")
print(x)
x.pop(3)
print(x)
x.pop(3)
print(x)
x.pop()
print(x)
del x[0]
print(x)
x.clear()
print(x)
