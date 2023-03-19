x=int(input("Enter a value:\t"))
match x:
    case _ if(x%2==0):
        print("value is Even")
    case _ if x%2!=0:
        print("value is Odd")
    case 10:
        print("value is 10")
    case _ :
        print("Value is negative")