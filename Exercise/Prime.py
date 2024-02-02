
num=input(print("Enter the start number : "))
num2=input((print("Enter the end number : ")))
for num2 in range(2, int(num2)):
    if num2 > int(num):
        for i in range(2, num2):
             if (num2 % i) == 0:
                break
        else:
            print(num2)