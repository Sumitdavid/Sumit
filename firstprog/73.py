class Employee:
    name="Sagar"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

    def __str__(self):
        return f"This is str with {self.name}"

    def __repr__(self):
        return Employee.name

    def __call__(self):
        print("I'm good")
e=Employee()
# print(e.name)
# print(len(e))
print(e)
print(repr(e))
e()