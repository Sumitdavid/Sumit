class person:
    def __init__(self,n,o):
        print("Hey!")
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")
    print(f"{self.name} is a {self.occ}")
a=person("Sumit","Software developer")
b=person("Divya","HR")

a.info()
b.info()
