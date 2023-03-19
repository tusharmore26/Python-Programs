#we can also use else block in looping
for i in range(10):
    print("iteration {} in a loop".format(i+1))
    if(i==9):
        break
else:
    print("out of loop")