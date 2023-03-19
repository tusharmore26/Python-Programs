print("Pyhton does not have built in support for an array, but we can use lists instead.")
thislist=["Pune","Mumbai","Solapur","Bengalore","Delhi"]
print(thislist)

#length of list
print(len(thislist))

#looping through list
for x in thislist:
    print(x)


#accessing items from list
print(thislist[1])


#adding items to the list
thislist.append("Chennai")
print(thislist)

#removing items from list
thislist.remove("Chennai")
print(thislist)

thislist.pop(0)
print(thislist)




