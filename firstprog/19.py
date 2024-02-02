for i in range(12):
    if(i==10):
        break
    print("5X",i+1,"=",5*(i+1))
print("Leave the loop")

for i in range(12):
    if(i==10):
     print("5X",i,"=",5*(i))
    continue
print("Leave the loop")