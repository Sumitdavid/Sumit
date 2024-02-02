i=int(input(print("your age is")))
if i<0:
    print("Age is negative")
elif i>0:
    print("Age is positive")
    if i<18:
        print("You are under age to drive")
    elif i>=18 and i<60:
        print("You are fit to drive")
    else: print("You are Senior citizen")
else: print("You are just born, Learn to crawl")

if (i>=18) and (i<60):
    print("You can drive")
    print("Yay!!!")
else:
    print("You can't drive")