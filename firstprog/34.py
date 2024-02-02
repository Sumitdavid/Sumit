e1={1:9,2:8,3:6,4:3,5:10}
e2={6:7,7:6}
e1.update(e2)
print(e1)
for i,s in e1.items():
    print((i,s)),
    i=i+1
e1.pop(7)
print(e1)