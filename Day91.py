#Generators in Python

#ClassicMethod
def using_list():
    my_list = list()
    for i in range(100):
        my_list.append(i)
        #Store Value in List until loop is over and consume more memory
    return my_list
print(using_list())




#Newer Method
def using_generator():
    for j in range(100):
        yield j
    #No store of value and same task
for k in using_generator():
    print(k)