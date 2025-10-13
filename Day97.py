#MultiThreading In Python

from concurrent.futures import ThreadPoolExecutor
import time
import threading
def func1(seconds):
    time.sleep(seconds)

#No Threading
print("No threading Start")
init_time = time.perf_counter()
func1(4)
func1(2)
finaltime = time.perf_counter()
execution_time = finaltime - init_time
print(f"Code by No Threading Run In {execution_time} Seconds")



#Basic Threading
print("Basic Threading Starts")
init_time = time.perf_counter()
t1 =threading.Thread(target=func1 , args=[4])
t2 =threading.Thread(target=func1 , args=[2])
t1.start() #Start parallelly
t2.start() #Start parallelly

t1.join() #Wait till large code runs
t2.join()

finaltime = time.perf_counter()
execution_time = finaltime - init_time
print(f"Code by Basic Threading Run In {execution_time} Seconds")


#Advance Threading
print("Advance Threading Starts")
def polingDemo():
    #Method 1
    with ThreadPoolExecutor() as executor:
        init_time = time.perf_counter()
        f1 = executor.submit(func1 , 4)
        f2 = executor.submit(func1 , 2)
        print(f1.result())
        print(f2.result())
        finaltime = time.perf_counter()
        execution_time = finaltime - init_time
        print(f"Code by Advance Threading - Method 1 Run In {execution_time} Seconds")

        #Method2
        init_time = time.perf_counter()
        results = executor.map(func1 , [4,2])
        for result in results:
            pass
        finaltime = time.perf_counter()
        execution_time = finaltime - init_time
        print(f"Code by Advance Threading - Method 2 Run In {execution_time} Seconds")
    
polingDemo()



