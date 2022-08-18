
class info():
    def __init__(self,name,age,hight,id):
        self.name=name
        self.age=age
        self.hight=hight
        self.id=id
    def introduction(self):
        print("My name is",self.name)
        print(f"I am {self.age} years old.")
        print(f"My hight is {self.hight} fit")
        print(f"My student id is {self.id}")
      

info1=info("Md:Hasibul Islam Shaon",22,6.3,"193-35-506")

info1.introduction()