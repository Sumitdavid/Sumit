i=int(input(print("Enter the value of i")))
match i:
    case 1:
        print(i,"is 1")
    case 2:
        print(i,"is 2")
    case _ if i!=10:
        print(i,"not equal to 10")
    case _:
        print("equal to 10")


