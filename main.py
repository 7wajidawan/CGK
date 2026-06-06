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

    detail_url = f"https://api.coinpaprika.com/v1/coins/{coin['id']}"
    detail = requests.get(detail_url).json()

    volume = ticker.get("quotes", {}).get("USD", {}).get("volume_24h", "N/A")

    contracts = detail.get("contracts", [])
    contract_address = contracts[0].get("contract", "N/A") if contracts else "N/A"

    coin_link = f"https://coinpaprika.com/coin/{coin['id']}"

    message = (
        f"🆕 <b>New Listing Alert!</b>\n"
        f"🪙 <b>Name:</b> {coin['name']}\n"
        f"💎 <b>Symbol:</b> {coin['symbol']}\n"
        f"📊 <b>24h Volume:</b> ${volume}\n"
        f"📋 <b>Contract:</b> <code>{contract_address}</code>\n"
        f"🔗 <b>Link:</b> {coin_link}"
    )
    send_telegram(message)

print("Done")
