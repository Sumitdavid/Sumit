dic={ "Harry":"Human being",
      "Spoon":"object",
      1: "Akram",
      2:"Balsi",
      3:"Bindu",
      4:"Jyostna",
      5:"Hareesh"}
print(dic[5])
print(dic["Harry"])
print(dic.get(2))
print(dic.get(21))
# print(dic[21])
for key in dic.keys():
    print(dic[key])
    print(f"The value respective to their roll number {key} is {dic[key]}")
print(dic.keys())
print(dic.values())
print(dic.items())
for key,value in dic.items():
    print(f"The value respective to their roll number {key} is {value}")