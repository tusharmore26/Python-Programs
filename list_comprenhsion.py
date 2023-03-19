x=["Apple","Banana","Mango","Watermelon","Orange"]
y=[]
for i in x:
    if "pp" in i:
        y.append(i)

print(x)
print(y)

newlist=[i for i in range(10) if i<7]
print(newlist)

new_list=[i.upper() for i in x]
print(new_list)
