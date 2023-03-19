str="Hello World"
print(str[4])
print(len(str))
print("Hell" in str)
print("Hell" not in str)
for x in str:
    print(x)

#slicing a string
print(str[1:5])
#slicing from 1st index
print(str[:5])
#slicing to the last index
print(str[0:])

#to uppercase
print(str.upper())
#to lowercase
print(str.lower())
#replace string
print(str.replace("H","B"))
#split string
print(str.split(","))

#concatenate string
str2="is my first program in python!"
c=str+str2;
print(c)
c=str+" "+str2
print(c)
