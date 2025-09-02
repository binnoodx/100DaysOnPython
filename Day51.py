# tell() , seek() and truncate() in python

with open("myfile.txt" , "w") as f:
    f.seek(5) #Starts from 5 characters (bytes) behind
    data = f.read(10) #Starts from 5 bytes and read 10 bytes ahead
    print(data)
    print(f.tell()) #---> tell the current position. (Seek value)

    f.write("hello World")
    f.truncate(5) #Stop Writing when 5 bytes reached