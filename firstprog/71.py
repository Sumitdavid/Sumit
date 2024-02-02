# x=[1,2,3]
# print(dir(x))

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1

p=person("",0)
print(p.name,p.age,p.version)
print(dir(p))
print(help(p))

help(p.__dict__)