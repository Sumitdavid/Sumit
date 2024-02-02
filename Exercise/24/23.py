#Reverse the number
x=int(input("Enter the number"))
i=0
while(x>0):
    # print(x)
    a=x % 10
    i=i*10+a
    x=x//10
print(i)