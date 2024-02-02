a=input("Enter the multiplication table of:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid input")

print("Some important lines of code")
print("End of program")
