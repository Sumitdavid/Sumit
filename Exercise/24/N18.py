def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

z=int(input(print("Factorial of :",end="")))
f=fac(z)
print("\n")
print(f"is {f}",)
