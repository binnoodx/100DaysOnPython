#Exercise Clear the clutter

"""
Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png

"""

import os

loc = r"C:\\delete" #Put your filder Location here


files = os.listdir(loc)
i=0
for file in files:
    if(file.split(".")[1]=="png"):
        os.rename(f"loc\\{file}" , f"loc\\{i}")
    i=i+1

print("Success")







