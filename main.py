from flask import Flask, request
import requests
import os

app = Flask(__name__)
PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN","thinyurealestate")

# EDIT YOUR LISTINGS HERE
LISTINGS = {
    "PRICE_1": [
        
     {
             "title": """အမြန်ရောင်းမည် အင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး-ဘုရင့်နောင်လမ်းမကြီးဒဲ့ပေါက်,လမ်း-ကား၂စီးရှောင်လမ်း-အသင့်နေရုံ-2BN အိမ်ကောင်း
                        🌸မြေအမျိုးစား🌸ဘိုးဘွားပိုင်မြေ🌸အစက်ဆက်စာချုပ်🌸မြေကွက်အမှတ်စစ်လို့ရ
                        🌸ခြံထဲ ကားထားလို့ရ 🌸Solar ၆ချက်🌸အဲကွန်း ၅လုံး🌸CCTV ၁၂ လုံး
                        🌸Toilet အပေါ်အောက် ရေပူရေအေးပါ
                        💸ဝယ်ယူသူဘတ်မှ အကျိုးဆောင်ခကိုလုံး၀ပေးစရာမလိုပါ """,   
            "subtitle": "🌸ခြံအကျယ် 18× 80 ပေအကျယ် 🏡2 BN နှစ်ထပ်အိမ် အသင့်သင့် , 💸ရောင်းစျေး4400(ညှိ့နိူင်း)",
            "image_url": "https://i.postimg.cc/rmTRnYJK/Image-25-05-2026-at-4-44-PM-(4).png",
            "facebook_url": "https://www.facebook.com/share/p/1DaozjPCxM/" 
            
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
            "image_url": "https://i.postimg.cc/PJgjy0Wz/Image-25-05-2026-at-5-08-PM-(5).png",
            "facebook_url": "https://www.facebook.com/share/p/1duXavUZYd/" 

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
            "image_url": "https://i.postimg.cc/fymwGwT8/Image-26-05-2026-at-1-12-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1EwVh5nBds/" 

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
            "subtitle": "🌺ခြံအကျယ် ၂၅ × ၆၀ေပ , 💸၈၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/JntCLRK6/Image-25-05-2026-at-5-14-PM-(1).png",
            "facebook_url": "https://www.facebook.com/share/p/1duXavUZYd/" 
}, 
{
    "title": "ဂရံအမည်ပေါက် အိမ်နှင့်ခြံအရောင်း🌸...",
    "subtitle": "💸၄၀x၆၀ပေကျယ် 💸သိန်း ၈၅၀ (ညှိ့နိူင်းစျေး)",
    "image_url": "https://i.postimg.cc/q7z1BgVM/IMG-5193.jpg",
    "facebook_url": "https://www.facebook.com/share/p/1E1Uj9bsaT/"
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
        "image_url": "https://i.postimg.cc/RZbjLkv4/Image-26-05-2026-at-1-15-AM.png",
        "facebook_url": "https://www.facebook.com/share/p/1HdcYcGFfY/" 

        },
        { "title": "ဂရန်အမည်ပေါက် နေရာကောင်း လမ်းကျယ် ပတ်ဝန်ကျင်သန့် အိမ်နင့်ခြံ အရောင်း\n"
                    "🌸အင်းစိန်မြို့နယ် မြို့သစ် ရက်ကွက်\n"
                    "🌺ဘုရင့်နောင် ရိပ်သာ Vip လမ်းသန့်\n"
                    "🌸ဘုရင်နောင် လမ်းမကြီး အနီး\n"
                    "🌸မြို့သစ်စျေး အနီး\n"
                    "🌸ဘုရင်နောင်း စျေးကြီး 🚗 5 မီနစ်ခန့်\n"
                    "🌸စျေးနီးကျောင်းနီး မှတ်တိုင် အနီး\n"
                    "🌸ကားနှစ်စီးရှောင် လမ်းကျယ်\n"
                    "🌸လူတိုင်ကြိုက်တဲ့ အရှေ့အလှည့်\n"
                    "🌸နှစ်ထပ်ပြင်ထောင်အိမ်\n"   
                    "🌸ဂရံအမည်ပေါက် သက်ရှိထင်ရှား ရှိ\n"
                    "🌸အရောင်းမြေပူံ ကူးပေးမည်",
            "subtitle": "🌸ခြံအကျယ် ၃၀ × ၆၀ ပေ အကျယ်,💸ရောင်းစျေး ၁၄၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/L69wK9Xj/Image-26-05-2026-at-1-16-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Lu5qCkvfg/" 

            
     },
        { "title": "ကိုယ်တိုင်နေဖို့ ရှယ်ကိုလုပ်ထားတာမလို့။ဒါပေမယ့် ရောင်းရဖို့အကြောင်းပါလာတော့လဲရောင်းရတော့မယ်။ရွှေပြည်သာ Vip3 ရပ်ကွက်မှာပါ။ အမှတ် ၄လမ်းနဲ့တော်တော်နီးပါတယ်။ ခြံရှေ့လမ်းကျယ်ပါတယ်။",
         "subtitle": "➡️ခြံအကျယ်60'x90',➡️အိမ်အကျယ်35'x55'➡️ရေကူးကန်-15'x30',သိန်း ၁၈,၀၀၀",
         "image_url": "https://i.postimg.cc/3wrxk43f/Image-26-05-2026-at-1-46-AM.png",
         "facebook_url": "https://www.facebook.com/share/p/18oWZFS9zC/"
        },
    {
        "title": " နာမည်ကြီး မင်းသမီးခြံ အနီး နေရာကောင်း စိတ်ငြိမ်ရပ်ကွက် အမည်ပေါက်  ခြံအရောင်း,မရမ်းကုန်းမြို့နယ် ၅ ရပ်ကွက်,🌸၉ မိုင်\n"
                 "ဗိုလ်ညာဏ လမ်းသွယ် 🌸ပြည့်လမ်းမကြီး အနီး🌸Ocean Center အနီး🌸✈ ရန်ကုန် လေဆိပ် အနီး🌸ပတ်ဝန်ကျင်သန့် စိတ်ငြိမ်ရပ်ကွက်",
        "subtitle": "🌸ခြံအကျယ် ၃၆ × ၆၂ ပေ,💸၁၅၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
        "image_url": "https://i.postimg.cc/XY92Ypz5/Image-27-05-2026-at-2-32-AM.png",
        "facebook_url": "https://www.facebook.com/share/p/17m6ESdwqN/"
    },

    {
        "title": " မီး အမြဲမှန်တဲ့ လေဆိပ်လမ်းထဲက နေရာကောင်လမ်းကျယ် 1RC အိမ်နဲ့ခြံ  အရောင်း🍀 အင်းစိန်မြို့နယ် ၊ စောဘွားကြီးကုန်းရပ်ကွက်,🌸လေဆိပ်ရိပ်သာ လမ်းသွယ်,🌸ပြည်လမ်းမကြီး အနီး,🌸✈️ ရန်ကုန်လေဆိပ်အနီး,🌸Ocean Center အနီး,🌸ဆယ်မိုင်ကုန်းစျေး ,🌸တောင်ဘက်အလှည်,🌸ကားနှစ်စီးရှောင် လမ်း",
        "subtitle": "🌸ခြံအကျယ် ၆၀ × ၅၅ ,💸၁၅၀၀၀ သိန်း ( ညှိနှိုင်းစျေး)",
        "image_url": "https://i.postimg.cc/jdcHgPmH/Image-27-05-2026-at-2-52-AM.png",
        "facebook_url": "https://www.facebook.com/share/p/1chPdC9zSS/"
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
        "image_url": "https://i.postimg.cc/9Q4xCrj2/Image-26-05-2026-at-1-18-AM.png",
        "facebook_url": "https://www.facebook.com/share/p/1BDGbQti5V/" 

        },

        
    { "title": "မိုင် ပြည်လမ်းမ အလွန်းနီး လမ်းကျယ်နေရာကောင်း မြေသီသန့် ခြံကွက်အရောင်း,🌸မရမ်းကုန်းမြို့နယ် ၅ ရပ်ကွက်,🌸၉ မိုင် ဘောဂလမ်း,🌸ရန်ကုန်လေဆိပ် အနီး,🌸Ocean center အနီး,🌸ပြည်လမ်းမကြီး ဒဲပေါက့် အလွန်နီး,🌸ကားနှစ်စီးရှောင် လမ်းကျယ်",
           "subtitle": "🌸ခြံ အကျယ် 37 × 90  ပေ,💸ရောင်းစျေး  ၂၉၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
           "image_url": "https://i.postimg.cc/ncXFgtwS/Image-27-05-2026-at-2-57-AM.png",
           "facebook_url": "https://www.facebook.com/share/p/1DrXZbppAw/"
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
            "image_url": "https://i.postimg.cc/FRGbj449/703503390-1602069564214217-7649272277303429298-n.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18czyUKQ2V/" 
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
                        
                            sender_id = event["sender"]["id"]
                            if "referral" in event:
                            if "message" in event:

                    send_message(sender_id, "Thanks for coming from our ad!")
              
                # 2. message_reactions
               if "reaction" in event:
        reaction = event["reaction"].get("reaction", "")
        
        if reaction == "love":
            url = f"https://graph.facebook.com/v18.0/{sender_id}/labels?access_token={PAGE_ACCESS_TOKEN}"
            requests.post(url, json={"name": "Hot Lead"})
        
        send_message(sender_id, f"You reacted with {reaction}")

                if "read" in event:
                 print(f"User {sender_id} read the message")
                
                payload = event.get("message", {}).get("quick_reply", {}).get("payload", "")

               text = event.get("message", {}).get("text", "")
                
                message_data = payload if payload else text

                    if message_data in LISTINGS:
                        send_listings_carousel(sender_id, message_data)
                    else:
                        send_welcome_with_buttons(sender_id)
        
        return "OK", 200

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
        send_price_quick_replies(recipient_id)
        return

    elements = []
    for item in listings:
        elements.append({
            "title": item["title"],
            "subtitle": item["subtitle"],
            "image_url": item["image_url"],
            "buttons": [
                {
                    "type": "web_url",
                    "url": item["facebook_url"],
                    "title": "ပြည်စုံကြည့်ရန်လင့်"
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

    send_message(recipient_id, "👉 နောက်ထပ် စျေးနှုန်းတွေကိုလည်း အောက်မှာဆွဲ၍ နှိပ်ကြည့်နိုင်ပါတယ်:")
    send_price_quick_replies(recipient_id)


def send_price_quick_replies(recipient_id):
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
    requests.post(url, json=payload)

    # ADD THESE 2 LINES AT THE END:
    send_message(recipient_id, "👉 နောက်ထပ် စျေးနှုန်းတွေကိုလည်း အောက်မှာဆွဲ၍ နှိပ်ကြည့်နိုင်ပါတယ်:")
    send_price_quick_replies(recipient_id)
def send_price_quick_replies(recipient_id):
    # Map your payloads to readable titles
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
        if len(items) > 0:  # only show prices that have listings
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
def send_message(recipient_id, text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    requests.post(url, json=payload)
