# Global and Local Variables

x = 10; #Global variable

# def change():
#     x = 4; # This change doesn't update global variable
#     print(f"Inside function X is {x}")
# change()

def change():
    global x  # By this we can update global variables inside Function
    print(f"Inside function X is {x}")

change()


print(f"Outside Function X is {x}")
