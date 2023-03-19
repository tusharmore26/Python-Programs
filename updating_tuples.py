new_tuple=("Apple","Banana","Mango","Watermelon")
new_list=list(new_tuple)
new_list[3]="Orange"
new_tuple=tuple(new_list)
print(new_tuple)

#adding items to the tuple
new_list=list(new_tuple)
new_list.append("Pineapple")
new_tuple=tuple(new_list)
print(new_tuple)

#removing items from tuples
new_list=list(new_tuple)
new_list.remove("Pineapple")
new_tuple=tuple(new_list)
print(new_tuple)

#adding two tuples
second_tuple=("Pineapple",)
new_tuple+=second_tuple
print(new_tuple)
