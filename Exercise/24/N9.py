#check whether it is binary or not
n = int(input("Number : "))
i=0
while n>0:
    while n>0:
     if (n%10)==1:
        n=n//10
     elif (n%10)==0:
         n=n//10
     else:
         print("Not a binary number")
         exit()
    print("It's a binary number")


