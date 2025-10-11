#Requests in PYthon

import requests
from bs4 import BeautifulSoup

response = requests.get("https://binodx.vercel.app") #Get Request

soup = BeautifulSoup(response.text , "html.parser")

print(soup.prettify())



#Post Request
url = "https://binodx.vercel.app"
data = {
    "name":"binod"
}
headers = {
    "content-type":"application/json; charset=UFT-8"
}
response = requests.post(url , headers=headers , json=data)
print(response)