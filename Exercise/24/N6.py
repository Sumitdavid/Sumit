#check palindrome number
n = int(input("Number : "))
reverse,temp = 0,n
while temp>0:
    reverse = reverse*10 + temp%10
    temp=temp//10
if reverse==n:
    print("number is palindrome")
else:
    print("number is not palindrome")
