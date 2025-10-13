import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("Image1.jpg", "wb").write(response.content)
   

  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("Image2.jpg", "wb").write(response.content)
  


async def main():
#Run Code 1 by 1 taking equal time by both

    # await function1()
    # await function2()
    

#Run Code in Parallel so that both code run by same time
  await asyncio.gather(
        function1(),
        function2(),
  )

#    


asyncio.run(main())