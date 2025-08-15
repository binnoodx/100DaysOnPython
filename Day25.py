# Tuple Methods in Python

### Indirect change in Tuple
my_tup = (1,2,3)
print("Before : " , my_tup)


temp_list = list(my_tup)
temp_list.append(4)

my_tup = tuple(temp_list)
print("After : " , my_tup)
