import time
import requests

print("\n\n----- Welcome to News App -----")
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print("\n")


url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=def3350a64854009819d04e5dde1f0cf')


response = requests.get(url)
news_data = response.json()

print("Todays Top News\n")

for idx, article in enumerate(news_data.get("articles")):
    print(f"{idx+1}. {article['title']}")
    print(f"   {article['description']}\n")

