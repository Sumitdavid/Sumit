# num=input(print("Enter the start number : "))
num2=input(print("Enter the end number : "))

def a(int):
    for i in range(2, int(num2)):
       if ((num2)%i)==0:
            break
       else:
            return True
for i in range(2,int(num2)):
    a(num2)
    if a() is True:
        print(f"{num2} is a prime number")