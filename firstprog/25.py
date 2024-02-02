cnty=("U.S","Britain","India","Italy","Spain")
print(type(cnty),cnty)
temp=list(cnty)
temp.append("Russia")
temp.pop(1)
temp[1]="Uganda"
cnty=tuple(temp)
print(cnty)

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)