num=int(input(print("Enter the start number : ")))
num2=int(input(print("Enter the end number : ")))

def a():

    for i in range(2,num2):
       if (num2 % i)==0:
            break
       else:
            return True

if num2>num:
    a()
else:print("Wrong entry")
