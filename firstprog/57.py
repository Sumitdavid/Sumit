class person:
    name="Sumit"
    occupation="Software Engineer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()

a.name="Shubham"
a.occupation="Baba"
b.name="JAJA"
b.occupation="Horse rider"

a.info()
b.info()
person.info(self=person)
