import requests

# ⚠️ Replace with your actual Telegram bot values
TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert(message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=payload)
        print("📱 Alert sent successfully!")

    except:
        print("❌ Failed to send alert")
