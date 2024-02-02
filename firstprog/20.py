#def avg(a,b):
 #   print("The average is", (a+b)/2)
#avg(5,6)

def avg(*number):
    sum=0
    for i in number:
     sum=sum+i
    #print("The average is", sum/len(number))
    return sum/len(number)
c=avg(5,7,9,11)
print(c)