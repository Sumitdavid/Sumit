# Sum of n numbers (1-50)
print(sum(range(1,51)))
# Average of numbers
n=int(input(print("No.of digits:")))
sum=0
for i in range(1,n+1):
    i=int(input(print("The element is :")))
    sum=sum+i
avg=sum/n
print("Average:",avg)


