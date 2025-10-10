import time

#time.time()
# initial_time = time.time() #Get Total seconds from 1970 Jan 1 to current time
# for i in range(100): #Spend Some time in execution
#     pass
#Get Process time for For Loop
# process_time = time.time()-initial_time 
# print(f"Process took {process_time} seconds")


#time.sleep()

# print("Binod : Hey , Harry")
# time.sleep(2) #Execute Next code after 2 seconds
# print("Harry: Hey Binod")

#time.strftime()

# current_time = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_time)

words = ["Your", "Beauty", "Never","Ever",  "Scare", "Me", "...", "Mary", "On a", ]
print("-------------")
for word in (words ):
    print(word)
    
    time.sleep(0.5)