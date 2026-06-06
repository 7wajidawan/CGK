import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

# CoinPaprika - completely free, no API key
url = "https://api.coinpaprika.com/v1/coins"
response = requests.get(url)
coins = response.json()

# Sort by newest (highest id number = newest)
new_coins = sorted(coins, key=lambda x: x["rank"] == 0, reverse=True)[:10]

for coin in new_coins:
    message = (
        f"🆕 <b>New Listing Alert!</b>\n"
        f"🪙 Name: {coin['name']}\n"
        f"💎 Symbol: {coin['symbol']}\n"
        f"🔗 Type: {coin['type']}"
    )
    send_telegram(message)

print("Done")
