def fun():
    try:
        l=[1,3,5,7]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")

x=fun()
print(x)