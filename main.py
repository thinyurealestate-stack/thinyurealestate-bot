from flask import Flask, request
import requests
import os

app = Flask(__name__)
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")

# EDIT YOUR LISTINGS HERE
LISTINGS = {
    "PRICE_1": [
        
        {
            "title": """🏡ဂရံအမည်ပေါက်-လမ်းကျယ် နေရာကောင်း စီးပွါးရေးလုပ်ရန်အထူးအဆင်ပြေသောနေရာ🌷အင်းစိန်မြို့နယ်-က+ခ ရပ်ကွက်-မြို့သစ်စျေးအနီး🌷လမ်းမကြီးမှ(၈)အိမ်မြှောက်🌷ဘဏ်နီး-ကျောင်းနီ-စျေးနီး """,
            "subtitle": "🌷2BN.20x60,8800(ညှိ့နိူင်း)",
            "image_url": "https://drive.google.com/uc?export=view&id=1eSvjYhgjN0nOb0Yw5phphnoHv6esYqMe"
        },
            {
             "title": """အမြန်ရောင်းမည် အင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး-ဘုရင့်နောင်လမ်းမကြီးဒဲ့ပေါက်,လမ်း-ကား၂စီးရှောင်လမ်း-အသင့်နေရုံ-2BN အိမ်ကောင်း
                        🌸မြေအမျိုးစား🌸ဘိုးဘွားပိုင်မြေ🌸အစက်ဆက်စာချုပ်🌸မြေကွက်အမှတ်စစ်လို့ရ
                        🌸ခြံထဲ ကားထားလို့ရ 🌸Solar ၆ချက်🌸အဲကွန်း ၅လုံး🌸CCTV ၁၂ လုံး
                        🌸Toilet အပေါ်အောက် ရေပူရေအေးပါ
                        💸ဝယ်ယူသူဘတ်မှ အကျိုးဆောင်ခကိုလုံး၀ပေးစရာမလိုပါ """,   
            "subtitle": "🌸ခြံအကျယ် 18× 80 ပေအကျယ် 🏡2 BN နှစ်ထပ်အိမ် အသင့်သင့် , 💸ရောင်းစျေး4400(ညှိ့နိူင်း)",
            "image_url": "https://drive.google.com/uc?export=view&id=138Y0sAC0twMImPgBvYfoaVCZLgYC9KWr" 
        },
            {
            "title": """ကျောက်ရေတွင်း လမ်းမဒဲ့ပေါက် လမ်းကျယ် မိန်လမ်းမပေါ် နေရာကောင်း အိမ်နှင်ခြံ အရောင်း
                        🌺မရမ်းကုန်း မြို့နယ်  ၅ရပ်ကွက်
                        🌸သဗ္ဗညုပုထိုးတော်ကြီး အနီး
                        🌺စွယ်တော်မြတ် စေတီတော် အနီး
                        🌸ကျောက်ရေတွင်း လမ်းမ ဒဲ့ပေါက်
                        🌺ရန်ကုန် လေဆိပ် အနီး
                        🌸ကားနှစ်စီးရှောင် မိန်လမ်မပေါ်
                        🌸ခြံအကျယ် ၃၀ × ၈၀ ပေ
                        🌺1RC တစ်ထပ်တိုက် အိမ်ကောင်း
                        🌸လူတိုင်ကြိုက်တဲ့ အရှေ့အလှည့်
                        🌺ခြံထဲ ကားနှစ်စီးခန့် ထားလို့ရ
                        🌸မာစတာ (2) ခန်း ထပ်ခိုးပါ
                        🌺ရေကူးကန် ငယ်တစ်ခုပါ
                        🌸ကားဂိုထောင် (1) ထပ်ခိုးပါ
                        🌸ဘိုးဘွားပိုင် အရပ်စာချုပ်
                        🌺ဂရန်ပြန်လျောက်လို့ရသော မြေ""",
            "subtitle": " 💸၈၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://drive.google.com/uc?export=view&id=1rgLIGefRfvNGg-pU28d6NCnh6-wZKP8w"
        },
            {
            "title": """🏡ရပ်ကွက်သန့် လမ်းကျယ် နေရာကောင်းမှာ 1RC တိုက်လေးပါမယ် အိမ်နှင့်ခြံ အရောင်း
                        🌸မရမ်းကုန်း မြို့နယ်  ၅ရပ်ကွက်
                        🌸သဗ္ဗညုပုထိုးတော်ကြီး အနီး
                        🌸စွယ်တော်မြတ် စေတီတော် အနီး
                        🌸ကျောက်ရေတွင်း လမ်းမ အနီး
                        🌸ရန်ကုန် လေဆိပ် အနီး
                        🌸ကားနှစ်စီးရှောင် လမ်းကျယ်
                        🌸ခြံအကျယ် ၄၀ × ၆၀ ပေ
                        🌸1RC တစ်ထပ်တိုက် အိမ်ကောင်း
                        🌸ခြံထဲ ကားနှစ်စီးခန့် ထားလို့ရ
                        🌸Master Bedrooms (3) ခန်း
                        🌸ပြင်ဆင်ပြီး အသင့်နေလို့ရ
                        🌸ဘိုးဘွားပိုင် အရပ်စာချုပ်
                        🌸ဂရန်ပြန်လျောက်လို့ရသော မြေ """,
            "subtitle", "💸၇၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url", "https://drive.google.com/uc?export=view&id=1rgLIGefRfvNGg-pU28d6NCnh6-wZKP8w"
        },
            {
            "title": """ရှယ်ပြင်ဆင်ပြီးအသင့်နေအိမ်ရောင်းမည်
                        🌷အင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး
                        🌷လမ်းမကြီးမှကားနဲ့ ၁မီးနှစ်သာဝင်ရ
                        🌷ဘဏ်နီး-ကျောင်းနီ-စျေးနီး
                        🌷ခြံကျယ်၂၅x၆၀/၆၅၀၀
                        🌷2 5,BN. အမိုးစလပ်ကိုယ်တိုင်နေဖို့ဆောက်ထားသောအိမ် ဖြစ်လို့အရမ်တန်သောလေး
                        🌷အောက်ထပ်-ဧည့်ခန်း (1)ခန်း
                        🌸Master bed room-(1)ခန်း
                        🌸မီးဖိုခန်းကျယ်။(၁)ခန်း
                        🌸ရေချိုးခန်းကျယ်(၁)ခန်း
                        🌸ဘိုထိုင် (၁)
                        🌸ဗားတပ်(၁)
                        အခန်းကျင်း(၁)
                        🌸အပေါ်ထပ်-ဧည့်ခန်း(၁)ခန်း
                        🌸မာစတာခန်း (၂)ခန်း
                        🌸စင်ဂယ်။(၂)ခန်း
                        🌸ရေချိုးခန်း။(၂)ခန်း
                        🌸ဘိုထိုင်(၂)
                        🌸အပေါ်ဗားတပ်။(၁)
                        အပေါ်စလပ်မိုးဖြစ်လို့လေကောင်းလေသန့်ရတဲ့ပြင်-အပင်စိုက်လို့လည်းရပါတယ်ရှင့်
                        မြေကွက် ၁ကွက်အပိုရသလိုပါပဲရှင့်
                        🏡အပေါ်စလပ်မှာ ဘိုထိုင်ပါသေးတယ်နော်
                        🏡ကား၂စီးရှောင်လမ်း
                        🏡မြေအမျိုးစား
                        🏡ဘိုးဘွားပိုင်-အစက်ဆက်စာချုပ်
                        🏡အရူပ်ရှင်းကင်း
                        မြေကွက်အမှတ်စစ်လို့ရ
                        စာရွက်စာတမ်း-ခိုင်မာပြီး
                        အရူပ်ရှင်းကင်းသော-အိမ်-ခြံ
                        မြေ-များကိုသာအရောင်းဝယ်
                        လုပ်ပေးပါတယ်ရှင့်
                        💁‍♂️လူကြီးမင်းစိတ်ဝင်စားလျင်
                        လူကိုယ်တိုင်လာကြည့်ဖို့ဖိတ်ခေါ်ပါရစေရှင့်🙏
                        💸💸ဝယ်ယူသူဖက်မှအကျိုးဆောင်ခ(လုံးဝ)ပေးးန်မ
                        လိုပါရှင့်🙏
                        👉စာရွက်စာတမ်းခိုင်မာပြီးအရူပ်ရှင်းကင်းသော-အိမ်ခြံမြေများကိုသာ-အရောင်းဝယ်လုပ်ပေးပါတယ်ရှင့်💁‍♂️""",
            "subtitle": "💸2.5.RC 25.60,6500(ညှိ့နိူင်း)",
            "image_url": "https://drive.google.com/uc?export=view&id=1IQuSP5CuuxbNBs0PIIGKKIxvadrQSWcM"
        },
            {
            "title": """🏠 ကျောက်ရေတွင်း လမ်းမဒဲ့ပေါက် လမ်းကျယ်မိန်လမ်းမပေါ် နေရာကောင်း အိမ်နှင်ခြံ အရောင်း
                        🌸မရမ်းကုန်း မြို့နယ်  ၅ရပ်ကွက်
                        🌸သဗ္ဗညုပုထိုးတော်ကြီး အနီး
                        🌸စွယ်တော်မြတ် စေတီတော် အနီး
                        🌸ကျောက်ရေတွင်း လမ်းမ ဒဲ့ပေါက်
                        🌸ရန်ကုန် လေဆိပ် အနီး
                        🌸ကားနှစ်စီးရှောင် မိန်းလမ်မပေါ်
                        🌸အိမ်ကနေ လမ်းမကြီးမြင်နေရ
                        🌺2BN နှစ်ထပ်တိုက် အိမ်ကောင်း
                        🌺အနောက်ဘက်အလှည့် ထောင့်ကွက် 
                        🌺ခြံထဲ ကားထားလို့ရ
                        🌸ဘိုးဘွားပိုင်  အဆက်စပ် စာချုပ်
                        💸ဝယ်ယူသူဘတ်မှ အကျိုးဆောင်ခကို
                        လုံး၀ပေးစရာမလိုပါ""",
            "subtitle": "🌺ခြံအကျယ် ၂၅ × ၆၀ေပ , 💸၅၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://drive.google.com/uc?export=view&id=1yFTHdvpczHgU1xfZnqe4pHlfFyTjw26e"
        }
            ],
    "PRICE_2": [
    {    "title": """၉မိုင် ပြည်လမ်းမဒဲ့ပေါက် နေရာကောင်းလမ်းမ အနီး အိမ်နှင့်ခြံ ရောင်းမည်။
                    🌸 မရမ်းကုန်မြို့နယ် ၉မိုင် ၅ ရက်ကွက်
                    🌸ပြည်လမ်း ဒဲ့ပေါက်
                    🌸Ocean center အနီး
                    🌸✈ ရန်ကုန်လေဆိပ် အနီး
                    🌸ကားနှစ်စီးရှောင် လမ်း
                    🌸မြောက်ဘက်အလှည့် 
                    🌸2BN နှစ်ထပ်တိုက် အသင့်သင့်
                    🌸ခြံထဲ 🚕သုံးစီး ထားလို့ရ
                    🌸မြေပိုင်မြေ အမျိုးအစား
                    🌸အမည်ပေါက် လျောက်ထားဆဲ ပါ
                    🌺ဝယ်ယူသူဘတ်မှ အကျိုးဆောင်ခကိုလုံး၀ပေးစရာမလိုပါ""",
        "subtitle": "🌸ခြံ  အကျယ်  ၄၀ × ၈၀ ပေ,💸သိန်း ၁၁၀၀၀ သိန်း (ညှီနှိုင်စျေး)",
        "image_url": "https://drive.google.com/uc?export=view&id=1DT0vy8jJ23YBdfcpdiMgEvof6_K0I4X5"
        },
        { "title": """ ဂရန်အမည်ပေါက် နေရာကောင်း လမ်းကျယ် ပတ်ဝန်ကျင်သန့် အိမ်နင့်ခြံ အရောင်း
                    🌸အင်းစိန်မြို့နယ် မြို့သစ် ရက်ကွက်
                    🌺ဘုရင့်နောင် ရိပ်သာ Vip လမ်းသန့်
                    🌸ဘုရင်နောင် လမ်းမကြီး အနီး
                    🌸မြို့သစ်စျေး အနီး
                    🌸ဘုရင်နောင်း စျေးကြီး 🚗 5 မီနစ်ခန့်
                    🌸စျေးနီးကျောင်းနီး မှတ်တိုင် အနီး
                    🌸ကားနှစ်စီးရှောင် လမ်းကျယ်
                    🌸လူတိုင်ကြိုက်တဲ့ အရှေ့အလှည့်
                    🌸နှစ်ထပ်ပြင်ထောင်အိမ်   
                    🌸ဂရံအမည်ပေါက် သက်ရှိထင်ရှား ရှိ
                    🌸အရောင်းမြေပူံ ကူးပေးမည်
                    💸ဝယ်ယူသူဘတ်မှ အကျိုးဆောင်ခကို
                    လုံး၀ပေးစရာမလိုပါ""",
            "subtitle": "🌸ခြံအကျယ် ၃၀ × ၆၀ ပေ အကျယ်,💸ရောင်းစျေး ၁၄၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://drive.google.com/uc?export=view&id=1jA2an67VfIJe_1lCJUYv2l6NcE5gWCQp"
            
        }
            ],
        
    "PRICE_3": 
    [
        { "title": """မီးအမြဲလာတဲ့_လေဆိပ်ရိပ်သာလမ်းမပေါ်_နေရာကောင်း_အိမ်နှင့်ခြံအရောင်း
                📍 အင်းစိန်မြို့နယ် ၊ စောဘွားကြီးကုန်းရပ်ကွက်
                📍 လေဆိပ်ရိပ်သာလမ်းမပေါ်
                📍လေဆိပ်လမ်းမကြီးရဲ ၃ ခြံ မြောက်
                ✈️ ရန်ကုန်လေဆိပ်အနီး
                🛍 Ocean Center ၊ ဆယ်မိုင်ကုန်းစျေး ၊ ပြည်လမ်းမကြီး အနီး
                ✨ VIP နေရာကောင်း ၊ ပတ်ဝန်းကျင်သန့်
                ✨ 24hr မီးမပြတ်သော ရပ်ကွက်
                ✨ 2RC နှစ်ထပ်တိုက် အိမ်ကောင်းအိမ်သန့်
                ✨ ခြံထဲ ကား ၅ စီးခန့် ရပ်နားနိုင်
                ✨ ဘိုးဘပိုင်မြေ  အဆက်အစပ်စာချုပ်
                ✨ အကွက်အမှတ် စစ်ဆေးနိုင်
                ✨ အထူးဂရန် လျှောက်ထားနိုင်သော မြေ
                💸ဝယ်ယူသူဘတ်မှ အကျိုးဆောင်ခကို""",
        "subtitle": "✨ ခြံအကျယ် 70 × 100 ( 7000 Sqft),💵 ၂၂၀၀၀ သိန်း (ပိုင်ရှင်တိုက်ရိုက် ညှိနှိုင်း)",
        "image_url": "https://drive.google.com/uc?export=view&id=16qZuOJExsMMd_tojtSf6A1RtDswImatS"
        }
            ],
            
    "PRICE_4": [
    {
            "title": """👉 ရင်းနှီးမြှုပ်နှံမလား ၊ ကိုယ်တိုင်နေမလား ၊ ကုမ္ပဏီရုံးခန်းလား ၊ ဝင်ငွေကောင်းတဲ့ Inn ဖွင့်မလား အားလုံးအဆင်ပြေတာမို့ ဝယ်ယူဖို့ အကြံပြုပါရစေ
                        🌺မရမ်းကုန်မြို့နယ် ၉ မိုင်
                        🌸ပြည်လမ်း ဒဲ့ပေါက်
                        🌺Ocean center အနီး
                        🌸✈ ရန်ကုန်လေဆိပ် အနီး
                        🌺ကားနှစ်စီးရှောင် လမ်းကျယ် နေရာကောင်း
                        🌺2RC နှစ်ထပ်တိုက် 
                        🌸Master Bedrooms (11) ခန်း
                        🌺လူကြီး  ရေကူးကန် ပါ
                        🌸မြေပိုင်မြေအမည်ပေါက် """,
                        
            "subtitle": "🌸ခြံအကျယ် ၅၅×၁၀၀ ပေ,💵 သိန်း ၄၀၀၀၀ သိန်း (ညှီနှိုင်စျေး)",
            "image_url: "https://drive.google.com/uc?export=view&id=1NNfe_UItc9RTv0wTMJ2sixZVp-_Hbwp0"
            }
     ],
    "PRICE_5": [],
    "PRICE_6": [],
    "PRICE_7": [],
    "PRICE_8": [],
    "PRICE_9": [],
    "PRICE_10": []
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
            "text": "👩🏻‍💼🏘️🏡🏘️👩🏻‍💼 Ma Thin Yu အိမ်ခြံမြေအကျိုးဆောင်မှာကြိုဆိုပါတယ် 📞 Contact :09424006004 📞 💜 Viber : 09767975004 💜 💙 Facebook : သင်းယု အိမ်ခြံမြေအကျိုးဆောင် 💙 🤍အိမ်ကြည့်မယ်ဆို 3နာရီကြိုဆက်ပေးပါ🤍\n\nနှစ်သက်ရာစျေးနှုန်းလေးများကိုအောက်ကဈေးနှုန်းဘားအတိုင်းနိတ်ပြီးဆွဲကြည့်လိုရပါတယ်နော်",
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
