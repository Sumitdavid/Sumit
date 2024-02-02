import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/top-headlines?q={query}&from=2024-01-11&sortBy=publishedAt&apiKey=0a30c842ab6543bb831d4e386e656895"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")