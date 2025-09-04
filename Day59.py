#Decorators in python

def greetings(fx):
    def modify(*args , **kwargs):  #Since 2,3 from sum(2,3) cannot reach directly to fx() we use *args , **kwargs as arguments
        
        print("Function Starts")  #Run before Function Execution
        fx(*args , **kwargs) #Run Function
        print("Function Ends , Thanks for Using this Function") #Run after Function Execution
    return modify

@greetings #Apply Greeting Function for all Functions

def sum(a,b):
    print("The Sum is ", a+b)
sum(2,3)