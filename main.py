import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://api.coingecko.com/api/v3/coins/list/new"

response = requests.get(url)
coins = response.json()

message = "🆕 Latest CoinGecko Listings\n\n"

if isinstance(coins, list):
    for coin in coins[:10]:
        message += f"• {coin['name']} ({coin['symbol']})\n"
else:
    message += str(coins)

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
