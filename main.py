import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

url = "https://api.coingecko.com/api/v3/coins/list/new"
response = requests.get(url)
data = response.json()

print("Type:", type(data))
print("Data:", data)
