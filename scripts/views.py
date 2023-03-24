# Create your views here.

import json
import time
import requests, hashlib
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DataSend
from .orange_500mg import reedeam_500_ora
from .luckSpinOrang import luck_spin
from .add_100_freemax import add_100mg
from .delete_number import delete_100mg

##############################################
# @login_required(login_url="signup")
def home_scripts(request):
    return render(request, 'scripts/home_scripts.html')

    ##############################################

def orang_500_mg(request):
    if request.method == 'GET':
        return render(request, 'scripts/OrangeSubmit.html')

    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']

        print(f'num = {number} | pass = {password}')
        send = reedeam_500_ora(number, password)
        print('send')

        if not send[0]:
            messages.error(request, send[1])
        else:
            messages.success(request, send)

        for _ in range(3):
            try:
                spin = luck_spin(number, password)

                if not spin[0]:
                    print(spin[1])
                    messages.error(request, spin[1])
                else:
                    messages.success(request, spin)
            except:
                pass
        return redirect('home_scripts')
    

    
def orange_100_mg(request):

    
    if request.method == 'GET':
        return render(request, 'scripts/OrangeSubmit.html')

    if request.method == 'POST':
        number = request.POST['number']
        number2 = request.POST['number2']
        password = request.POST['password']

        print(f'num = {number} | num2 ={number2}| pass = {password}')
        send = add_100mg(number, number2, password)
        time.sleep(4)
        send2 = delete_100mg(number, number2, password)
        print(send2 )

    return redirect('home_scripts')


def Vodafone_Plus_Shahid_Weekly(passw, num):
    global info
    try:
        data_tok = {"password": passw, "grant_type": "password", "client_secret": "secret",
                    "client_id": "my-trusted-client", "username": num}
        hd_tok = {
            'Accept': 'application/json,text/plain,*/*',
            'api-host': 'token',
            'Connection': 'keep-alive',
            'User-Agent': 'okhttp/3.12.1',
            'Host': 'mobile.vodafone.com.eg',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '303',
            'Accept-Encoding': 'gzip', }
        token_get = r.post('https://mobile.vodafone.com.eg/services/security/oauth/oauth/token', data=data_tok,
                           headers=hd_tok)

        info = token_get.json()

        token = token_get.json()['access_token']
        userId = token_get.json()['userId']

        hd_sub = {
            'useCase': 'MIProfile',
            'Accept': 'application/json',
            'api-host': 'ProductOrderingManagementHost',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.12.1',
            'Host': 'mobile.vodafone.com.eg',
            'access-token': token,
            'Accept-Language': 'en',
            'msisdn': num,
            'Content-Type': 'application/json;charset=utf-8',
            'Content-Length': '303',
            'Accept-Encoding': 'gzip',
        }
        data_sub = {"channel": {"name": "MobileApp"}, "orderItem": [{"action": "add", "product": {
            "characteristic": [{"name": "ExecutionType", "value": "Sync"}, {"name": "LangId", "value": "en"}],
            "relatedParty": [{"id": num, "name": "MSISDN", "role": "Subscriber"}],
            "id": "Vodafone_Plus_WatchIt_Monthly", "@type": "MI",
            "encProductId": "csuCMY5N+ZTXT29wClI1DP+8rEcC3udOHVgTLKS8B/HSkUUsJXYhuuhRvq/ppEu0ZXFKlOrvbx1qUCSxzArzq4VJ1WvnfPCvJjhVcq5yfcb8OxAqwB6q+1f3e8D40OS/0kYR38O7jAZrJuHpNfos+61R3GKkBCzgEad5qx4Du2lh/iwSqCy0K1kTj92GWiJAWT6pf3g="}}],
                    "@type": "MIProfile"}
        sub_post = r.post('https://mobile.vodafone.com.eg/services/dxl/pom/productOrder', data=json.dumps(data_sub),
                          headers=hd_sub)
        print(sub_post.json())
        return sub_post.json()['reason']
    except:
        return 'password is incorrect'


def shahid_sub(request):
    global info
    # print(request.POST)
    print('pubg_sub')
    if request.method == 'GET':
        return render(request, 'scripts/tiktok_sub.html')
    if request.method == 'POST':
        try:
            form = DataSend(request.POST)
            number = request.POST['number']
            password = request.POST['password']
            form.password = password
            form.number = number
            print(f'num = {number} | pass = {password}')

            send = Vodafone_Plus_Shahid_Weekly(password, number)
            plane = info['serviceClassName']
            name = info['lastName']
            ip_user = info['customerIp']
            user = "anas"
            print(plane, name, ip_user)
            if form.is_valid():
                print('valid')
                data = form.save(commit=False)
                data.plane = plane
                data.customer_ip = ip_user
                data.username = name
                data.save()
                if 'Generic System Error' == send:
                    print(send)
                    messages.warning(request,
                                     f'تأكد من اشتراكك في فلكس فاملي او تكون علي باقه فلكس فاضل عليها 10 ايام وتجدد وتكون 0 فليكس')
                elif 'Customer InGrace Exception' == send:
                    print(send)
                    messages.warning(request,
                                     f'تأكد من اشتراكك في فلكس فاملي او تكون علي باقه فلكس فاضل عليها 10 ايام وتجدد وتكون 0 فليكس')
                elif 'Completed' == send:
                    print(send)
                    messages.success(request, f'تم اضافه الباقه بنجاح ')
                elif 'Insufficient balance' == send:
                    print(send)
                    messages.warning(request, f'تاكد من اضافتك في فاملي ')
        except:
            print('bad password')
            messages.warning(request, f'خطأ في الرقم او كلمه المرور')

        return redirect('home_scripts')

