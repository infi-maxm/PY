import random

num=int(input("Enter the value:"))
computer=random.randint(1,100)
cnt=0

while(num!=computer):
    cnt+=1
    
    if(num>computer):
        print("Lower number please")
    else:
        print("Higher number please")
    num=int(input("Enter the value:"))

if(num==computer):
    cnt+=1
    print(f"Correct guess in {cnt} chance(s)")