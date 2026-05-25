from flask import Flask, request
import requests
import os

app = Flask(__name__)
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")

# EDIT YOUR LISTINGS HERE
LISTINGS = {
    "PRICE_1": [
        {
            "title": "15x30 မြေကွက် လှိုင်",
            "subtitle": "သိန်း80 - 3BR, 2Bath",
            "image_url": "https://via.placeholder.com/400x300.png?text=House+1"
        }
    ],
    "PRICE_2": [],
    "PRICE_3": [],
    "PRICE_4": [],
    "PRICE_5": [],
    "PRICE_6": [],
    "PRICE_7": []
}

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == os.environ.get("VERIFY_TOKEN"):
            return request.args.get("hub.challenge")
        return "Invalid token", 403

    if request.method == 'POST':
        data = request.get_json()
        
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                if "message" in event:
                    sender_id = event["sender"]["id"]
                    payload = event.get("message", {}).get("quick_reply", {}).get("payload", "")
                    text = event.get("message", {}).get("text", "")
                    message_data = payload if payload else text

                    if message_data in LISTINGS:
                        send_listings_carousel(sender_id, message_data)
                    else:
                        send_welcome_with_buttons(sender_id)
        
        return "ok", 200

def send_welcome_with_buttons(recipient_id):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": "👩🏻‍💼🏘️🏡🏘️👩🏻‍💼 Ma Thin Yu အိမ်ခြံမြေအကျိုးဆောင်မှာကြိုဆိုပါတယ် 📞 Contact :09424006004 📞 💜 Viber : 09767975004 💜 💙 Facebook : သင်းယု အိမ်ခြံမြေအကျိုးဆောင် 💙 🤍အိမ်ကြည့်မယ်ဆို 3နာရီကြိုဆက်ပေးပါ🤍\n\nဘယ်စျေးနှုန်းအကွာအဝေးကို ကြည့်ချင်လဲ?",
            "quick_replies": [
                {"content_type": "text", "title": "1.သိန်း၁သောင်းအောက်", "payload": "PRICE_1"},
                {"content_type": "text", "title": "2.သိန်း၂သောင်း", "payload": "PRICE_2"},
                {"content_type": "text", "title": "3.သိန်း၃သောင်း", "payload": "PRICE_3"},
                {"content_type": "text", "title": "4.သိန်း၄သောင်း", "payload": "PRICE_4"},
                {"content_type": "text", "title": "5.သိန်း၅သောင်း", "payload": "PRICE_5"},
                {"content_type": "text", "title": "6.သိန်း၆သောင်း", "payload": "PRICE_6"},
                {"content_type": "text", "title": "7.သိန်း၇သောင်း", "payload": "PRICE_7"}
            ]
        }
    }
    requests.post(url, json=payload)

def send_listings_carousel(recipient_id, price_key):
    listings = LISTINGS.get(price_key, [])
    
    if not listings:
        send_message(recipient_id, "လောလောဆယ် ဒီစျေးနှုန်းမှာ အိမ်မရှိသေးပါဘူး။ နောက်တခု ရွေးပေးပါ။")
        return

    elements = []
    for item in listings:
        elements.append({
            "title": item["title"],
            "subtitle": item["subtitle"],
            "image_url": item["image_url"],
            "buttons": [
                {
                    "type": "phone_number",
                    "title": "ဆက်သွယ်ရန်",
                    "payload": "+959424006004"
                }
            ]
        })

    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements
                }
            }
        }
    }
    requests.post(url, json=payload)

def send_message(recipient_id, text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    requests.post(url, json=payload)
