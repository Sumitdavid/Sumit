#Generators
def my_gen():
    for i in range(5):
        yield i

gen=my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
for j in gen:
    print(j ,"\n")