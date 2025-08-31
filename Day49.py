# File IO

file_ = open("my_file.txt","r") #Opening my_file.txt which exists and we open for reading purpose
text = file_.read() #Read Data on File
print(text)
file_.close()


file_2 = open("my_file.txt" , "w") #If file exist that will open else create new one
file_2.write("hello , world")  # Erase all content and Write on that file
file_.close()

file_3 = open("my_file.txt" , "a")
file_2.write("hello , world")  # Append text on exixting text
file_.close()


### Alternative method

with open("my_file.txt","w") as f:
    f.write("hello Worls")

    ## No need to close file
