# Program to Greet as per Time

import time

print(time.time()) # Machine Readable Time
timeNow = time.ctime() #Human readable Time

# hourNow =  int(timeNow[11:13]) --> More time Consuming 

hourNow = int(time.strftime("%H")) # --> More Efficient

if(hourNow >= 1 and hourNow <=12):
    print("Good Morning , BinodX")

elif(hourNow > 12 and hourNow <=17 ):
    print("Good Afternoon, BinodX")

elif(hourNow >17 and hourNow <= 19):
    print("Good Evening, BinodX")

else:
    print("Good Night, BinodX")




