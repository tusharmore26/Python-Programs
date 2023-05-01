try:
    print(a)

except TypeError:
    print("Type of a is unknown")

except NameError:
    print("a is not defined")

except:
    print("Error")

finally:
    print("End of try except block")

# raise an exception using raise keyword
x="Tushar"

if not type(x) is int:
  raise TypeError("Only integers are allowed")