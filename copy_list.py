firstlist=["Pune","Mumbai","Solapur","Begalore"]
newlist=firstlist.copy()
print(firstlist)
print(newlist)

#another method
new_list=list(newlist)
print(new_list)

#join lists
li=["Nashik","Chennai"]
li.extend(firstlist)
print(li)
x=firstlist+li;
print(x)
