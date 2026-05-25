
# str="Welcoming you to college!\nLNMIIT\nGood evening ,one n all\nThankyou"

# f=open("two.txt","w")
# f.write(str)
# f.close()

f = open("two.txt")
# data=f.read()
#lines=f.readlines()
line1=f.readline()
line2=f.readline()
# print(data)
#print(lines,type(lines))
print(line1,type(line1))
print(line2,type(line2))
f.close()

f = open("two.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()

with open("two.txt") as f:
    data=f.read()

print(data,type(data))

# l=len(data)
# i=0
# count=0
# while i<(l-1):
#     if(data[i].isalpha()==True and (data[i+1]=='\n' or data[i+1]==' ')):
#         count=count+1
#     i=i+1    

# print(count)

count=data.split()
print(len(count),type(count))

print(data.find("LNMIIT"))
print(data.find("LM"))

newdata=data.replace("Shine","Proud")

with open("two.txt","w") as f:
    f.write(newdata)

with open("two.txt") as f:
    print(f.read())

with open("two.txt") as f:
   line=f.readline()
   lnum=1
   while(line!=""):
        if("earth" in line):
            print(f"Word found,line number:{lnum}")
            break
        else:
            line=f.readline()
            lnum=lnum+1






