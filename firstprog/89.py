#Request module
import requests
response=requests.get("https://www.youtube.com/watch?v=Nsb3bLIlO4w")
print(response.content)
i=0
for i in response.text:
    if response.text == ";":
        i=i+1
    break
a=response.text.split(";")
print(a)
print("\n")
print(i)