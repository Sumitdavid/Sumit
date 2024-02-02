def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(2))
print(factorial(3))
print(factorial(4))

#Fibonacci sequence
for n in range(12):
    def fib(n):
        if (n==0):
            return 0
        elif (n==1):
            return 1
        else:
            return fib(n-1)+fib(n-2)
    print(fib(n))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))