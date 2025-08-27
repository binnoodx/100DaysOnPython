#Custom Errors in Python

num = int(input("Enter Any Even Number : "))

if(num % 2 != 0):
    raise ValueError("I told you to give even Number")
else:
    print("Good Job")

    ## We can also give SyntaxError , MemoryError , IndexError etc
