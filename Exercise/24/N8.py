#display greatest number among 3 numbers
a=int(input(print("Enter the 1st number")))
b=int(input(print("Enter the 2nd number")))
c=int(input(print("Enter the 3rd number")))
if b>a:
    if c>b:
        print(f"{c} is larger than {a},{b}")
    else:print(f"{b} is greater than {a},{c}")
else:print(f"{a} is larger than {b},{c}")
