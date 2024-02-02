class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"The name of Employee ID: {self.id} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default Language is Python")
e1=Employee("Vasist",1234)
e2=Employee("Hiss",1235)
e1.showdetails()
e2.showdetails()
e3=Programmer("Googly",1236)
e3.showdetails()
e3.showlanguage()
