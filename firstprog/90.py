#Excercise 10
import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/top-headlines?q={query}&from=2024-01-10&sortBy=publishedAt&apiKey=0a30c842ab6543bb831d4e386e656895"
r = requests.get(url)
# s=r.text
# for text in s:
#     if "url" in text:
#         print("\n")

s=r.text.replace("url","\n")

print(s)