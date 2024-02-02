#check Armstrong number
a=int(input(print("Enter the number")))

n=0
i=a
d=a
while (i>0):
    i=i//10
    n=n+1
print(n)
c=0
while (a>0):
    b=a%10
    c=c+(b**n)
    a=a//10
print(c)
if d==c:
    print(f"{d} is an Armstrong number")
else: print("It is not an Armstrong number")
exit()
