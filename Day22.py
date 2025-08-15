# List in Python

color_list = ["yellow", "blue","Red"]

print(color_list) #Print All
print(color_list[:]) # Print All

num_list = [i for i in range(11) if i%2!=0]

print(num_list)
if(7 in num_list):
    print("7 is also there")

print(num_list[0:-2]) #print(num_list[0:len(num_list)-2])
print(num_list[0:len(num_list):2]) #Value Jumps by 2