### Difference Between == and is


#### ------- Case I ------- ####
a=3 #Constant and isn't changeble
b=3 #Constant and isn't changeble

# Python make one memory for a and since a is not changable b also use same memory location
print(a is b) #True ---> is return true if memory location is same
print(a == b) #True ---> == return true if value is same


#### ------- Case II ------- ####
list_1 = [1,2,3]
list_2 = [1,2,3]
# Python make one memory for list_1 and since list_1 is changable so list_2 use another memory location
print(list_1 is list_2) #False ---> is return false if memory location is different
print(list_1 == list_2) #True ---> is return true if memory location is same

