# Os module in Python

import os

if(not os.path.exists("new_folder")): # Check if folder exist or not
    os.mkdir("new_folder") # make new folder


for i in range(1,101):
    os.mkdir(f"Day{i}") #Makes folders like Day1 , Day2 , Day3 ...
    os.rename(f"Day{i}" , f"Night{i}") #Raname Day1-->Night1 ...

folder_list = os.listdir("new_folder")  # Get all folder inside new_folder

for folder in folder_list:
    print(folder)

current_path = os.getcwd() # Get current Path
os.chdir("/User") # Change Path

os.remove("Day1") # Remove File
os.rmdir("new_folder") # Remove Folder
 

