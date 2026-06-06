import requests
import os

BOT_TOKEN = os.environ.get("8483160777:AAG872i0TMAxuAXcB6ZhqjcooPSoapo_y-U")
CHAT_ID = os.environ.get("534605127")

url = "https://api.coingecko.com/api/v3/coins/list/new"
response = requests.get(url)
data = response.json()

print("Type:", type(data))
print("Data:", data)
