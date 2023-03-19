x=["Tushar","Prajwal","Vinit","Om"]
for i in x:
    print(i)


#looping using index number

for i in range(len(x)):
    print(x[i])


#using while loop
i=0
while i<len(x):
    print(x[i])
    i=i+1


#list comprehnsion
[print(x) for i in x]
    
