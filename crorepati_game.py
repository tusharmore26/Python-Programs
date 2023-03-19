print("\t\t!!!!Kon Banega CrorePati!!!\n")

li=["Who is the PM of India?","Who is CM of Maharashtra?","In which year India won the World Cup?"]

i=0
win=0
while i<len(li):
    var=li[i]
    ind=i
    
    if(i==0):
        print(li[0])
        ans=input("\tEnter Your answer:")
        if(ans=="Narendra Modi"):
            print("\tCongratulations you are correct!!")
            win=win+1000
        else:
            print("\tThis is wrong answer! Best luck for next one!")
    elif(i==1):
        print(li[1])
        ans=input("\tEnter your answer:")
        if(ans == "Eknath Shinde"):
            print("\t!!Congratulations You are correct!!")
            win=win+1000
        else:
            print("\tThis is wrong answer! Best luck for next one!")
    elif(i==2):
        print(li[2])
        ans=int(input("\tEnter your answer:"))
        if(ans==2011):
            print("\tCongratulations you are correct!!")
            win=win+1000
        else:
            print("\tThis is wrong answer! Best luck for next one!")
    
    i+=1

print("You won ",win,"Rupies\n Thank You!!")