class Math:
    def __init__(self,num):
        self.num=num

    def __add__(self, n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.num)
a.__add__(6)
print(a.num)
print(a.add(2,4))
result=Math.add(3,4)
print(result)