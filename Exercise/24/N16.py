#Average of numbers
n = int(input("No.of elements are : "))
a=[]
for i in range(0,n):
    i=int(input(f"Numbers {i+1} is :"))
    a.append(i)
avg=sum(a)/n
print(avg)
