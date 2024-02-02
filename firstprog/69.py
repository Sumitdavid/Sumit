class Employee:
    company="Apple"
    def show(self):
        print(f"The employee {self.name} works in {self.company}")

    @classmethod
    def changeCompany(cls,Newcompany):
        cls.company=Newcompany

e1=Employee()
e1.name="Sagar"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)