 # Finally Keyword in Python


def checkEven(num):
    try:
        if(int(num)%2 == 0):
            return(1)
        else:
            return(0)

    except:
        return(404)

    finally:
        print("Execution Over") ## Can be executed even after return statement

    print("Execution Over")  ## Don't Run 

result = checkEven(input("Enter Any Number : "))

if(result == 0):
    print("Odd Number")
elif(result == 404):
    print("Invalid Number")
else:
    print("Even Number")
