s1={1,4,7,9}
s2={2,5,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1,s2 )
print(s1.difference(s2))
print(s1.difference_update(s2))