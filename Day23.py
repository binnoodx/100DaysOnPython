# List Methods in Python

my_list = [1,2,3]
print(my_list)
my_list.append(4)
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)


print(my_list.index(2))

print(my_list.count(1))

my_second_list = [5,6,7]
my_list.extend(my_second_list)
print(my_list)

copy_list = my_list.copy() #copy and make a new list. 
### we cannot do like  
### copy_list = my_list
### while changing copy_list it affects my_list also

copy_list.insert(8,7) #Insert 8 in index 7
