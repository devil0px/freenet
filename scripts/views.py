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

        #print(f'num = {number} | num2 ={number2}| pass = {password}')
        send = add_100mg(number, number2, password)
        send2 = delete_100mg(number, number2, password)
        print('send2')

    return redirect('home_scripts')
