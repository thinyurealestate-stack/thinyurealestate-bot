from flask import Flask, request
import os
import requests

app = Flask(_name_)

PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # 1. Handle GET for Meta verification
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Wrong token", 403

    # 2. Handle POST for messages - reply 200 immediately
    return "ok", 200

def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    requests.post(url, json=payload)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
