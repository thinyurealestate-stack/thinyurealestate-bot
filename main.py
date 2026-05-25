from flask import Flask, request
import requests
import os

app = Flask(_name_)
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verification
        if request.args.get("hub.verify_token") == os.environ.get("VERIFY_TOKEN"):
            return request.args.get("hub.challenge")
        return "Invalid token", 403

    if request.method == 'POST':
        data = request.get_json()
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                if "message" in event:
                    sender_id = event["sender"]["id"]
                    send_message(sender_id, "Hey! Got your message 👋")
        return "ok", 200

def send_message(recipient_id, text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    requests.post(url, json=payload)
