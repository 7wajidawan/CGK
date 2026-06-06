import requests

BOT_TOKEN = "8483160777:AAG872i0TMAxuAXcB6ZhqjcooPSoapo_y-U"
CHAT_ID = "534605127"

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

# Fetch new listings from CoinGecko
url = "https://api.coingecko.com/api/v3/coins/list/new"
response = requests.get(url)
coins = response.json()  # Returns a LIST ✅

for coin in coins[:10]:
    message = (
        f"🆕 <b>New CGK Listing!</b>\n"
        f"🪙 Name: {coin['name']}\n"
        f"💎 Symbol: {coin['symbol'].upper()}\n"
        f"🆔 ID: {coin['id']}\n"
        f"⏰ Activated: {coin['activated_at']}"
    )
    send_telegram(message)

print("Done")


# Updated v2
