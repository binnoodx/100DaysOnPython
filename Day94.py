"""

Write a python program which reminds you of drinking water every hour or two. Your 
program can Beep

"""

#pip install  AudioPlayer 
from  audioplayer import AudioPlayer 
import time




isManAlive = True

while(isManAlive):
    time.sleep(1*60*60)
    print("\nHey , Drink Some Water. Stay Hydrated !\n")
    AudioPlayer("beep.mp3").play(block=True)




