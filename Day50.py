### Readline and Writeline in Python

#To read lines
my_file = open("myfile.txt" , "r")
lines = my_file.readline()
print(lines)
my_file.close()

#To write lines
my_file2 = open("myfile2.txt" , "w")
lines = ["hi\n", "hello\n"]
my_file2.writelines(lines)
my_file2.close()