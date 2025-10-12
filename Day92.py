#Function Caching in Python

import functools
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def func(num):
    time.sleep(5)
    return num*5

print(func(10))
print("Printed After 5 sec") #Run after 5 second
print(func(20))
print("Printed After 5 sec")


print(func(10))
print("Printed Instantly") #Since the function already compute for 10 it instantly returns
print(func(20))
print("Printed Instantly")