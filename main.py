import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
CMC_API_KEY = os.environ.get("CMC_API_KEY")

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/new"
headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}
params = {"limit": 10}

response = requests.get(url, headers=headers, params=params)
data = response.json()

print("Response:", data)

if "data" not in data:
    send_telegram(f"⚠️ API Error: {data}")
    exit()

coins = data["data"]

for coin in coins:
    message = (
        f"🆕 <b>New Listing Alert!</b>\n"
        f"🪙 Name: {coin['name']}\n"
        f"💎 Symbol: {coin['symbol']}\n"
        f"💰 Price: ${coin['quote']['USD']['price']:.6f}\n"
        f"📅 Added: {coin['date_added'][:10]}"
    )
    send_telegram(message)

print("Done")
