def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,3,4]
# newl=[]
# for i in l:
#     newl.append(cube(i))
# print(newl)
newl=list(map(cube,l))
print(newl)
