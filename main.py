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
            "title": "အင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး-ဘုရင့်နောင်လမ်းမကြီးဒဲ့ပေါက်,ကားလမ်း၂စီးရှောင်လမ်း-အသင့်နေရုံ-2BN အိမ်ကောင်း",
            "subtitle": "8× 80 ပေအကျယ် 🏡2 BN နှစ်ထပ်အိမ် အသင့်သင့် , 💸ရောင်းစျေး4400(ညှိ့နိူင်း)",
            "image_url": "https://i.postimg.cc/rmTRnYJK/Image-25-05-2026-at-4-44-PM-(4).png",
            "facebook_url": "https://www.facebook.com/share/p/1DaozjPCxM/"
        },
        {
            "title": "ကျောက်ရေတွင်း,မိန်လမ်းမပေါ်,,သဗ္ဗညုပုထိုးတော်ကြီး အနီး,ကားနှစ်စီးရှောင် မိန်လမ်မပေါ်",
            "subtitle": "၃၀ × ၈၀ ပေ,၈၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/PJgjy0Wz/Image-25-05-2026-at-5-08-PM-(5).png",
            "facebook_url": "https://www.facebook.com/share/p/1duXavUZYd/"
        },
        {
            "title": "အင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး,လမ်းမကြီးမှကားနဲ့ ၁မီးနှစ်သာဝင်ရ,ဘဏ်နီး-ကျောင်းနီ-စျေးနီး",
            "subtitle": "25x60,6500(ညှိ့နိူင်း)",
            "image_url": "https://i.postimg.cc/fymwGwT8/Image-26-05-2026-at-1-12-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1EwVh5nBds/"
        },
        {
            "title": "ရန်ကုန် လေဆိပ် အနီး,ကားနှစ်စီးရှောင် မိန်းလမ်မပေါ်,သဗ္ဗညုပုထိုးတော်ကြီး အနီး",
            "subtitle": "၂၅ × ၆၀ ပေ,၅၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/FR654bv1/Image-28-05-2026-at-11-44-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1AxEFygDE1/"
        },
        {
            "title": "မရမ်းကုန်း မြို့နယ်  ၅ရပ်ကွက်,သဗ္ဗညုပုထိုးတော်ကြီး အနီး,ကျောက်ရေတွင်း လမ်းမ အနီး,ကားနှစ်စီးရှောင် လမ်းကျယ်",
            "subtitle": "၄၀ × ၆၀ ပေ,၇၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/d3FXv5Xs/Image-25-05-2026-at-5-14-PM-(1).png",
            "facebook_url": "https://www.facebook.com/share/p/1Ffm963ffL/"
        },
        {
            "title": "သာကေတမြို့နယ်,အောင်သပြေ အနောက်( -)လမ်း,၇ရပ်ကွက် -ပျဉ်ထောင်အိမ်,ဂရံအမည်ပေါက်",
            "subtitle": "၄၀x၆၀ပေကျယ်,သိန်း ၈၅၀၀ (ညှိ့နိူင်းစျေး)",
            "image_url": "https://i.postimg.cc/0N7cKZY4/Image-29-05-2026-at-1-52-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Eev1FQdnA/"
        },
        {
            "title": "စရံဦးသူယူပါ,မင်းနန်ဒါလမ်းမကြီး ဒဲ့ဆင်း ၂လမ်းမြှောက်,စျေးနီးကျောင်းနီးဘဏ်နီးမှတ်တိုင်အနီးcapitalနီး",
            "subtitle": "၁၂ပေ ခွဲ ပေ၅၀,၁၀၉၀ပါးပါးညှိနှိုင်း",
            "image_url": "https://i.postimg.cc/MGj3zq3f/IMG-5244.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Eev1FQdnA/"
        },
        {
            "title": "Spring Line Hotel ကပ်လျက်,လမ်းမမေးတင်-လူစည်ကားသောနေရာကောင်း,ဘိုးဘပိုင်မြေ",
            "subtitle": "27x78.3000-သိန်း(ညှို့နိူင်း)",
            "image_url": "https://i.postimg.cc/tJy9hrnN/IMG-5253.jpg",
            "facebook_url": "https://www.facebook.com/share/p/172BwdwPeK/"
        },
        {
            "title": "သိန်း၃၀၀၀(ပါးပါးရှော့)မှော်ဘီမြို့နယ်-မင်္ဂလာကုန်းရွာ,ခြံကျယ် ၁ ဧကခွဲ,မြေ အမျိုးစား-G -မြေ",
            "subtitle": "ပေကျယ် ၄၀x၉၀ (၆၀၀),၁၅၀x၁၅၀(၃၀၀၀),၁၀၅x၁၅၀(၂၈၀၀),၁၀၀x၂၀၀(၁၅၀၀)",
            "image_url": "https://i.postimg.cc/nzXFFjbN/post-558794-featured.jpg",
            "facebook_url": "https://www.facebook.com/share/r/18YgKNwfCC/"
        }
    ],
    "PRICE_2": [
        {
            "title": "၉မိုင် ပြည်လမ်းမဒဲ့ပေါက် နေရာကောင်းလမ်းမ အနီး အိမ်နှင့်ခြံ,မရမ်းကုန်မြို့နယ် ၉မိုင် ၅ ရက်ကွက်,ပြည်လမ်း ဒဲ့ပေါက်,Ocean center အနီး,ရန်ကုန်လေဆိပ် အနီး",
            "subtitle": "ခြံ  အကျယ်  ၄၀ × ၈၀ ပေ,သိန်း ၁၁၀၀၀ သိန်း (ညှီနှိုင်စျေး)",
            "image_url": "https://i.postimg.cc/RZbjLkv4/Image-26-05-2026-at-1-15-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1HdcYcGFfY/"
        },
        {
            "title": "ဂရန်အမည်ပေါက်,လမ်းကျယ်,ပတ်ဝန်ကျင်သန့်,အင်းစိန်မြို့နယ် မြို့သစ် ရက်ကွက်,ဘုရင့်နောင် ရိပ်သာ Vip လမ်းသန့်",
            "subtitle": "ခ၃၀ × ၆၀ ပေ အကျယ်,၁၄၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/T3TDmn8f/Image-26-05-2026-at-1-16-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1GeBfDq5Pb/"
        },
        {
            "title": "နာမည်ကြီးမင်းသမီးခြံအနီး,စိတ်ငြိမ်ရပ်ကွက် အမည်ပေါက်,၉ မိုင် ဗိုလ်ညာဏ လမ်းသွယ်,ရန်ကုန် လေဆိပ် အနီး ",
            "subtitle": "ခြံအကျယ် ၃၆ × ၆၂ ပေ,၁၅၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/XY92Ypz5/Image-27-05-2026-at-2-32-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Fx3xqX3TD/"
        },
        {
            "title": "မီး အမြဲမှန်တဲ့,လေဆိပ်လမ်းထဲ လမ်းကျယ်,အင်းစိန်မြို့နယ် စောဘွားကြီးကုန်းရပ်ကွက်,ပြည်လမ်းမကြီး အနီး",
            "subtitle": "ခြံအကျယ် ၆၀ × ၅၅,၁၅၀၀၀ သိန်း ( ညှိနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/jdcHgPmH/Image-27-05-2026-at-2-52-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1GbLC4R9qi/"
        },
        {
            "title": "ရွှေပြည်သာ Vip3 ရပ်ကွက်,အမှတ် ၄လမ်းနဲ့တော်တော်နီး,ခြံရှေ့လမ်းကျယ်,ရေကူးကန် - 15' x 30'",
            "subtitle": "အိမ်အကျယ် - 35' x 55',သိန်း ၁၈,၀၀၀",
            "image_url": "https://i.postimg.cc/KYvp9KM6/Image-26-05-2026-at-1-46-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/17SKswxhxW/"
        },
        {
            "title": "ပြည်လမ်းမကြိး အနီး စျေးတန် တိုက်သစ်,မရမ်းကုန်းမြို့နယ် ၅ရပ်ကွက်",
            "subtitle": "ခြံအကျယ် ၃၅ × ၅၅ ပေ,၁၆၅၀၀ သိန်း (ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/7LF75dwK/Image-29-05-2026-at-12-14-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1CvrKUZjoP/"
        },
        {
            "title": "မရမ်းကုန်းမြို့နယ်ကျိုက်ဝိုင်းအနီး,ဈေးနီး လမ်းမတန်းနီး,၃ ထပ်ခွဲ ရုံး စီးပွားရေးအသင့်သုံး အဆောက်အဦး",
            "subtitle": "မြေအကျယ် (35’ x 70’),(33’ x 55’) အကျယ်ရှိ (၃) ထပ်ခွဲ ,သိန်း 18,000 (ညှိနှိုင်း)",
            "image_url": "https://i.postimg.cc/C1DLZwgd/IMG-5255.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1H2HyMEswu/"
        }
        
    ],
    "PRICE_3": [
        {
            "title": "မီးအမြဲလာတဲ့,လေဆိပ်ရိပ်သာလမ်းမပေါ်_နေရာကောင်း,အိမ်နှင့်ခြံအရောင်း,အင်းစိန်မြို့နယ်,စောဘွားကြီးကုန်းရပ်ကွက်,လေဆိပ်လမ်းမကြီးရဲ ၃ ခြံ မြောက်",
            "subtitle": "70 × 100 ( 7000 Sqft),၂၂၀၀၀ သိန်း (ပိုင်ရှင်တိုက်ရိုက် ညှိနှိုင်း)",
            "image_url": "https://i.postimg.cc/9Q4xCrj2/Image-26-05-2026-at-1-18-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BDGbQti5V/"
        },
        {
            "title": "၉မိုင် ပြည်လမ်းမ အလွန်းနီး လမ်းကျယ်,၉ မိုင် ဘောဂလမ်း,ကားနှစ်စီးရှောင် လမ်းကျယ်",
            "subtitle": "ခြံ အကျယ် 37 × 90 ပေ,၂၉၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/ncXFgtwS/Image-27-05-2026-at-2-57-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1HnUUviamn/"
        }
    ],
    "PRICE_4": [
        {
            "title": "ရင်းနှီးမြှုပ်နှံမလား,ကိုယ်တိုင်နေမလား,ကုမ္ပဏီရုံးခန်းလား,ဝင်ငွေကောင်းတဲ့ Inn ဖွင့်မလား,မရမ်းကုန်မြို့နယ် ၉ မိုင်,ပြည်လမ်း ဒဲ့ပေါက်,ကားနှစ်စီးရှောင် လမ်းကျယ် နေရာကောင်း",
            "subtitle": "၅၅×၁၀၀ ပေ,💵 သိန်း ၄၀၀၀၀ သိန်း (ညှီနှိုင်စျေး)",
            "image_url": "https://i.postimg.cc/FRGbj449/703503390-1602069564214217-7649272277303429298-n.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18czyUKQ2V"
        }
    ],
    "PRICE_5": [],
    "PRICE_6": [],
    "PRICE_7": [],
    "PRICE_8": [],
    "PRICE_9": [],
    "PRICE_10": []
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
            "text": "မင်္ဂလာပါ👩🏻‍💼🏘️🏡\nမသင်းယုအိမ်ခြံမြေအကျိုးဆောင်မှ ကြိုဆိုပါတယ်\n\n💜 Viber : 09767975004 💜\n\n📞 Contact :09424006004 📞\n\n🤍အိမ်ကြည့်မယ်ဆို 3နာရီကြိုဆက်ပေးပါ🤍\n\n🏡အိမ်များကို အောက်ကစျေးနှုန်းအတိုင်းဆွဲ၍ ကြည့်ရူနိုင်ပါတယ်🏡\n\n",
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
                        
                        # Label တစ်ခုချင်းစီအတွက် သင့်တော်တဲ့ တုံ့ပြန်မှု
                if label_name == 'Hot Lead':
                    send_message(user_id, "မင်္ဂလာပါ VIP ဖောက်သည်ကြီး ကြိုဆိုပါတယ်")
                
                elif label_name == 'သတိထားရမည့်သူ':
                    # သတိထားရမည့်သူအတွက် လုပ်စေချင်တဲ့အလုပ်
                    # ဥပမာ - ကိုယ်တိုင်အသေးစိတ်စစ်ဆေးဖို့ Admin ကို အကြောင်းကြားခြင်း
                    send_message(user_id, "ကျေးဇူးပြု၍ အချိန်ယူပြီး စစ်ဆေးပါ။ ကျေးဇူးတင်ပါသည်။")
                    print(f"⚠️ Warning: User {user_id} marked as 'စသတိထားရမည့်သူ'")
                
                elif label_name == 'လူလိမ်':
                    # လူလိမ်အတွက် လုပ်စေချင်တဲ့အလုပ်
                    # ဥပမာ - ဘာတုံ့ပြန်မှုမှမလုပ်တော့ဘဲ Block လုပ်ခြင်း သို့မဟုတ် Log ထားခြင်း
                    send_message(user_id, "သင့်အကောင့်အား စစ်ဆေးနေပါသည်။")
                    print(f"🚨 ALERT: User {user_id} marked as 'လူလိမ်'")
                
                elif label_name == 'မှတ်ထားရမည့်သူ':
                    # မှတ်ထားရမည့်သူအတွက် အသိပေးခြင်း
                    send_message(user_id, "ကျေးဇူးပါ။ သင့်အကြောင်းကို မှတ်သားထားပါမည်။ နောက်မှ အကြောင်းပြန်ပါမည်။")
                    print(f"📝 Info: User {user_id} marked as 'မှတ်ထားရမည့်သူ'")
                
                else:
                    continue
                        
                        
                
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
