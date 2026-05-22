#rock paper scissors

import random

#rock=1 paper=2 scissors=3

str={'rock':1,'paper':2,'scissors':3}
rstr={1:'rock',2:'paper',3:'scissors'}
count=int(input('Enter number of chances:'))
c=0
winc=0
winu=0

while c<count:
    
    print(f"\nRound {c}:")
    computer=random.randint(1,3)
    user_input=input("Enter your choice:")
    user=str[user_input]
    print(f"Choices: computer->{rstr[computer]}  user->{user_input}")
    
    if(computer==user):
        print('Draw')
    elif(computer==1 and user==2 ):
        winu=winu+1
        print("User wins")
    elif(computer==1 and user==3):
        winc=winc+1
        print("Computer wins")
    elif(computer==2 and user==1):
        winc=winc+1
        print("Computer wins")
    elif(computer==2 and user==3):
        winu=winu+1
        print("User wins") 
    elif(computer==3 and user==1):
        winu=winu+1
        print("User wins")
    elif(computer==3 and user==2):
        winc=winc+1
        print("Computer wins") 
    else:
        print("Something went wrong!")

    c=c+1

if(winc>winu):
    print("\nComputer winner!")
elif(winc<winu):
    print("\nUser winner!")
else:
    print("\nDraw!")



