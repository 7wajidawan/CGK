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

url = "https://api.coinpaprika.com/v1/coins"
response = requests.get(url)
coins = response.json()

new_coins = [c for c in coins if c["rank"] == 0][:5]

for coin in new_coins:
    ticker_url = f"https://api.coinpaprika.com/v1/tickers/{coin['id']}"
    ticker = requests.get(ticker_url).json()

    price = ticker.get("quotes", {}).get("USD", {}).get("price", "N/A")
    volume = ticker.get("quotes", {}).get("USD", {}).get("volume_24h", "N/A")
    first_data = ticker.get("first_data_at", "N/A")[:10]

    message = (
        f"🆕 <b>New Listing Alert!</b>\n"
        f"🪙 <b>Name:</b> {coin['name']}\n"
        f"💎 <b>Symbol:</b> {coin['symbol']}\n"
        f"🔗 <b>Type:</b> {coin['type']}\n"
        f"📅 <b>First Listed:</b> {first_data}\n"
        f"💰 <b>Price:</b> ${price}\n"
        f"📊 <b>24h Volume:</b> ${volume}"
    )
    send_telegram(message)

print("Done")
