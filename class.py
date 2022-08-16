from module import *

EmployeID()

class myclas():
    def __init__(self):
        self.age ="employe age is 49."
        self.foo="And his name is Khan"
        
obj= myclas()

print(obj.age,obj.foo)

class hisclas():
    def __init__(self):
        self.myname="His name is Shaon."
        self.hisage="And his age is 22"

obj = hisclas()
print(obj.myname,obj.hisage)
"""how can a object can name both class 
at the same time. find the answer""" 

obj2 = hisclas()
print(obj2.myname,obj2.hisage)