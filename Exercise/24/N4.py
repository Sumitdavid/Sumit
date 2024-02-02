#Fibanacci number
a=int(input("Fibonacci Number"))
first=0
second=1
for i in range(0,a):
    if i<=1:
        result=i
    else:
        result=first+second
        first=second
        second=result
    print(result)