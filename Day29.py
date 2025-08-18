### Docstrings in Python

def sum(a,b):

    #always put docstring above all

    '''Hey Friends , This function Print Sum of two numbers'''  #Just like Comment but can be printed unlike Comment
    
    print("The Sum Is " , a+b)
    print(sum.__doc__)  

sum(5,6)