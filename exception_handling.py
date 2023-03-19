
try:
    a=int(input("Enter a value:"))
    li=[1,5,7]
    print(li[a])

except ValueError:
    print("Given value is not ineger")

except IndexError:
    print("Index Error")

except IndentationError:
    print("Indentation Error")