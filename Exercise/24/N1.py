#reverse an integer
a=int(input(print("Enter the number")))
i=0
while(a>0):
    n=a%10
    i=i*10+n
    a=a//10
print(i)