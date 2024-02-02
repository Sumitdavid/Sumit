#Fibonacci number
a=int(input("Fibonacci Number"))
def fibbanocchi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbanocchi(n-1)+fibbanocchi(n-2)
for i in range(0,a):
    # fibbanocchi(i)
    print(fibbanocchi(i))