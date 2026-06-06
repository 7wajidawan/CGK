import requests

BOT_TOKEN = "8483160777:AAG872i0TMAxuAXcB6ZhqjcooPSoapo_y-U"
CHAT_ID = "534605127"

url = "https://api.coingecko.com/api/v3/coins/list/new"

response = requests.get(url)

print("STATUS:", response.status_code)
print("RESPONSE:", response.text)

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": "Bot is working"
    }
)
