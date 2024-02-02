marks=[52,45,62,87,95,61]
# Above is a list, () is a tuple
for index,mark in enumerate(marks,start=1):
    print(mark)
    if (index == 3):
        # marks.pop(3)    (doesn't work in tuple)
        print("It's working")
