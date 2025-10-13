#MultiProcessing In Python

import multiprocessing
import concurrent.futures
import requests

def download_photos(url , name):
    response = requests.get(url)
    open(f"Photos/{name}.jpg", "wb").write(response.content)

urls = []

for i in range(10):
    urls.append(f"https://picsum.photos/id/{i+1}/2000/3000")

#Without MultiProcessing
#Download 1 by 1 and takes much time
# for index, url  in enumerate(urls):
#     download_photos(url , index)



#----------------------------------------------
#Use Multiple Processors in CPU to work parallelly

#With Basic MultiProcessing
# if(__name__ == "__main__"):
#     processes = []
#     for index, url  in enumerate(urls):
#         p = multiprocessing.Process(target=download_photos , args=[url , index])
#         p.start()
#         processes.append(p)

#     for pr in processes:
#         pr.join()

#-----------------------------------------------

#Advance MultiProcessing
if(__name__ == "__main__"):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_photos , urls ,(i for i in range(10)))
    
