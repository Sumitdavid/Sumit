a=int(input("Enter a number between 5 to 9" '\n'))
if((a<5) or (a>9)):
    # raise ValueError
    raise ValueError("Entered number is not in between 5 and 9")