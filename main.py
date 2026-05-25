from flask import Flask, request
import requests
import os

app = Flask(_name_)
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")

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
                    user_text = event.get("message", {}).get("text", "").strip()

                    # Handle button clicks
                    if user_text == "1.သိန်း၁သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၁သောင်းအောက်အိမ်များ\n1. 🏡ဂရံအမည်ပေါက်-လမ်းကျယ် နေရာကောင်း စီးပွါးရေးလုပ်ရန်အထူးအဆင်ပြေသောနေရာ🌷အင်းစိန်မြို့နယ်-က+ခ ရပ်ကွက်-မြို့သစ်စျေးအနီး🌷လမ်းမကြီးမှ(၈)အိမ်မြှောက်🌷ဘဏ်နီး-ကျောင်းနီ-စျေးနီး🌷2BN.20x60,8800(ညှိ့နိူင်း)🏡ကား၂စီးရှောင်လမ်း🏡မြေအမျိုးစား🏡ဂရံအမည်ပေါက်🏡အရောင်းမြေပုံကူးပေးမည်🚕ကားလိူင်းပေါင်းစုံအနီးစာရွက်စာတမ်း-ခိုင်မာပြီးအရူပ်ရှင်းကင်းသော-အိမ်-ခြံမြေ-များကိုသာအရောင်းဝယ်လုပ်ပေးပါတယ်ရှင့်\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    elif user_text == "2.သိန်း၂သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၂သောင်းအောက်အိမ်များ\n1. 20x40 အိမ် - သိန်း150\nတည်နေရာ: ရွှေပြည်သာ\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    elif user_text == "3.သိန်း၃သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၃သောင်းအောက်အိမ်များ\n1. 40x60 အိမ် - သိန်း280\nတည်နေရာ: မရမ်းကုန်း\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    elif user_text == "4.သိန်း၄သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၄သောင်းအောက်အိမ်များ\n1. 60x80 အိမ် - သိန်း350\nတည်နေရာ: ကမာရွတ်\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    elif user_text == "5.သိန်း၅သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၅သောင်းအောက်အိမ်များ\n1. လုံးချင်းအိမ် - သိန်း450\nတည်နေရာ: ကမာရွတ်\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    elif user_text == "6.သိန်း၆သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၆သောင်းအောက်အိမ်များ\n1. ကွန်ဒို - သိန်း550\nတည်နေရာ: စမ်းချောင်း\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    elif user_text == "7.သိန်း၇သောင်းအောက်အိမ်များ":
                        reply_text = "🏡 သိန်း၇သောင်းအောက်အိမ်များ\n1. လုံးချင်းအိမ် - သိန်း650\nတည်နေရာ: ကမာရွတ်\n📞 09424006004"
                        send_message(sender_id, reply_text)
                    
                    else:
                        # First message - send welcome + buttons
                        send_welcome_with_buttons(sender_id)
        
        return "ok", 200

def send_welcome_with_buttons(recipient_id):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": "👩🏻‍💼🏘️ Ma Thin Yu အိမ်ခြံမြေအကျိုးဆောင်မှာကြိုဆိုပါတယ်\nဘယ်စျေးနှုန်းအကွာအဝေးကို ကြည့်ချင်လဲ?",
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

def send_message(recipient_id, text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    requests.post(url, json=payload)


