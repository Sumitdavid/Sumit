class Employee:
    company="Apple"
    Noof_employees=0
    def __init__(self,name):
        self.name=name
        self.raise_=0.2
        Employee.Noof_employees +=1
    def showdetails(self):
        print(f"The name of the Employee {self.name} has a raise of {self.raise_}"
              f" in {self.company} of {Employee.Noof_employees}")

emp1=Employee("Sagar")
emp1.raise_=0.3
emp1.company="Apple India"
emp1.showdetails()

emp2=Employee("David")
emp2.showdetails()
Employee.company="Google"
emp3=Employee("Xico")
emp3.showdetails()