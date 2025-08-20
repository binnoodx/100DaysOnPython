# Dictionary Methods in Python

d1 = {1:"BinodX", 2:"Python"}
d2 = {3:"Hey" , 4:"Hello"}

d1.update(d2)
print(d1)

d1.pop(1) #Gives value having key 1
d1.popitem() #Gives Last item of d1

d1.clear() #clear Entire Dictionary
del d1 #Delete entire Dictionary