import time
# H=int in range(23)
# M=int in range(59)
# S=int in range(59)

# print("Enter time in HH:MM:SS")
# #i=input(str, H, print(":"),M,print(":"),S)
# H=int(input(print("Hours")))
# M=int(input(print("Minutes")))
# S=int(input(print("Seconds")))
# print("Your entered time is",H,":",M,":",S)
t=time.strftime('%H:%M:%S')
print("Your time is",t)
H=int(time.strftime('%H'))
# if H<24 and M<60 and S<60:
if H<24:
 if (H>=0) and (H<6):
    print("Good Morning sir/madam")
 elif (H>=6) and (H<12):
    print("Good afternoon sir/madam")
 elif H>=12 and H<18:
    print("Good evening sir/madam")
 elif H>=18 and H<24:
    print("Good night")
else: print("You entered an invalid time\nKindly check your watch")

