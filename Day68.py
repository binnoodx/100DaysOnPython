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

loc = r"C:\delete"
files = os.listdir(loc)

# Function to rename files of a specific extension
def rename_by_extension(ext):
    count = 1
    for file in files:
        if file.lower().endswith(ext):
            name, _ = os.path.splitext(file)
            src = os.path.join(loc, file)
            dst = os.path.join(loc, f"{count}{ext}")
            
            # Handle conflicts by using a temp name first
            if os.path.exists(dst):
                dst = os.path.join(loc, f"temp_{count}{ext}")

            os.rename(src, dst)
            count += 1

# Call for the extensions you care about
rename_by_extension(".png")
rename_by_extension(".jpg")
rename_by_extension(".jpeg")
rename_by_extension(".txt")

print("Success")




