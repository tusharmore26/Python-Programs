fruits=["Apple","Banana","Watermelon","Orange"]
for i in fruits:
    print(i)

#for loop for the string
str="Tushar"
for i in str:
    print(i)

#break statement
for i in fruits:
    
    if i=="Banana":
        break
    print(i)

#continue statement
for i in fruits:
    if i =="Apple":
        continue
    print(i)


#range function
for i in range(2,30,3):
    print(i)
