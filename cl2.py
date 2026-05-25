# class Programmer:
#     company="Apple"
#     def greet(self):
#         print("welcome to coding world!")
#     def __init__(self):
#         print("Constructor Programmer!")

# class Manager(Programmer):
#     language="py"
#     def inform(self):
#         print(f"Language:{self.language} welcome to {self.company}")
#     def __init__(self):
#         print("Constructor Manager!")

# class Assistant:
#     book="learn py"
#     def state(self):
#         print(f"Learn python with {self.book}")
#     def __init__(self):
#         print("Constructor Assistant!")
    
#     @classmethod
#     def msg(cls):
#         print(f"class attribute is:{cls.book}")

#     @property
#     def resource(self):
#         return (f"resources include:{resource.fres} {resource.lres}")
    
#     @resource.setter
#     def resource(self,value):
#         self.fres=value.split()[0]
#         self.lres=value.split()[1]


# class Head(Assistant,Manager):
#     department="Py department"
#     name="Roy"
#     def tell(self):
#         print(f"Myself {self.name},company {self.company},department:{self.department}")
#         print(f"language:{self.language}")
#     def __init__(self):
#         super().__init__()#calls intructor of parent class which is first among two
#         print("Constructor head!")
    

# obj=Head()
# obj.tell()
# obj.state()

# obj2=Manager()
# obj2.inform()
# # obj2.state() error becuse manger can use progrmmer and its own attributes only

# obj3=Assistant()
# obj3.book="py in 20 days"
# obj3.resource="NOTES PDF"

# print(obj3.fres,obj3.lres)
# obj3.msg()

# class dim2:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#         print(f"Vector:{self.i}i+{self.j}j")

# class dim3(dim2):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#         print(f"Vector:{self.i}i+{self.j}j+{self.k}k")

# dim3(2,3,5)

# class Employee:

#     def __init__(self):
#         self.val=0
#         self.inc=0
#         self.after=0

#     @property
#     def salary(self):
#         return self.val
    
#     @property
#     def increement(self):
#         return self.inc
    
#     @salary.setter
#     def salary(self,val):
#         if(val<0):
#             print("Not allowed")
#         else:
#             self.val=val
    
#     @increement.setter
#     def increement(self,inc):
#         if(inc<0):
#             print("Not allowed")
#         else:
#             self.inc=inc

#     @property
#     def salaryafterincreement(self):
#         return self.after
    
#     @salaryafterincreement.setter
#     def salaryafterincreement(self,val,inc):
#         self.after=self.val+self.inc

# e1=Employee()
# e1.salary=300000
# e1.salary=-3200000
# print(e1.salary)
# e1.increement=-3200
# print(e1.increement)
# e1.increement=4500
# print(e1.increement)
# print(e1.salaryafterincreement)


class Complex:
    def __init__(self,re,im):
        self.re=re
        self.im=im

    def __add__(self,c2):
        return Complex(self.re+c2.re,self.im+c2.im)
    
    def __str__(self):
        return f"{self.re}+{self.im}i"

    def __mul__(self,c2):
        return Complex((self.re*c2.re)-(self.im*c2.im),(self.re)*c2.im+((self.im)*c2.re))      

c1=Complex(1,2)
c2=Complex(3,-2)

print(c1+c2)
print(c1*c2)

# print(c1.sum(c2).re,c1.sum(c2).im)
# print(c1.mul(c2).re,c1.mul(c2).im) 


class Vector:
    def __init__(self,value):
        self.value=value
    
    def __add__(self,v2):
        return Vector([a+b for a,b in zip(self.value,v2.value)])
         
    def __str__(self):
        return str(self.value)
    
    def __mul__(self,v2):
        return sum(a*b for a,b in zip(self.value,v2.value))

    def __len__(self):
        return len(self.value)

v1=Vector([1,2,3])
v2=Vector([2,3,4])

print(v1+v2)
print(v1*v2)
print(len(v1))

class dim3:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


vec=dim3(7,84,2)
print(vec)