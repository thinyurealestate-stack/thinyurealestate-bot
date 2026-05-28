import os
import requests
from flask import Flask, request

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "thinyurealestate")

# ========== YOUR LISTINGS DATA ==========
LISTINGS = {
    "PRICE_1": [
        {
            "title": "အမြန်ရောင်းမည် အင်းစိန်မြို့နယ်",
            "subtitle": "ခြံအကျယ် 18×80 ပေ, 2BN နှစ်ထပ်အိမ်",
            "image_url": "https://i.postimg.cc/rmTRnYJK/Image-25-05-2026-at-4-44-PM-(4).png",
            "facebook_url": "https://www.facebook.com/share/p/1DaozjPCxM/"
        }
    ],
    "PRICE_2": [
        {
            "title": "9မိုင် ပြည်လမ်းမဒဲ့ပေါက် အိမ်ခြံရောင်းမည်",
            "subtitle": "ခြံအကျယ် 40×80 ပေ, 11000 သိန်း",
            "image_url": "https://i.postimg.cc/RZbjLkv4/Image-26-05-2026-at-1-15-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1HdcYcGFfY/"
        }
    ]
}

# ========== HELPER FUNCTIONS ==========

def send_message(recipient_id, text):
    """Send a simple text message"""
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    try:
        response = requests.post(url, json=payload)
        print(f"Sent message: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_price_quick_replies(recipient_id):
    """Send price range quick replies"""
    label_map = {
        "PRICE_1": "1.သိန်း၁သောင်းအောက်",
        "PRICE_2": "2.သိန်း၂သောင်းအောက်",
        "PRICE_3": "3.သိန်း၃သောင်းအောက်", 
        "PRICE_4": "4.သိန်း၄သောင်းအောက်",
        "PRICE_5": "5.သိန်း၅သောင်းအောက်",
        "PRICE_6": "6.သိန်း၆သောင်းအောက်",
        "PRICE_7": "7.သိန်း၇သောင်းအောက်",
        "PRICE_8": "8.သိန်း၈သောင်းအောက်",
        "PRICE_9": "9.သိန်း၉သောင်းအောက်",
        "PRICE_10": "10.သိန်းကြီးတန်အိမ်များ"
    }

    quick_replies = []
    for key, items in LISTINGS.items():
        if len(items) > 0:
            quick_replies.append({
                "content_type": "text",
                "title": label_map.get(key, key),
                "payload": key
            })

    if quick_replies:
        url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
        payload = {
            "recipient": {"id": recipient_id},
            "message": {
                "text": "စျေးနှုန်း ရွေးပါ:",
                "quick_replies": quick_replies
            }
        }
        requests.post(url, json=payload)

def send_welcome_with_buttons(recipient_id):
    """Send welcome message with price range buttons"""
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": "မင်္ဂလာပါ အိမ်ခြံမြေအကျိုးဆောင်မှ ကြိုဆိုပါတယ်\n\nContact: 09424006004\n\nအိမ်ကြည့်မယ်ဆို 3နာရီကြိုဆက်ပေးပါ",
            "quick_replies": [
                {"content_type": "text", "title": "1.သိန်း၁သောင်းအောက်", "payload": "PRICE_1"},
                {"content_type": "text", "title": "2.သိန်း၂သောင်းအောက်", "payload": "PRICE_2"},
                {"content_type": "text", "title": "3.သိန်း၃သောင်းအောက်", "payload": "PRICE_3"},
                {"content_type": "text", "title": "4.သိန်း၄သောင်းအောက်", "payload": "PRICE_4"},
                {"content_type": "text", "title": "5.သိန်း၅သောင်းအောက်", "payload": "PRICE_5"},
                {"content_type": "text", "title": "6.သိန်း၆သောင်းအောက်", "payload": "PRICE_6"},
                {"content_type": "text", "title": "7.သိန်း၇သောင်းအောက်", "payload": "PRICE_7"},
                {"content_type": "text", "title": "8.သိန်း၈သောင်းအောက်", "payload": "PRICE_8"},
                {"content_type": "text", "title": "9.သိန်း၉သောင်းအောက်", "payload": "PRICE_9"},
                {"content_type": "text", "title": "10.သိန်းကြီးတန်အိမ်များ", "payload": "PRICE_10"}
            ]
        }
    }
    try:
        response = requests.post(url, json=payload)
        print(f"Sent welcome: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_listings_carousel(recipient_id, price_key):
    """Send property listings as a carousel"""
    listings = LISTINGS.get(price_key, [])
    
    if not listings:
        send_message(recipient_id, "လောလောဆယ် ဒီစျေးနှုန်းမှာ အိမ်မရှိသေးပါဘူး")
        send_price_quick_replies(recipient_id)
        return
    
    elements = []
    for item in listings:
        elements.append({
            "title": item["title"][:80],
            "subtitle": item["subtitle"][:80],
            "image_url": item["image_url"],
            "buttons": [
                {
                    "type": "web_url",
                    "url": item["facebook_url"],
                    "title": "အသေးစိတ်ကြည့်ရန်"
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
    try:
        response = requests.post(url, json=payload)
        print(f"Sent carousel: {response.status_code}")
        
        # Send follow-up message
        send_message(recipient_id, "👉 နောက်ထပ် စျေးနှုန်းတွေကိုလည်း အောက်မှာဆွဲ၍ နှိပ်ကြည့်နိုင်ပါတယ်:")
        send_price_quick_replies(recipient_id)
    except Exception as e:
        print(f"Error: {e}")

# ========== WEBHOOK ==========

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge
        return "Invalid token", 403

    data = request.get_json()
    if not data:
        return "OK", 200
    
    try:
        for event in data.get('entry', []):
            for messaging_event in event.get('messaging', []):
                sender_id = messaging_event.get('sender', {}).get('id')
                
                if not sender_id:
                    continue
                
                # Handle messages
                if 'message' in messaging_event:
                    message = messaging_event['message']
                    
                    if 'text' in message:
                        message_text = message['text'].lower().strip()
                        print(f"Received: {message_text}")
                        
                        if message_text in ['hi', 'hello', 'start', 'help']:
                            send_welcome_with_buttons(sender_id)
                        else:
                            send_message(sender_id, "မင်္ဂလာပါ။ စာရင်းကြည့်ရန် 'hi' လို့ရိုက်ပါ။")
                    
                    if 'quick_reply' in message:
                        payload = message['quick_reply'].get('payload', '')
                        if payload.startswith('PRICE_'):
                            send_listings_carousel(sender_id, payload)
                
                # Handle postbacks
                elif 'postback' in messaging_event:
                    payload = messaging_event['postback'].get('payload', '')
                    if payload.startswith('PRICE_'):
                        send_listings_carousel(sender_id, payload)
                
                # Handle inbox_labels
                if 'inbox_labels' in messaging_event:
                    user_id = messaging_event['recipient']['id']
                    added_labels = messaging_event['inbox_labels'].get('added_labels', [])
                    for label in added_labels:
                        label_name = label.get('page_label_name', label.get('label_name', ''))
                        print(f"Label: {label_name}")
                        
                        if label_name == 'Hot Lead':
                            send_message(user_id, "မင်္ဂလာပါ VIP ဖောက်သည်မာကြီး")
                
                # Log other events
                if 'delivery' in messaging_event:
                    print("Message delivered")
                if 'read' in messaging_event:
                    print("Message read")
                if 'reaction' in messaging_event:
                    print("Reaction received")
                if 'referral' in messaging_event:
                    print("Referral received")
                if 'pass_thread_control' in messaging_event:
                    print("Handover received")
                if 'standby' in messaging_event:
                    print("Standby event")
                        
    except Exception as e:
        print(f"Error: {e}")

    return "OK", 200

@app.route('/', methods=['GET'])
def health_check():
    return "Bot is running!", 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
