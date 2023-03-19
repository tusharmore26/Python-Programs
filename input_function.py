#input function is used to take input from user.

x=input("Enter the value of x:")
print(x)

#but the input function takes input as a string so if we want to take integer input we will have to perform typecasting
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print(n1 + n2)

#taking integers without typecasting
a=input("Enter first number:")
b=input("Enter second number:")
print(a+b)   #it will join the to numbers (string concatenation )

#taking floating numbers
f1=input("Enter value1:")
f2=input("Enter valur2:")
print(float(f1) * float(f2))

#invallid conversion
str=int(input("Enter string:"))
print(str(str))




