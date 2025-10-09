# Shoutout To Everyone Problem

#pip install pywin32

from win32com.client import constants
import win32com.client
import pythoncom
speaker = win32com.client.Dispatch("SAPI.SpVoice")


persons = ["Binod", "Harry" , "Rauda" , "Saya"]

for name in persons:
    speaker.Speak(f"A Big ShoutOut to {name}")
 


