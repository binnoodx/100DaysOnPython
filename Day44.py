### How Import Functions work ?

import math #Import all functions inside math
from math import sqrt #import only one function
from math import sin as s #Can give custom name

from Day43 import hello #Import module or any variable from another file
hello()


print(dir(math)) # Show all Functions inside Math

def hey():
    print("Hey , Hello Form Day 44")

if __name__ == "__main__":
    hey()
