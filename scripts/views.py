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



#########################################
def orange500mega(passw, num):
    global info
    try:
        hd_500m = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '75',
            'Host': 'netapi.eu5.org',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.9.1',
        }
        data_500m = {
            "day": "", "phone": num, "count": "", "jus": "", "pass": passw, "event": "500orange",
            "code": ""
        }
        senddata_500m = r.post('http://netapi.eu5.org/api.php', data=data_500m, headers=hd_500m)
        info = senddata_500m.json()['msg']
        return info
    except:
        return 'حاول مره اخري لاحقا '
    


    
def orange500m(request):
    global info
    # print(request.POST)
    print('orange 500')
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

            send = orange500mega(password, number)
            user = "anas"
            if form.is_valid():
                print('valid')
                data = form.save(commit=False)
                # data.user_send = user
                data.plane = 'plane'
                data.customer_ip = 'ip_user'
                data.username = 'name'
                data.save()
                print(send)
                if "حاول مره اخري لاحقا" in send:
                    print(send)
                    messages.warning(request, f'خطأ في الرقم او كلمه المرور')
                elif 'لقد استمعت بالعرض من قبل،حاول فى وقت لاحق' in send:
                    print(send)
                    messages.warning(request, send)
                else:
                    print(send)
                    messages.success(request, send)

        except:
            print('bad password')
            messages.warning(request, f'خطأ في الرقم او كلمه المرور')

        return redirect('home_scripts')




    ##############################################
# @login_required(login_url="signup")
def home_scripts(request):
    return render(request, 'scripts/home_scripts.html')

    ##############################################

def orang_500_mg(request):
    if request.method == 'GET':
        return render(request, 'scripts/tiktok_sub.html')

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
    

    
def orange_100_mg(request, number, password):
    if request.method == 'GET':
        return render(request, 'scripts/tiktok_sub.html')

    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']

        print(f'num = {number} | pass = {password}')
        send = add_100mg(number, password)
        print('send')

        if not send[0]:
            messages.error(request, send[1])
        else:
            messages.success(request, send)

        
        return redirect('home_scripts')
