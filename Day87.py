#Shutils Module in Python

import shutil

shutil.copy("Day87.py" , "new_file.py") #Copy Exact File
shutil.copytree("Folder1" , "new_folder")

shutil.move("Day87.py" , "new_file.py") #Move Exact File

shutil.rmtree("my_folder") #Delete Folder

print(shutil.__dict__)