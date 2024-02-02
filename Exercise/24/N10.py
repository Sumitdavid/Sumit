#sum of digits
n = int(input("Number : "))
# s=0
# def sum(num):
#     s=0
#     s=s+num
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
print(s)
