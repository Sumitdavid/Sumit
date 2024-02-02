class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromstr(cls,s):
        return cls(s.split("-")[0],int(s.split("-")[1]))

e1=Employee("Sagar",45000)
print(e1.name,e1.salary)

s="JAmpa-13000"
# e2=Employee(s.split("-")[0],s.split("-")[1])
e2=Employee.fromstr(s)
print(e2.name,e2.salary)