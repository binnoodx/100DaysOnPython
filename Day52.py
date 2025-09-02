#Lambda Functions in Python

#Traditional Way
def sum(a,b):
    return a+b
print(sum(2,3))

#One Liner (Lambda Function)

sum_2 = lambda x,y:x+y
print(sum_2(2,3))

#Passing Function as Argument

def square_of_sum(fx):
    print(fx(2,3)*fx(2,3))
square_of_sum(sum_2)
