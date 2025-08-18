# Recursion in Python 

# To calculate Factorial

def fact(num):

    if(num == 0 or num ==1):
        return 1
    else:
        return num * fact(num-1)

user_inp = int(input("Enter number to calculate Factorial : "))
output = fact(user_inp)
print("The Factorial of " , user_inp , "is" , output)


#Without Using Recursion

def fibo(num):
    num_1 = 0
    num_2 = 1
    counter = 0
    temp =0
    my_list = []

    while(counter != num/2):
        my_list.append(num_1)
        my_list.append(num_2)

        temp = num_1 + num_2

        num_1 = num_1 + num_2
        num_2 = num_2 + temp
        counter = counter + 1

    print(my_list)    

user_inp = int(input("How many numbers you want to display ?"))
fibo(user_inp)




# Using Recursion

def fibo(num):
    if(num == 1):
        return 0
    elif(num == 2):
        return 1;
    else:
        return (fibo(num-1)+fibo(num-2))
    

user_input = int(input("How many terms you want to display? : "))

for i in range(1,user_input+1):
    output = fibo(i)
    print(output)