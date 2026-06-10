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
            "title": "အင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး",
            "subtitle": "8×80 ပေ, 2BN နှစ်ထပ်အိမ်, 4400 သိန်း",
            "image_url": "https://i.postimg.cc/rmTRnYJK/Image-25-05-2026-at-4-44-PM-(4).png",
            "facebook_url": "https://www.facebook.com/share/p/1DaozjPCxM/"
        },
        {
            "title": " လမ်းသစ်လမ်းမကြီး အနီး,နံသာမြိုင်လမ်း,Pro (1) global home အနီး",
            "subtitle": "ကားနှစ်စီးကပ်ရှောင်,လမ်းကျယ်ခြံ အကျယ် 1770 Sqft,၂၆၅၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/1Rvnn33Y/IMG-5293.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1CdefBLAM3/"
        },
        {
            "title": "ဆယ်မိုင်စျေးအနီး ရန်ကြီးအောင်းလမ်း,ဘိုးဘပိုင်မြေ,အင်းစိန်မြို့နယ်",
            "subtitle": "ကား၂စီးရှောင်လမ်း,၃၀x၆၀.၅၅၀၀(ပါးပါးရှော့)",
            "image_url": "https://i.postimg.cc/RCW6tzJ7/IMG-5263.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Kz23aMk3C/"
        },
        {
            "title": "Spring Line Hotel ကပ်လျက်,🏡ဘိုးဘပိုင်မြေ",
            "subtitle": "27x78.3000-သိန်း(ညှို့နိူင်း)",
            "image_url": "https://i.postimg.cc/nzkkQfXv/IMG-5253.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Fc4LMhbM9/"
        },
        {
            "title": "မှော်ဘီမြို့နယ်-မင်္ဂလာကုန်းရွာ,တခါတလေအပန်းဖြေသွားမလား ဝယ်ဥထားရင်လည်းအမြတ်ရမှာနော်",
            "subtitle": "ခြံကျယ် ၁ ဧကခွဲ,သိန်း၃၀၀၀(ပါးပါးရှော့),မြေ အမျိုးစား-G -မြေ",
            "image_url": "https://i.postimg.cc/d3g4Jm7H/post-558794-featured.jpg",
            "facebook_url": "https://www.facebook.com/share/r/17SwGtwbix/"
        },
        {
            "title": "မှင်းနန်ဒါလမ်းမကြီး ဒဲ့ဆင်း ၂လမ်းမြှောက်,စျေးနီး ကျောင်းနီး ဘဏ်နီး မှတ်တိုင်အနီး capitalနီး",
            "subtitle": "၁၂ပေ ခွဲ ပေ၅၀,၁၀၉၀ပါးပါးညှိနှိုင်း",
            "image_url": "https://i.postimg.cc/Mp6dqTXy/IMG-5244.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1JNAaEHcEz/"
        },
        {
            "title": "သာကေတမြို့နယ်,အောင်သပြေ အနောက်( -)လမ်း,ဂရံအမည်ပေါက် အိမ်နှင့်ခြံအရောင်း",
            "subtitle": "ပေကျယ် ၄၀”၆၀,သိန်း ၈၅၀၀ (ညှိ့နိူင်းစျေး)",
            "image_url": "https://i.postimg.cc/HsXkdYRv/IMG-5193.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1BG5exRsdz/"
        },
        {
            "title": "ကျောက်ရေတွင်း လမ်းမဒဲ့ပေါက် လမ်းကျယ်,မရမ်းကုန်း မြို့နယ်  ၅ရပ်ကွက်,စွယ်တော်မြတ် စေတီတော် အနီး",
            "subtitle": "ရေကူးကန် ငယ်တစ်ခုပါ,ဘိုးဘွားပိုင် အရပ်စာချုပ်,၈၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/zB4H2dHT/Image-25-05-2026-at-5-08-PM-(5).png",
            "facebook_url": "https://www.facebook.com/share/p/1EmM7sSUsU/"
        },
        {
            "title": "ကအင်းစိန်မြို့နယ်-အောင်ဆန်းစျေးအနီး,ဘဏ်နီး-ကျောင်းနီ-စျေးနီး",
            "subtitle": "လမ်းမကြီးမှကားနဲ့ ၁မီးနှစ်သာဝင်ရ,ခြံကျယ်၂၅x၆၀ 6500 ညှိ့နိူင်း",
            "image_url": "https://i.postimg.cc/4dpXZwFh/Image-26-05-2026-at-1-12-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/18oLWtVcv6/"
        },
        {
            "title": "မရမ်းကုန်း မြို့နယ် ၅ရပ်ကွက်,ရန်ကုန် လေဆိပ် အနီး,သဗ္ဗညုပုထိုးတော်ကြီး အနီး",
            "subtitle": "ဂရန်ပြန်လျောက်လို့ရသော မြေ,ခြံအကျယ် ၄၀ × ၆၀ ပေ,၇၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/dtLSyDwn/Image-25-05-2026-at-5-14-PM-(1).png",
            "facebook_url": "https://www.facebook.com/share/p/18fMXD47JE/"
        },
        {
            "title": "ကျောက်ရေတွင်း လမ်းမဒဲ့ပေါက်,မရမ်းကုန်း မြို့နယ်  ၅ရပ်ကွက်,ဘိုးဘွားပိုင်  အဆက်စပ် စာချုပ်",
            "subtitle": "ခြံအကျယ် ၂၅ × ၆၀ ပေ,၅၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/0Ntzb7Dn/Image-28-05-2026-at-11-44-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1CRS21Zhin/"
        },
         {
            "title": "အင်းစိန်မြို့နယ်၊ မြို့သစ် ခဘက်ခြမ်း,ပိန္နဲကုန်းရပ်ကွက်",
            "subtitle": "ကားဝင်လို့ရ လမ်းသွယ်လမ်းပိတ်မဟုတ်ပါ,၁၉၅၀ နဲ့တန်တန်လေးရောင်းမည်",
            "image_url": "https://i.postimg.cc/hPPTP4HC/IMG-5363.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18igS589wC/"
        }
        
    ],
    "PRICE_2": [
        {
            "title": "မရမ်းကုန်မြို့နယ် ၉မိုင် ၅ ရက်ကွက်,ပြည်လမ်းမဒဲ့ပေါက်,ရန်ကုန်လေဆိပ် အနီး,ကားနှစ်စီးရှောင် လမ်း",
            "subtitle": "40×80 ပေ, 11000 သိန်း",
            "image_url": "https://i.postimg.cc/RZbjLkv4/Image-26-05-2026-at-1-15-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1HdcYcGFfY/"
        },
        {
            "title": "မရမ်းကုန်းမြို့နယ်၊ ကျိုက်ဝိုင်းအနီး,ဘိုးဘွားပိုင်မြေ (စာရွက်စာတမ်းအပြည့်အစုံ)BCC ကျပြီးသား",
            "subtitle": "၃ ထပ်ခွဲ ရုံး စီးပွားရေးအသင့်သုံး အဆောက်အဦး 33’ x 55’,သိန်း 18,000 ညှိနှိုင်း",
            "image_url": "https://i.postimg.cc/ZKZmS8mt/IMG-5255.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Xq4U7jYGz/"
        },
        {
            "title": "နာမည်ကြီး မင်းသမီးခြံ အနီး,မရမ်းကုန်းမြို့နယ် ၅ ရပ်ကွက်,၉ မိုင် ဗိုလ်ညာဏ လမ်းသွယ် ",
            "subtitle": "စိတ်ငြိမ်ရပ်ကွက် အမည်ပေါက်,ခြံအကျယ် ၃၆ × ၆၂ ပေ,၁၅၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/XJH5bjZs/Image-27-05-2026-at-2-32-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BRai2EH5x/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် မြို့သစ် ရက်ကွက်,ဘုရင့်နောင် ရိပ်သာ Vip လမ်း",
            "subtitle": "လူတိုင်ကြိုက်တဲ့ အရှေ့အလှည့်,ခြံအကျယ် ၃၀ × ၆၀ ပေ အကျယ်,၁၄၀၀၀သိန်းညှီနှိုင်းစျေး",
            "image_url": "https://i.postimg.cc/rwjxJNV2/Image-26-05-2026-at-1-16-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BeZ8m2wyd/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် ၊ စောဘွားကြီးကုန်းရပ်ကွက်,လေဆိပ်ရိပ်သာ လမ်းသွယ်,Ocean Center အနီး",
            "subtitle": "တောင်ဘက်အလှည်,ကားနှစ်စီးရှောင် လမ်း,ခြံအကျယ် ၆၀ × ၅၅,၁၅၀၀၀ သိန်း ညှိနှိုင်းစျေး",
            "image_url": "https://i.postimg.cc/RhPqtX1s/Image-27-05-2026-at-2-52-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Hi635363E/"
        },
        {
            "title": "ရွှေပြည်သာ Vip3 ရပ်ကွက်,အမှတ် ၄လမ်းနဲ့တော်တော်နီး,စာရွက်စာတန်း အရှုပ်အရှင်း",
            "subtitle": "အိမ်အကျယ် - 35' x 55',ခြံအကျယ် 60' x 90',ရေကူးကန် - 15' x 30',သိန်း ၁၈,၀၀၀",
            "image_url": "https://i.postimg.cc/3JXYzLDM/Image-26-05-2026-at-1-46-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/14eeZywwfZo/"
        },
         {
            "title": "ပြည်လမ်းမကြိး အနီး,မရမ်းကုန်းမြို့နယ် ၅ရပ်ကွက်,အဆက်ဆက် စာချုပ်",
            "subtitle": "ခြံအကျယ် ၃၅ × ၅၅ ပေ,၁၆၅၀၀ သိန်းညှီနှိုင်း",
            "image_url": "https://i.postimg.cc/q7LGYdpg/Image-29-05-2026-at-12-14-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1KQgHPSarU/"
        },
        {
            "title": "🏡အင်းစိန်မြို့နယ်-မင်းဓ္မလမ်းမကြီးအနီး,အောင်သိဒ္ဓိVilla-နီး ဝိတိုရိယဆေးရုံအနီး",
            "subtitle": "မြှောက်အလှည့်,ပေကျယ်-၃၀x၁၂၀, သိန်း ၂သောင်း",
            "image_url": "https://i.postimg.cc/664FbwHk/IMG-5364.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18vbwdBjVv/"
        }
    ],
    "PRICE_3": [
        {
            "title": "လေဆိပ်ရိပ်သာလမ်းမ",
            "subtitle": "70×100 ပေ, 22000 သိန်း",
            "image_url": "https://i.postimg.cc/9Q4xCrj2/Image-26-05-2026-at-1-18-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BDGbQti5V/"
        },
        {
            "title": "၉မိုင် ပြည်လမ်းမ အလွန်းနီး လမ်းကျယ်,၉ မိုင် ဘောဂလမ်း,Ocean center အနီး",
            "subtitle": "ခြံ အကျယ် 37 × 90  ပေ,၂၉၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/9QkTKF7B/IMG-5198.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1DCfLUWDbn/"
        }
    ],
    "PRICE_4": [
        {
            "title": "မရမ်းကုန်းမြို့နယ် ၅ ရပ်ကွက်,၉မိုင် ရွှေ နှင်းဆီ မင်္ဂလာကန် အနီး",
            "subtitle": "ပြည်လမ်းမကြီး အနီး,ခြံအကျယ် ၅၀ × ၇၀ ပေ အကျယ်,၃၅၀၀၀ သိန်း (ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/c4Y9Vg9M/IMG-5355.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1EDpBUShAA/"
        },
        {
            "title": "၇မိုင် ကုန်းမြင့်သာ,မရမ်းကုန်းမြို့နယ်,မင်းဓမ္မလမ်းမကြီး ပြည်လမ်းမ အနီး",
            "subtitle": "ခြံအကျယ် ၅၀ × ၅၀ ပေ,လေးထောင့်ကျထောင့်ကွက်,၃၈၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/HxDjvNVS/IMG-5353.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Ppiv2a38n/"
        },
        {
            "title": "၉မိုင် ပြည်လမ်းမဒဲ့ပေါက်,Ocean center အနီး,ကားနှစ်စီးရှောင် လမ်းကျယ် ",
            "subtitle": "ခြံအကျယ် ၅၅×၁၀၀ ပေ,လူကြီးရေကူးကန်,သိန်း ၄၀၀၀၀ သိန်း (ညှီနှိုင်စျေး)",
            "image_url": "https://i.postimg.cc/s2FP1ggn/IMG-5121.jpg",
            "facebook_url": "https://www.facebook.com/share/p/17XtJz4td8/"
        }
    ],
    "PRICE_5": [],
    "PRICE_6": [],
    "PRICE_7": [],
    "PRICE_8": [],
    "PRICE_9": [
        {
            "title": "ရှစ်မိုင် ကျောက်ဝိုင်းဘုရားလမ်မကြီး,မရမ်းကုန်းမြို့နယ် ၄ ရပ်ကွက်",
            "subtitle": "၇ ပေကျယ် နှစ်ဦးသုံး ကိုယ်ပိုင်လမ်း,၇၅၀၀၀ သိန်း (ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/NjgzNbct/IMG-5296.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1GeYDV6592/"
        }
    ],
    "PRICE_10": [],
    "PRICE_11": [
        {
            "title": " Luxury Residence ဘုရင့်နောင်တံတားအောက်၊ မင်္ဂလာသန်းမြင့်ဘေးလမ်း",
            "subtitle": "ခမရမ်းကုန်းမြို့နယ်ရှိ အဆင့်မြင့် လူနေမှုပုံစံ,သိန်းကြီး 120000(ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/W46PjY5h/IMG-5346.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1EEaxo7r77/"
        }
    ]
}

# ========== SEND MESSAGE FUNCTION (WITH DETAILED ERROR LOGGING) ==========

def send_message(recipient_id, text):
    """Send a simple text message with detailed error logging"""
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {"recipient": {"id": recipient_id}, "message": {"text": text}}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Message sent to {recipient_id}")
        else:
            print(f"❌ ERROR {response.status_code}: {response.text}")
        return response
    except Exception as e:
        print(f"❌ Exception: {e}")
        return None

# ========== PRICE QUICK REPLIES ==========

def send_price_quick_replies(recipient_id):
    """Send price range quick replies"""
    label_map = {
        "PRICE_1": "1.သိန်း၁သောင်းအောက်",
        "PRICE_2": "2.သိန်း၂သောင်းအောက်",
        "PRICE_3": "3.သိန်း၃သောင်းအောက်",
        "PRICE_4": "4.သိန်း၄သောင်းအောက်",
        "PRICE_5": "5.အငှားအိမ်များ",
        "PRICE_6": "6.သိန်း၅သောင်းအောက်",
        "PRICE_7": "7.သိန်း၆သောင်းအောက်",
        "PRICE_8": "8.သိန်း၇သောင်းအောက်",
        "PRICE_9": "9.သိန်း၈သောင်းအောက်",
        "PRICE_10": "10.သိန်း၉သောင်းအောက်",
        "PRICE_11": "11.သိန်းကြီးတန်အိမ်များ"
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

# ========== WELCOME WITH BUTTONS ==========

def some_function_name():
    pass

def setup_get_started():
    url = f"https://graph.facebook.com/v18.0/me/messenger_profile?access_token={PAGE_ACCESS_TOKEN}"
    payload = {"get_started": {"payload": "GET_STARTED"}}
    try:
        response = requests.post(url, json=payload)
        print(f"Get Started: {response.status_code}")
        if response.status_code != 200:
            print(f"Error: {response.text}")
        return response
    except Exception as e:
        print(f"Error setting up Get Started: {e}")
        return None

setup_get_started()

payload = {
    "recipient": {"id": recipient_id},
    "message": {
        "text": "...",
        "quick_replies": [
            {"content_type": "text", "title": "1....", "payload": "PRICE_1"},
            {"content_type": "text", "title": "2....", "payload": "PRICE_2"},
            # ... rest of your items
        ]
    }
}
try:
    response = requests.post(url, json=payload)
    print(f"Sent welcome: {response.status_code}")
    return response
except Exception as e:
    print(f"Error sending welcome: {e}")
        return None

setup_get_started()
    payload = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": "မင်္ဂလာပါ👩🏻‍💼🏘️🏡\nမသင်းယုအိမ်ခြံမြေအကျိုးဆောင်မှ ကြိုဆိုပါတယ်\n\n💜 Viber : 09767975004 💜\n\n📞 Contact :09424006004 📞\n\n🤍အိမ်ကြည့်မယ်ဆို 3နာရီကြိုဆက်ပေးပါ🤍\n\n🏡အိမ်များကိုကျပ်သိန်း၁ထောင်မှစ အောက်ကစျေးနှုန်းအတိုင်းဆွဲ၍ \nကြည့်ရူနိုင်ပါတယ်🏡\n\n",
            "quick_replies": [
                {"content_type": "text", "title": "1.သိန်း၁သောင်းအောက်", "payload": "PRICE_1"},
                {"content_type": "text", "title": "2.သိန်း၂သောင်းအောက်", "payload": "PRICE_2"},
                {"content_type": "text", "title": "3.သိန်း၃သောင်းအောက်", "payload": "PRICE_3"},
                {"content_type": "text", "title": "4.သိန်း၄သောင်းအောက်", "payload": "PRICE_4"},
                {"content_type": "text", "title": "5.အငှားအိမ်များ", "payload": "PRICE_5"},
                {"content_type": "text", "title": "6.သိန်း၅သောင်းအောက်", "payload": "PRICE_6"},
                {"content_type": "text", "title": "7.သိန်း၆သောင်းအောက်", "payload": "PRICE_7"},
                {"content_type": "text", "title": "8.သိန်း၇သောင်းအောက်", "payload": "PRICE_8"},
                {"content_type": "text", "title": "9.သိန်း၈သောင်းအောက်", "payload": "PRICE_9"},
                {"content_type": "text", "title": "10.သိန်း၉သောင်းအောက်", "payload": "PRICE_10"},
                {"content_type": "text", "title": "11.သိန်းကြီးတန်အိမ်များ", "payload": "PRICE_11"}
            ]
        }
    }
    try:
        response = requests.post(url, json=payload)
        print(f"Sent welcome: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error sending welcome: {e}")
        return None

# ========== LISTINGS CAROUSEL ==========

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
        send_message(recipient_id, "👉 နောက်ထပ် စျေးနှုန်းတွေကိုလည်း အောက်မှာဆွဲ၍ နှိပ်ကြည့်နိုင်ပါတယ်:")
        send_price_quick_replies(recipient_id)
    except Exception as e:
        print(f"Error sending carousel: {e}")

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
                
                # Handle text messages
                if 'message' in messaging_event:
                    message = messaging_event['message']
                    
                    if 'text' in message:
                        message_text = message['text'].lower().strip()
                        print(f"Received: {message_text}")
                        
                        if message_text in ['hi', 'hello', 'start', 'help']:
                            send_welcome_with_buttons(sender_id)
                        else:
                            send_message(sender_id, "မင်္ဂလာပါ။ အိမ်စာရင်းကြည့်ရန် 'hi' လို့ရိုက်ပါ။")
                    
                    if 'quick_reply' in message:
                        payload = message['quick_reply'].get('payload', '')
                        if payload.startswith('PRICE_'):
                            send_listings_carousel(sender_id, payload)
                
                # Handle postbacks
                elif 'postback' in messaging_event:
                    payload = messaging_event['postback'].get('payload', '')
                    if payload.startswith('PRICE_'):
                    send_listings_carousel(sender_id, payload)
                elif payload == 'GET_STARTED':
                    send_welcome_with_buttons(sender_id)
                    
                
                # Handle inbox_labels
                if 'inbox_labels' in messaging_event:
                    user_id = messaging_event['recipient']['id']
                    added_labels = messaging_event['inbox_labels'].get('added_labels', [])
                    for label in added_labels:
                        label_name = label.get('page_label_name', label.get('label_name', ''))
                        print(f"Label: {label_name}")
                        
                        if label_name == 'Hot Lead':
                            send_message(user_id, "မင်္ဂလာပါ VIP ဖောက်သည်ကြီး ကြိုဆိုပါတယ်")
                        elif label_name == 'သတိထားရမည့်သူ':
                            send_message(user_id, "ကျေးဇူးပြု၍ အချိန်ယူပြီး စစ်ဆေးပါ။")
                            print(f"⚠️ Warning: User {user_id} marked as 'သတိထားရမည့်သူ'")
                        elif label_name == 'လူလိမ်':
                            send_message(user_id, "သင့်အကောင့်အား စစ်ဆေးနေပါသည်။")
                            print(f"🚨 ALERT: User {user_id} marked as 'လူလိမ်'")
                        elif label_name == 'မှတ်ထားရမည့်သူ':
                            send_message(user_id, "ကျေးဇူးပါ။ သင့်အကြောင်းကို မှတ်သားထားပါမည်။")
                            print(f"📝 Info: User {user_id} marked as 'မှတ်ထားရမည့်သူ'")
                
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

# Call this once when the bot starts
setup_get_started()

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
