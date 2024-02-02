#prime factors of a number
print(f"The prime factors of {n} are {n}",end=",")
for i in range(2,n):
        if ((n%i)==0):
            print(i,end=",")
            # break
