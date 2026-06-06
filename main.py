import requests
import os

BOT_TOKEN = os.environ.get("8483160777:AAG872i0TMAxuAXcB6ZhqjcooPSoapo_y-U")
CHAT_ID = os.environ.get("534605127")

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

url = "https://api.coingecko.com/api/v3/coins/list/new"
response = requests.get(url)
data = response.json()

# Handle both list and dict response
if isinstance(data, list):
    coins = data
elif isinstance(data, dict):
    coins = data.get("coins", data.get("data", []))
else:
    coins = []

for coin in coins[:10]:
    message = (
        f"🆕 <b>New CGK Listing!</b>\n"
        f"🪙 Name: {coin['name']}\n"
        f"💎 Symbol: {coin['symbol'].upper()}\n"
        f"🆔 ID: {coin['id']}"
    )
    send_telegram(message)

print("Done")
