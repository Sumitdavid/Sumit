l=[45,5,6,7,9,1,4,3]
print(l)
l.append(7)
print(l)
# l.sort()
# print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(7))
# m=l
# m[0]=0
# print(l)
m=l.copy()
m[0]=0
print(l)
print(m)
l.insert(2,66)
print(l)
k=l+m
print(k)
l.extend(m)
print(l)

