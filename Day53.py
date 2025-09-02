# Map , Filter and Reduce in Python

my_list = [1,2,3,4,5]
squared_list = list(map(lambda x:x*x , my_list))  #Map Every Element of older list to function and makes new list
print(squared_list)

raw_list = [1,2,3,4,5,6,7]
even_list = list(filter(lambda num:num%2==0 , raw_list)) #Filter those members in older list which are returned true through function
print(even_list)

from functools import reduce

raw_list2 = [1,2,3,4,5,6]
sumOfElement = reduce(lambda a,b:a+b , raw_list2) #Takes two element and pass to function and reduce them to one and redo until last element remains
print(sumOfElement)