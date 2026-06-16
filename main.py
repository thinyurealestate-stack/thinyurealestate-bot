import os
import requests
from flask import Flask, request

app = Flask(__name__)

PAGE_ACCESS_TOKEN = os.environ.get("thinyurealestate")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "thinyurealestate")

# ========== YOUR LISTINGS DATA ==========
LISTINGS = {
     "PRICE_1": [
        {
            "title": "ယိုးဒယားစျေးအနီး,ရေ မီးစုံ အခန်း ၁ခန်းပါပတ်ဝန်းကျင်သန့် လူစည်ကားသောနေရာ",
            "subtitle": "ပထမထပ် 12.5x55.ပေကျယ်,၁၃၅၀(ညှိ့နိူင်းစျေး)ရောင်းမည်",
            "image_url": "https://i.postimg.cc/0Qys0Mf3/Image-15-06-2026-at-10-58-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1EJf62y4SH/"
        },
        {
            "title": "ဆယ်မိုင်ရန်ကြီးအောင်လမ်း,အရှေ့အလှည့်,မြေပိုင်မြေအမျိုးစား",
            "subtitle": "အဆက်စက်စာချုပ်-အရူပ်ရှင်းကင်း,၂၀x၆၀.၃၅၀၀(ညှိ့နိူင်း)",
            "image_url": "https://i.postimg.cc/cLZ15PKC/Image-15-06-2026-at-5-50-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1RB3W5xwpY/"
        }  
     ],
       
     "PRICE_2": [
        {
            "title": "ဘုရင့်နောင်လမ်းမကြီးမှလမ်းလျှောက်-၂မိနစ်သာဝင်ရ,တိုက်ခန်းစျေးနဲ့မို့အရယူပါရှင်",
            "subtitle": "ကိုယ်ပိုင်မီတာ မော်တာပါ,ပိုင်ရှင်ကိုယ်တိုင်ရောင်းချသောရှုပ်ရှင်းကင်း",
            "image_url": "https://i.postimg.cc/XqrsV4jY/Image-15-06-2026-at-10-49-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BNNHbSrc9/"
        },
        {
            "title": "အင်းစိန် မြို့နယ်- အောင်ဆန်း စျေးအနီး",
            "subtitle": "8×80 ပေ , 2BN နှစ်ထပ်အိမ်, 4400 သိန်း",
            "image_url": "https://i.postimg.cc/rmTRnYJK/Image-25-05-2026-at-4-44-PM-(4).png",
            "facebook_url": "https://www.facebook.com/share/p/1DaozjPCxM/"
        },
        {
            "title": "အင်းစိန်မြို့နယ်-ဂျပန်လမ်းနီး,အဘထ လမ်း,အဆက်စက်စာချုပ်-အရူပ်ရှင်းကင်း",
            "subtitle": "ဂရမ်မြေ-သိန်း ၂၈၀၀,စိတ်ညိမ်ရပ်ကွက်,ပတ်ဝန်းကျင်သန့်",
            "image_url": "https://i.postimg.cc/kgFWHsTK/IMG-5836.jpg",
            "facebook_url": "https://www.facebook.com/share/p/17jfG4U9PD/?mibextid=wwXIfr"
        },
        {
            "title": " လမ်းသစ်လမ်းမကြီး အနီး,နံသာမြို့င်လမ်း,Pro (1) global home အနီး",
            "subtitle": "ကား၂စီးကပ် ဂိုဒေါင်,လမ်းကျယ် ခြံအကျယ် 1770 Sqft,၂၆၅၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/1Rvnn33Y/IMG-5293.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1CdefBLAM3/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် ဖော့ကန်,ဝါဦး(၅)လမ်း-လမ်းကျယ်,စိတ်ညိမ်ရပ်ကွက်",
            "subtitle": "၁၅x၁၀၀.၂၈၀၀ ညှိ့နိူင်း,မြေပိုင်မြေအမျိုးစား,စည်ပင်မြေကွက်",
            "image_url": "https://i.postimg.cc/wB10Qh6X/Image-10-06-2026-at-5-00-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1D9GGGtkJ9/"
        },
        {
            "title": "ဆယ်မိုင် စျေးအနီး ရန်ကုန်းအောင်းလမ်း,ဘိုးဘပိုင် မြေ,အင်းစိန် မြို့နယ်",
            "subtitle": "ကား၂စီး ဂိုဒေါင်လမ်း,၃၀x၆၀.၅၅၀၀(ပါးပါး ညှော့)",
            "image_url": "https://i.postimg.cc/RCW6tzJ7/IMG-5263.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Kz23aMk3C/"
        },
        {
            "title": "Spring Line Hotel ကပ်လျက်, ဘိုးဘပိုင် မြေ",
            "subtitle": "27x78.3000-သိန်း(ညှိနိုင်း)",
            "image_url": "https://i.postimg.cc/nzkkQfXv/IMG-5253.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Fc4LMhbM9/"
        },
        {
            "title": "မှောင်ဘီ မြို့နယ်-မင်္ဂလာကုန်းရွာ,တခါတလေ အပန်းဖြေသွားမလား ဝယ်ထားရင်လည်းအမြတ်ရမှာနော်",
            "subtitle": "ခြံကျယ်၁ ဧကခွဲ,သိန်း၃၀၀၀(ပါးပါး ညှော့), မြေအမျိုးစား-G - မြေ",
            "image_url": "https://i.postimg.cc/d3g4Jm7H/post-558794-featured.jpg",
            "facebook_url": "https://www.facebook.com/share/r/17SwGtwbix/"
        },
        {
            "title": "မှင်းနန်ဒါလမ်းမကြီး ဒဲ့ဆင်း ၂လမ်းမြောက်, စျေးနီး ကျောင်းနီး ဘဏ်နီး မှတ်တိုင်အနီး capitalနီး",
            "subtitle": "၁၂ ပေ ခွဲ ပေ ၅၀,၁၀၉၀ပါးပါးညှိနိုင်း",
            "image_url": "https://i.postimg.cc/Mp6dqTXy/IMG-5244.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1JNAaEHcEz/"
        },
        {
            "title": "အင်းစိန် မြို့နယ်၊ မြို့သစ်ဘက် ခြမ်း,ပိုင်ကုန်းရပ်ကွက်",
            "subtitle": "ကားဝင်လိုရ လမ်းသွယ်လမ်းပိတ်မဟုတ်ပါ,၁၉၅၀$ တန်ဖိုးရောင်းမည်",
            "image_url": "https://i.postimg.cc/hPPTP4HC/IMG-5363.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18igS589wC/"
        }
    ],
    "PRICE_3": [
        {
            "title": "သာကေတ မြို့နယ်, အောင်သပြေ အနောက်(-)လမ်း,ဂရံအမည်ပေါက်အိမ်နှင့် ခြံအရောင်း",
            "subtitle": "ပေကျယ်၄၀'၆၀,သိန်း ၈၅၀၀ (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/HsXkdYRv/IMG-5193.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1BG5exRsdz/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် က+ခ ရက်ကွက်-ဘုရင့်နောင်လမ်းမကြီးအနီး မြို့သစ်စျေးအနီး",
            "subtitle": "၂၀x၆၀.၇၅၀၀(ညှိ့နိူင်း),လမ်းမကြီးမှလှမ်းကြည့်မြင်ရ",
            "image_url": "https://i.postimg.cc/VN02kybY/Image-10-06-2026-at-5-10-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1CeANQP3Ev/"
        },
        {
            "title": "ကျောက်ရေတွင်း လမ်းမဒဲ့ပေါက်လမ်းကျယ်,မရမ်းကုန်း မြို့နယ် ၅ရပ်ကွက်,စွယ်တောင်မြတ်စေတီတောင်အနီး",
            "subtitle": "ရေကူးကန်ငယ်တစ်ခုပါ,ဘိုးဘွားပိုင်အရပ်စာချုပ်,၈၅၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/zB4H2dHT/Image-25-05-2026-at-5-08-PM-(5).png",
            "facebook_url": "https://www.facebook.com/share/p/1EmM7sSUsU/"
        },
        {
            "title": "Lucky 7 Tea house အနီး,ရမ်းကုန်းမြို့နယ် ၅ ရက်ကွက်,Ocean center အနီး",
            "subtitle": "ခြံအကျယ် 18 × 58 ပေ,၉၈၀၀ သိန်း ညှီနှိုင်းစျေး,မြေပိုင်မြေ အဆက်စပ်စာချုပ်",
            "image_url": "https://i.postimg.cc/TwwG9NKn/Image-10-06-2026-at-5-06-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1JKXu3w7Qh/"
        },
        {
            "title": "အင်းစိန် မြို့နယ်- အောင်ဆန်း စျေးအနီး,ဘဏ်နီး- ကျောင်းနီး- စျေးနီး",
            "subtitle": "လမ်းမကြီးမှကားနဲ့၁မီးနှစ်သာဝင်ရ, ခြံကျယ်၂၅x၆၀ 6500 ညှိနိုင်း",
            "image_url": "https://i.postimg.cc/4dpXZwFh/Image-26-05-2026-at-1-12-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/18oLWtVcv6/"
        },
        {
            "title": "မရမ်းကုန်း မြို့နယ်၅ရပ်ကွက်,ရန်ကုန် လေဆိပ်အနီး,သဗ္ဗညုတ်ထိုးတောင်ကြီး အနီး",
            "subtitle": "ဂရန် ပြန်လျောက်လိုရသော မြေ, ခြံအကျယ်၄၀ × ၆၀ ပေ,၇၀၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/dtLSyDwn/Image-25-05-2026-at-5-14-PM-(1).png",
            "facebook_url": "https://www.facebook.com/share/p/18fMXD47JE/"
        },
        {
            "title": "ကျောက်ရေတွင်း လမ်းမဒဲ့ပေါက်,မရမ်းကုန်း မြို့နယ် ၅ရပ်ကွက်,ဘိုးဘွားပိုင် အဆက်စပ်စာချုပ်",
            "subtitle": "ခြံအကျယ်၂၅ × ၆၀ ပေ,၅၅၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/0Ntzb7Dn/Image-28-05-2026-at-11-44-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1CRS21Zhin/"
        }
    ],
    "PRICE_4": [
        {
            "title": "မရမ်းကုန် မြို့နယ်၉မိုင်၅ ရပ်ကွက်,ပြည်လမ်းမဒဲ့ပေါက်,ရန်ကုန် လေဆိပ်အနီး,ကား၂စီး ဂိုဒေါင်လမ်း",
            "subtitle": "40×80 ပေ, 11000 သိန်း",
            "image_url": "https://i.postimg.cc/RZbjLkv4/Image-26-05-2026-at-1-15-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1HdcYcGFfY/"
        },
        {
            "title": "လမ်းမကြီး အလွန်းနီး,အင်းစိန်မြို့နယ် ရွာမအရှေ့ရပ်ကွက်,အောက်မင်္ဂလာဒုံ လမ်းမကြီး အနီးကွယ်ကဘော အင်းစိန်ဆေးရုံကြီး အနီး",
            "subtitle": "ခြံအကျယ်  32 × 90 ပေအကျယ်,၁၃၀၀၀သိန်း (ပိုင်ရှင်တိုက်ရိုက် ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/qM14STTB/Image-10-06-2026-at-5-45-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1B4QFnC7zs/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် ရွာမအရှေ့ရပ်ကွက်,မင်းကြီးလမ်းမကြီး အနီး,အောက်မင်္ဂလာဒုံ လမ်းမကြီး အနီး",
            "subtitle": "ကားနှစ်စီရှောင် လမ်း ရပ်ကွက်သန့်,ခြံအကျယ်  25 × 90 ပေအကျယ်, ၁၂၀၀၀ သိန်း (ပိုင်ရှင်တိုက်ရိုက် ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/hvG37N3p/Image-10-06-2026-at-5-48-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1D7qMpgxfF/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် ဖော့ကန်ရပ်ကွက်,ဖောကန်စျေး အနီး ဝါဦးလမ်း,City Mart / KFC ကြက်ကြော် ဆိုင် အနီး",
            "subtitle": "ခြံအကျယ်  ၅၅x၉၀ပေ အကျယ်,၁၂၀၀၀ သိန်း ညှီနှိုင်းစျး,KBZ/AYA ဘဏ် များ နီး",
            "image_url": "https://i.postimg.cc/5NnRb9yk/IMG-5380.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18pY8chwks/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် ရွာမအရှေ့ ရပ်ကွက်,ကွယ်ကဘောဆေးရုံ အနီး,ဘိုကုန်းစျေး အနီးမင်းကြီးလမ်း /အောက်မင်္ဂလာဒုံ လမ်း အနီး",
            "subtitle": "ခြံအကျယ် ၅၀ × ၈၀ ပေ,၁၂၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/SKKC6qfD/Image-10-06-2026-at-5-14-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1DJGniW6jP/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် နဲသာကုန်း ရပ်ကွက်,လမ်းသစ်လမ်း မကြီး အနီး,Pro (1) Global Home အနီး",
            "subtitle": "ခြံအကျယ် ၄၀ × ၆၀ ပေ,၁၅၀၀၀ သိန်း ညှီနှိုင်းစျေး",
            "image_url": "https://i.postimg.cc/PqS2mSsj/Image-10-06-2026-at-4-53-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/18FHc9gwSo/"
        },
        {
            "title": "နာမည်ကြီး မင်းသမီး ခြံအနီး,မရမ်းကုန်း မြို့နယ်၅ ရပ်ကွက်,၉ မိုင်ဗိုလ်ညဏလမ်းသွယ်",
            "subtitle": "စိတ်ငြိမ်ရပ်ကွက်အမည်ပေါက်, ခြံအကျယ်၃၆ × ၆၂ ပေ,၁၅၅၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/XJH5bjZs/Image-27-05-2026-at-2-32-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BRai2EH5x/"
        },
        {
            "title": "အင်းစိန် မြို့နယ်၊ စောဘွားကြီးကုန်းရပ်ကွက်, လေဆိပ်ရိပ်သာ လမ်းသွယ်,Ocean Center အနီး",
            "subtitle": "တောင်ဘက်အလှည့်,ကား၂စီး ဂိုဒေါင်လမ်း, ခြံအကျယ်၆၀ × ၅၅,၁၅၀၀၀ သိန်း ညှိနိုင်းစျေး",
            "image_url": "https://i.postimg.cc/RhPqtX1s/Image-27-05-2026-at-2-52-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Hi635363E/"
        },
        {
            "title": "အင်းစိန် မြို့နယ်၊ စောဘွားကြီးကုန်းရပ်ကွက်, လေဆိပ်ရိပ်သာ လမ်းသွယ်,Ocean Center အနီး",
            "subtitle": "တောင်ဘက်အလှည့်,ကား၂စီး ဂိုဒေါင်လမ်း, ခြံအကျယ်၆၀ × ၅၅,၁၅၀၀၀ သိန်း ညှိနိုင်းစျေး",
            "image_url": "https://i.postimg.cc/RhPqtX1s/Image-27-05-2026-at-2-52-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Hi635363E/"
        }
    ],
    "PRICE_5": [
        {
            "title": "ရွေပြည်သာ Vip3 ရပ်ကွက်,အမှတ်၄လမ်းနဲ့တာတော်နီး,စာရွက်စာတမ်း အပြည့်အစုံ",
            "subtitle": "အိမ်အကျယ် - 35' x 55', ခြံအကျယ် 60' x 90', ရေကူးကန် - 15' x 30',သိန်း ၁၈,၀၀၀",
            "image_url": "https://i.postimg.cc/3JXYzLDM/Image-26-05-2026-at-1-46-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/14eeZywwfZo/"
        },
        {
            "title": "မရမ်းကုန်း မြို့နယ်၊ ကျိုက်ဝိုင်းအနီး,ဘိုးဘွားပိုင် မြေ (စာရွက်စာတမ်းအပြည့်အစုံ)BCC ကျပြီးသား",
            "subtitle": "၃ ထပ်ခွဲဆုံး စီးပွားရေးအသင့်သုံး အဆောက်အဦး 33' x 55',သိန်း 18,000 ညှိနိုင်း",
            "image_url": "https://i.postimg.cc/ZKZmS8mt/IMG-5255.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Xq4U7jYGz/"
        },
        {
            "title": "ပြည်လမ်းမကြီး အနီး,မရမ်းကုန်း မြို့နယ်၅ရပ်ကွက်,အဆက်ဆက်စာချုပ်",
            "subtitle": "ခြံအကျယ်၃၅ × ၅၅ ပေ,၁၆၅၀၀ သိန်းညှိနိုင်း",
            "image_url": "https://i.postimg.cc/q7LGYdpg/Image-29-05-2026-at-12-14-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1KQgHPSarU/"
        },
        {
            "title": "မရမ်းကုန်း ၅ ရပ်ကွက်, စွယ်တော်မြတ်စေတီအနီး,ကမ္ဘာအေးဗီလာအနီး",
            "subtitle": "မ မြေ 75’ × 30’ (ထောင့်ခြံ),ရောင်းစျေး  ၁၉၇၀၀ သိန်း (ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/mDkrpgcs/Image-10-06-2026-at-5-40-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BHpbqC2ao/"
        },
        {
            "title": "အင်းစိန် မြို့နယ်-မင်းဓမ္မလမ်းမကြီးအနီး,အောင်သိဒ္ဓိ Villa-နီး ဝိတိုရိယ ဆေးဆုံအနီး",
            "subtitle": "မြောက်အလှည့်, ပေကျယ်-၃၀x၁၂၀, သိန်း ၂ သောင်း",
            "image_url": "https://i.postimg.cc/664FbwHk/IMG-5364.jpg",
            "facebook_url": "https://www.facebook.com/share/p/18vbwdBjVv/"
        }
    ],
    "PRICE_6": [
        {
            "title": "လေဆိပ်ရိပ်သာလမ်းမ",
            "subtitle": "70×100 ပေ, 22000 သိန်း",
            "image_url": "https://i.postimg.cc/9Q4xCrj2/Image-26-05-2026-at-1-18-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1BDGbQti5V/"
        },
        {
            "title": "အင်းစိန်မြို့နယ် ရွာမအရှေ့ရပ်ကွက်,ဂျပန်လမ်းမကြီး အနီး,Jade Vista Hotel အနီး",
            "subtitle": "ခြံ အကျယ် - 122 × 220 ပေ,၂၈၅၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/7YdSgjWx/IMG-5374.jpg",
            "facebook_url": "https://i.postimg.cc/7YdSgjWx/IMG-5374.jpg"
        },
        {
            "title": "မရမ်းကုန်းမြို့နယ် (၉) ရပ်ကွက်,ကမ္ဘာအေးလမ်းမကြီးအနီး,ဂမုန်းပွင့်ကုန်တိုက်အနီး",
            "subtitle": "မြေအကျယ် 70' × 70' 4,900 Sqft,ရောင်းစျေး  ၂၉,၀၀၀ သိန်း ညှိနှိုင်း",
            "image_url": "https://i.postimg.cc/4xq3mgnR/Image-10-06-2026-at-4-56-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1Dhs8sqMsm/"
        },
        {
            "title": "၉မိုင် ပြည်လမ်းမ အလွန်းနီး လမ်းကျယ်,၉ မိုင် ဘောဂလမ်း,Ocean center အနီး",
            "subtitle": "ခြံအကျယ် 37 × 90 ပေ,၂၉၀၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/9QkTKF7B/IMG-5198.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1DCfLUWDbn/"
        }
    ],
    "PRICE_7": [
        {
            "title": "မရမ်းကုန်း မြို့နယ်၅ ရပ်ကွက်,၉မိုင် ရေနှင်းဆီမင်္ဂလာကန်အနီး",
            "subtitle": "ပြည်လမ်းမကြီး အနီး, ခြံအကျယ်၅၀ × ၇၀ ပေအကျယ်,၃၅၀၀၀ သိန်း (ညှိနိုင်း)",
            "image_url": "https://i.postimg.cc/c4Y9Vg9M/IMG-5355.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1EDpBUShAA/"
        },
        {
            "title": "မရမ်းကုန်းမြို့နယ် ဆိတ်ငြိမ်ရပ်ကွက်, ၉မိုင် ပြည်လမ်းဒဲ့ပေါက်အ",
            "subtitle": "SQFT - 3100ပေ,အဆောက်အဉီးအကျယ် 5 x 65 ( နှစ်ထပ်),သိန်း35000 ညှိနှိုင်း",
            "image_url": "https://i.postimg.cc/4yYWBVvw/Image-10-06-2026-at-5-19-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/18xKZp6Ane/"
        },
        {
            "title": "၇မိုင်ကုန်း မြင့်သာ,မရမ်းကုန်း မြို့နယ်,မင်းဓမ္မလမ်းမကြီး ပြည်လမ်းမ အနီး",
            "subtitle": "ခြံအကျယ်၅၀ × ၅၀ ပေ, လေးထောင့်ကျ ထောင့်ကွက်,၃၈၀၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/HxDjvNVS/IMG-5353.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1Ppiv2a38n/"
        },
        {
            "title": "၉မိုင်ပြည်လမ်းမဒဲ့ပေါက်,Ocean center အနီး,ကား၂စီး ဂိုဒေါင်လမ်းကျယ်",
            "subtitle": "ခြံအကျယ်၅၅×၁၀၀ ပေ,လူကြီး ရေကူးကန်,သိန်း ၄၀၀၀၀ သိန်း (ညှိနိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/s2FP1ggn/IMG-5121.jpg",
            "facebook_url": "https://www.facebook.com/share/p/17XtJz4td8/"
        }
    ],
    "PRICE_8": [
        {
            "title": "အင်းစိန်မြို့နယ် အောင်ဆန်းရပ်ကွက်,အောက်မင်္ဂလာဒုံ လမ်းမကြီးအနီးလမ်းမကြီးမှ လမ်လျောက် တစ်မီနစ် -လှမ်းကြည့်လမ်းမကြီးမြင်ရ",
            "subtitle": "ခြံအကျယ်-20 × 100ပေ,2RC.2ထပ်အိမ် ဌားမည်,၁လ ၁၅ သိန်း",
            "image_url": "https://i.postimg.cc/x8wxF5P3/710756262-1611823103238863-620643681076249583-n.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1HgdrNAccb/"
        }
    ],
    "PRICE_9": [
        {
            "title": "အင်းစိန်မြို့နယ် တောင်သူကုန်းရပ်ကွက်,မင်းကြီးလမ်း အနီး,ဘိုကုန်းစျေး ယိုးဒယာစျေး အနီး,ကွယ်ကဘော ဆေးရုံ အနီး",
            "subtitle": "ခြံအကျယ် ၁၀၀ × ၂၀၀  ပေ (20000Sqft),ကား ၃စီးရှောင်လမ်းအကျယ်,၅၀၀၀၀ သိန်း (ညှီနှိုင်းစျေး)",
            "image_url": "https://i.postimg.cc/BQgCHhG6/Image-10-06-2026-at-5-24-PM.png",
            "facebook_url": "https://www.facebook.com/share/p/1ByBBmDqcH/"
        }
    ],
    "PRICE_10": [],
    "PRICE_11": [],
    "PRICE_12": [
        {
            "title": "နှစ်မိုင် ကျောက်ဝိုင်းဘုရားလမ်းမကြီး,မရမ်းကုန်း မြို့နယ်၄ ရပ်ကွက်",
            "subtitle": "၇ ပေကျယ်နှစ်ဦးသုံး ကိုယ်ပိုင်လမ်း,၇၅၀၀၀ သိန်း (ညှိနိုင်း)",
            "image_url": "https://i.postimg.cc/NjgzNbct/IMG-5296.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1GeYDV6592/"
        }
    ],
    "PRICE_13": [
        {
            "title": "ရန်ကင်းမြို့နယ်,သုခီတာလမ်း,ကားသုံးစီး ရှောင် လမ်းကျယ်",
            "subtitle": "ခြံအကျယ် ၅၀ × ၇၀ ပေ,အိမ် အကျယ် ၃၀ × ၄၀ ပေ အိမ် အကျယ် ၃၀ × ၄၀ ပေ ,၈၉၀၀၀ သိန်း (ညှီနှိုင်း)",
            "image_url": "https://i.postimg.cc/3Nh2qhyH/Image-15-06-2026-at-10-53-AM.png",
            "facebook_url": "https://www.facebook.com/share/p/1GeYDV6592/"
        }
    ],
    "PRICE_14": [
        {    
            "title": "Luxury Residence ဘုရင့်နောင်တံတား အောက် မင်္ဂလာသန်းမြင့် ဘေးလမ်း",
            "subtitle": "မရမ်းကုန်း မြို့နယ်ရှိအဆင့်မြင့်လူနေမှုပုံစံ,သိန်းကြီး 120000ညှိနိုင်းစျေး",
            "image_url": "https://i.postimg.cc/W46PjY5h/IMG-5346.jpg",
            "facebook_url": "https://www.facebook.com/share/p/1EEaxo7r77/"
        }
    ]
}
# ========== SEND MESSAGE FUNCTION ==========
def send_feedback_message(recipient_id, message_text, thinyurealestate):
    url = f"https://graph.facebook.com/v21.0/me/messages?access_token={thinyurealestate}"
    
    payload = {
        "recipient": {"id": recipient_id},
        "messaging_type": "RESPONSE",
        "message": {"text": message_text}
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        # Log the FULL response for debugging
        print(f"Response Status: {response.status_code}", flush=True)
        print(f"Response Body: {response.text}", flush=True)  # <- This will show the exact error
        
        if response.status_code != 200:
            error_data = response.json()
            print(f"ERROR: {error_data}", flush=True)  # Show full error
            return None
            
        return response
    except Exception as e:
        print(f"Exception: {e}", flush=True)
        return None
# ========== PRICE QUICK REPLIES ==========
def send_price_quick_replies(recipient_id):
    """Send price range quick replies"""
    label_map = {
        "PRICE_1": "1.သိန်း၃ထောင်အောက်",
        "PRICE_2": "2.သိန်း၅ထောင်အောက်",
        "PRICE_3": "3.သိန်း၁သောင်းအောက်",
        "PRICE_4": "4.သိန်း၁သောင်းခွဲအောက်",
        "PRICE_5": "5.သိန်း၂သောင်းအောက်",
        "PRICE_6": "6.သိန်း၃သောင်းအောက်",
        "PRICE_7": "7.သိန်း၄သောင်းအောက်",
        "PRICE_8": "8.အငှားအိမ်များ",
        "PRICE_9": "9.သိန်း၅သောင်းအောက်",
        "PRICE_10": "10.သိန်း၆သောင်းအောက်",
        "PRICE_11": "11.သိန်း၇သောင်းအောက်",
        "PRICE_12": "12.သိန်း၈သောင်းအောက်",
        "PRICE_13": "13.သိန်း၉သောင်းအောက်",
        "PRICE_14": "14.သိန်းကြီးတန်အိမ်များ"
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
        url = f"https://graph.facebook.com/v18.0/me/messages?access_token={thinyurealestate}"
        payload = {
            "recipient": {"id": recipient_id},
            "message": {
                "text": "💰 စျေးနှုန်း ရွေးပါ:",
                "quick_replies": quick_replies
            }
        }
        requests.post(url, json=payload)

# ========== WELCOME WITH BUTTONS ==========
def send_welcome_with_buttons(recipient_id):
    """Send welcome message with price quick replies"""
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={thinyurealestate}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": "မင်္ဂလာပါ 👩‍💼🏘🏠\nမသင်းယုအိမ်ခြံမြေ အကျိုးဆောင်မှုကိုဆိုပါတယ်\n\n💜 Viber : 09767975004 💜\n\n📞 Contact :09424006004 📞\n\nအိမ်ကြည့်မယ်ဆို 3နာရီ ကြိုဆက်ပေးပါ 🏠\n\nအိမ်များကိုကျပ်သိန်း၁ ထောင်မှစ အောက်ကစျေးနှုန်းအတိုင်းဆွဲ၍ \n ကြည့်နိုင်ပါတယ်\n\n",
            "quick_replies": [
                {"content_type": "text", "title": "1.သိန်း၃ထောင်အောက်", "payload": "PRICE_1"},
                {"content_type": "text", "title": "2.သိန်း၅ထောင်အောက်", "payload": "PRICE_2"},
                {"content_type": "text", "title": "3.သိန်း၁သောင်းအောက်", "payload": "PRICE_3"},
                {"content_type": "text", "title": "4.သိန်း၁သောင်းခွဲအောက်", "payload": "PRICE_4"},
                {"content_type": "text", "title": "5.သိန်း၂သောင်းအောက်", "payload": "PRICE_5"},
                {"content_type": "text", "title": "6.သိန်း၃သောင်းအောက်", "payload": "PRICE_6"},
                {"content_type": "text", "title": "7.သိန်း၄သောင်းအောက်", "payload": "PRICE_7"},
                {"content_type": "text", "title": "8.အငှားအိမ်များ", "payload": "PRICE_8"},
                {"content_type": "text", "title": "9.သိန်း၅သောင်းအောက်", "payload": "PRICE_9"},
                {"content_type": "text", "title": "10.သိန်း၆သောင်းအောက်", "payload": "PRICE_10"},
                {"content_type": "text", "title": "11.သိန်း၇သောင်းအောက်", "payload": "PRICE_11"},
                {"content_type": "text", "title": "12.သိန်း၈သောင်းအောက်", "payload": "PRICE_12"},
                {"content_type": "text", "title": "13.သိန်း၉သောင်းအောက်", "payload": "PRICE_13"},
                {"content_type": "text", "title": "14.သိန်းကြီးတန်အိမ်များ", "payload": "PRICE_14"}
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

# ========== SETUP GET STARTED BUTTON ==========
def setup_get_started():
    """Register the Get Started button with Facebook"""
    url = f"https://graph.facebook.com/v18.0/me/messenger_profile?access_token={thinyurealestate}"
    payload = {"get_started": {"payload": "GET_STARTED"}}
    try:
        response = requests.post(url, json=payload)
        print(f"Get Started setup: {response.status_code}")
        if response.status_code != 200:
            print(f"Error: {response.text}")
        return response
    except Exception as e:
        print(f"Error setting up Get Started: {e}")
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
                    "title": "အသေးစိတ် ကြည့်ရန်"
                }
            ]
        })

    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={thinyurealestate}"
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
        send_message(recipient_id, "နောက်ထပ် စျေးနှုန်း တွေကိုလည်း အောက်မှာဆွဲ၍ နှိပ်ကြည့်နိုင်ပါတယ်:")
        send_price_quick_replies(recipient_id)
    except Exception as e:
        print(f"Error sending carousel: {e}")

# ========== WEBHOOK ==========
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Debug: Log the token (first few chars only for security)
    token = os.environ.get('PAGE_ACCESS_TOKEN')
    print(f"Token exists: {bool(token)}", flush=True)
    print(f"Token length: {len(token) if token else 0}", flush=True)
    
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if verify_token == VERIFY_TOKEN:
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

                    # Check quick_reply FIRST — before plain text
                    if 'quick_reply' in message:
                        payload = message['quick_reply'].get('payload', '')
                        if payload.startswith('PRICE_'):
                            send_listings_carousel(sender_id, payload)

                    elif 'text' in message:
                        message_text = message['text'].lower().strip()
                        print(f"Received: {message_text}")

                        if message_text in ['hi', 'hello', 'start', 'help']:
                            send_welcome_with_buttons(sender_id)
                        else:
                            send_message(sender_id, "မင်္ဂလာပါ။ အိမ်စာရင်း ကြည့်ရန် 'hi' လိုက်ရိုက်ပါ။")

                # Handle postbacks
                elif 'postback' in messaging_event:
                    payload = messaging_event['postback'].get('payload', '')
                    if payload.startswith('PRICE_'):
                        send_listings_carousel(sender_id, payload)
                    elif payload == 'GET_STARTED':
                        send_welcome_with_buttons(sender_id)

                # Handle inbox labels
                if 'inbox_labels' in messaging_event:
                    user_id = messaging_event['recipient']['id']
                    added_labels = messaging_event['inbox_labels'].get('added_labels', [])
                    for label in added_labels:
                        label_name = label.get('page_label_name', label.get('label_name', ''))
                        print(f"Label: {label_name}")

                        if label_name == 'Hot Lead':
                            send_message(user_id, "မင်္ဂလာပါ VIP ဖောက်သည်ကြီး ကြိုဆိုပါတယ်")
                        elif label_name == 'သတိထားရမည့်သူ':
                            send_message(user_id, "ကျေးဇူးပြု၍ အချိန်ယူ ပြီး စစ်ဆေးပါ။")
                            print(f"⚠️ Warning: User {user_id} marked as 'သတိထားရမည့်သူ'")
                        elif label_name == 'လူလိမ်':
                            send_message(user_id, "သင့်အကောင့်အား စစ်ဆေး နေပါသည်။")
                            print(f"🚨 ALERT: User {user_id} marked as 'လူလိမ်'")
                        elif label_name == 'မှတ်ထားရမည့်သူ':
                            send_message(user_id, "ကျေးဇူးပါ။ သင့်အကြောင်းကိုမှတ်သားထားပါမည်။")
                            print(f"📝 Info: User {user_id} marked as 'မှတ်ထားရမည့်သူ'")

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


# Call once when the bot starts
setup_get_started()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
