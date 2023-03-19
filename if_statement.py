a=55
b=56
c=50

if a>b:
    print("a is greater than b")
elif a==b:
    print("both variables are equal")
else:
    print("b is greater than a")


#short hand if

if a>b: print("A is greater rhan b")

#short hand if else
print("A is greater") if a>b else print("B is greater than a")

# short hand if with multiple else
print("A is greater") if a>b else print("Equala") if a==b else print("B is greater")

print("Using Logical AND OR NOT")

#logical And operator

if a>b and a<c:
    print("A is greater")
else:
    print("Both conditions should be true")


#logical or operator
if a>b or a<c:
    print("A is greater")
else:
    print("Only condition should be true")


#logical not operator
if not b>a:
    print("B is not greater than a")
else:
    print("B is greater than a")


