# string = r"This is a string\nwith a newline character."
# string1 = "This is a string\nwith a newline character."
# print(string)
# print(string1)
n=int(input("Enter the number of lines"))
num = 0

for i in range(0, n):

    for j in range(0, i+1 ):
        print(num, end=" ")
        num = num +1
    print("\r")