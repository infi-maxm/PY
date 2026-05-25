class Employee:
    name="INfi"
    id=45
    age=23
    salary=450000#class attributes

infi=Employee()
print(infi.age,infi.salary)
  
infi.language='py' #object attribute
print(infi.language)

infi.id=54#instance attribute
print(infi.id)


class Student:
    name='Dhoni'
    age=7
    id=7

    def info(self):
        print(f"{self.name} loves cricket,his age is{self.age} and jersey no. is {id}")

    @staticmethod
    def greet():
        print("Welcome!")

    def __init__(self,name,age,id):#Dunder method , automatically called
        print(f"{self.name},{self.age}")
        self.name=name
        self.age=age
        self.id=id

s1=Student("virat",6,18)

s1.info()
Student.info(s1)
Student.greet()
s1.greet()

class Programmer:
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language


p1=Programmer("pr1",34,'C++')
p2=Programmer("pr2",32,'python')
p3=Programmer("pr3",33,'js')
print(p1.name,p3.age,p2.language)

import math

class Calculator:
    def __init__(self,val):
        self.sqr=(val)**2
        self.cube=(val)**3
        self.root=math.sqrt(val)

    @staticmethod
    def greet():
        print("HELLO!")

v1=Calculator(4)
v1.greet()
print(v1.sqr,v1.root)

class first:
    a='hello'

obj=first()
obj.a="bye"
print(obj.a,first.a)
