import requests

BOT_TOKEN = "8483160777:AAG872i0TMAxuAXcB6ZhqjcooPSoapo_y-U"
CHAT_ID = "534605127"

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": "Bot is working"
    }
)

print("Message sent")
