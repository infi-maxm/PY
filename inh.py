# try:
#     with open("f1.txt") as f:
#         print(f.read())

# except Exception as e:
#     print(e)

# try:
#     with open("f2.txt") as f:
#       print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("f3.txt") as f:
#        print(f.read())

# except Exception as e:
#     print(e)

# # try:
# #     with open({"f1.txt","f2.txt","f3.txt"}) as f:
# #         print("File found")

# # except Exception as e:
# #     print(e)

# print("Thankyou")

# fruits=['apple','litchi','mango','orange','banana','watermelon','muskmelon','pineapple','guava']

# for i,j in enumerate(fruits):
#     if(i==2 or i==4 or i==6):
#         print(j)

# num=int(input("Enter number:"))

# l=[str(num*i) for i in range(1,11)]
# print(l)
# l2="\n".join(l)
# print(l2)

# with open ("f1.txt",'a') as f:
#     for i,j in enumerate(l):
#         f.write(f"{num}*{i+1}:{j}\n")

# a=int(input("Enter number a:"))
# b=int(input("Enter number b:"))

# try:
#     print(a/b)

# except ZeroDivisionError as z:
#     print(z)

# fil=filter(lambda x:x%5==0,[num for num in range(1,101)])
# print(list(fil))

from functools import reduce
import random

l=[2,6,8,3,10,4,6,9]

def maxm(x,y):
    if(x>y):
        return x
    return y

r=reduce(maxm,l)

print(r)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
