import requests
import os
import json

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

# Load seen coins to avoid duplicates
SEEN_FILE = "seen_coins.json"
try:
    with open(SEEN_FILE, "r") as f:
        seen_coins = set(json.load(f))
except:
    seen_coins = set()

# Get all coins from CoinPaprika
url = "https://api.coinpaprika.com/v1/coins"
response = requests.get(url)
coins = response.json()

# Filter unranked (newest) coins
new_coins = [c for c in coins if c["rank"] == 0]

found = 0

for coin in new_coins:
    if coin["id"] in seen_coins:
        continue

    # Get ticker data
    ticker_url = f"https://api.coinpaprika.com/v1/tickers/{coin['id']}"
    ticker = requests.get(ticker_url).json()

    usd = ticker.get("quotes", {}).get("USD", {})
    volume = usd.get("volume_24h", 0) or 0
    market_cap = usd.get("market_cap", 0) or 0

    # Get detail data
    detail_url = f"https://api.coinpaprika.com/v1/coins/{coin['id']}"
    detail = requests.get(detail_url).json()

    contracts = detail.get("contracts", [])
    contract_address = contracts[0].get("contract", None) if contracts else None

    # Apply filters
    if volume < 1000:
        continue
    if market_cap < 100000:
        continue
    if not contract_address:
        continue

    # Mark as seen
    seen_coins.add(coin["id"])

    coin_link = f"https://coinpaprika.com/coin/{coin['id']}"

    message = (
        f"🆕 <b>New Listing Alert!</b>\n"
        f"🪙 <b>Name:</b> {coin['name']}\n"
        f"💎 <b>Symbol:</b> {coin['symbol']}\n"
        f"📊 <b>24h Volume:</b> ${volume:,.0f}\n"
        f"🏦 <b>Market Cap:</b> ${market_cap:,.0f}\n"
        f"📋 <b>Contract:</b> <code>{contract_address}</code>\n"
        f"🔗 <b>Link:</b> {coin_link}"
    )
    send_telegram(message)
    found += 1

    if found >= 5:
        break

# Save seen coins
with open(SEEN_FILE, "w") as f:
    json.dump(list(seen_coins), f)

print(f"Done. Found {found} new coins.")
