n = int(input("Number : "))
def fac(num):
    for i in range(2,num):
     if n%i==0:
        print(i,",",end="")

for i in range(2,n):
    fac(i)

