import requests
import json

class TelegramNotifier:
    def __init__(self, settings):
        self.bot_token = settings.telegram_bot_token
        self.chat_id = settings.telegram_chat_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response.json()
