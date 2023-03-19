dict={"name":"Tushar","lname":"More","game":"Cricket","city":"Pune"}
print(dict)

#accessing dictionary
print(dict["name"])
print(dict.get("city"))

#accessing keys
print(dict.keys())

#accessing values
print(dict.values())

#for loop in dict
for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)

for i in dict.items():
    # print(f"Value of the index {keys} is {values}")
    print(i)

#Methods in dictionaries
dict2={1:111,2:222,3:333}
#update method
dict.update(dict2)
print(dict)

dict.update({"name":"Ashlesh"})
print(dict)

#pop method
dict.pop("name")
print(dict)

#pop items method
dict2.popitem()
print(dict2)

#clear method
dict.clear()
print(dict)

#del method
del dict2[1]
print(dict2)
