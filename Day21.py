# Return Statements in Python

def average(a,b):
    return (a+b)/2

result = average(2,4)
print("The Average is ", result)

def sum(*numbers): # Accept Tuple
    sum = 0;
    for number in numbers:
        sum = sum + number
    return sum

result = sum(1,2,3,4,5)
print("The Sum is ", result)



def fullName(**name): # Accept Dict
    print("Hello, " ,name["firstName"] , name["lastName"])
fullName(firstName="Binod", lastName="X")