# check perfect number
n = int(input("Number : "))
a=0
for i in range(1,n):
    if i**2==n:
        a=1
    else:pass
if a==1:
    print(f"{n} is a perfect number")
else:print(f"{n} is not a perfect number")