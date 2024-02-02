class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Programmer(Employee):
    def __init__(self,name,age,lan):
        super().__init__(name,age)
        self.lan=lan

Rohan=Employee("Rohan Das",41)
Sagar=Programmer("Sumit Sagar",29,"Python")
print(Rohan.name)
print(Sagar.name,Sagar.lan,Sagar.age)