import os
import time
os.mkdir("Folder")
for i in range(0,9):
    os.mkdir(f"Folder/00-0{i+1}-00",i)
for i in range(10,50):
    os.mkdir(f"Folder/00-{i}-00",i)

